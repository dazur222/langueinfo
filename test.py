
language_a = {
    'characters' : "abcdefasdfghjké"
}


language_b = {
    'characters' : "eqwertyuio"
}


def similarities(language_a,language_b):
    #recibe un diccionario con los datos de los dos lenguajes
   
    char_set_a = set(language_a['characters'])
    char_set_b = set(language_b['characters'])

    sim = char_set_a.intersection(char_set_b)


    if sim != set():
        full = 100
        val = 100 / len(char_set_a)
        for char in char_set_a:
            if char not in sim:
                full = full - val

        return { 'porcentage' : full, 'similiarities' : sim}
    else:
        return {'similarities' : "no similarities"}
   



similarities(language_a,language_b)
