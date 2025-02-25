from . import db_connection


def add_language(name,iso,characters,speakers,official):
    try:
        conn = db_connection.db_connect()
        cursor = conn.cursor()

        cursor.execute(f"INSERT INTO Languages (Name, Iso, Characters, Speakers, Official) VALUES (N'{name}', N'{iso}', N'{characters}', {speakers}, {official})")

        cursor.execute(f"SELECT TOP 1 * FROM Languages ORDER BY Id DESC")
        
        columns = [column[0] for column in cursor.description]
        rows = cursor.fetchall()    


        cursor.commit()
        cursor.close()
        conn.close()

        return dictionarify(columns,rows)
    except Exception as e:
        print(e)
    

def get_languages():
    try:
        conn = db_connection.db_connect()
        cursor = conn.cursor()

        cursor.execute(f"select * from Languages")
        
        columns = [column[0] for column in cursor.description]
        rows = cursor.fetchall()    

        cursor.close()
        conn.close()
        
        return dictionarify(columns,rows) 
        
    except Exception as e:
        print(e)

def dictionarify(colums,rows):
    try:

        result =  [ dict(zip(colums,row)) for row in rows ]  
        
        
        return result
    
    except Exception as e:
        # Print the exception for debugging purposes
        print(f" Error en la creacion del diccionario: {e}")
