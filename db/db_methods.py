from . import db_connection


def add_language(name,iso,characters,speakers):
    try:
        conn = db_connection.db_connect()
        cursor = conn.cursor()

        cursor.execute(f" insert into Languages(Name,Iso,Characters,Speakers) values ('{name}','{iso}','{characters}',{speakers})")

        cursor.execute("select * from Languages")
        result = cursor.fetchall()
        print(result)
        cursor.commit()
        cursor.close()
        conn.close()
    except Exception as e:
        print(e)
    

def get_languages():
    try:
        conn = db_connection.db_connect()
        cursor = conn.cursor()

        cursor.execute(f"select * from Languages")
        result = cursor.fetchall()
        cursor.close()
        conn.close()
        print(result)
        return result
        
    except Exception as e:
        print(e)