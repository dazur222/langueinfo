

async function getLanguages(){
    let promesa = await fetch("/get_languages")
    let languages = await promesa.json()

    return languages
}

async function postLanguage() {

    try {
        let name = document.getElementById('name').value
        let iso = document.getElementById('iso').value
        let characters = document.getElementById('characters').value
        let roots = document.getElementById('roots').value
        let speakers = document.getElementById('speakers').value


        let data = {
            name : name,
            iso : iso,
            characters: characters,
            roots : roots,
            speakers : speakers
        }

        console.log(data)

        event.preventDefault()

        let promesa = await fetch("/post_language",{
            method : 'POST',
            headers : {
                'Content-Type' : 'application/json'
            },
            body : JSON.stringify(data)
        })

        let respuesta = await promesa.json()

        console.log(respuesta)
            
    } catch (error) {
        console.log(error)
    }
    
}


async function generateLanguage(){
    let languages = await getLanguages()



    let nombres = ["Papulenguaje","El dialecto perdido de la tribu autoctona Kh,ur","Juanasm","Ñoñil","Alck,ul"]
    let iso = ["autismo","lol","hgf","tcp","sql"]
    let roots = ["tribu amazona","aldama","papunaca tradicional"]
    let char_set = "";
    console.log(languages)
    while(char_set.length < 8){
        for(let lang of languages){
            let num_random = Math.floor(Math.random() * (lang.characters.length))
            
            char_set += lang.characters[num_random]
        }
    }
    let ran = Math.floor(Math.random()*nombres.length)
    console.log(ran)
    document.getElementById('name').value = nombres[ran]
    
       
    document.getElementById('iso').value = iso[Math.floor(Math.random()*(nombres.length))]
    document.getElementById('characters').value = char_set
    document.getElementById('roots').value = roots[Math.floor(Math.random()*(roots.length))]

    document.getElementById('speakers').value = Math.floor(Math.random() * 2000)


    console.log(char_set)
}
function displayLanguages(languages){
    
    let display = document.getElementById("languages_display");

    let newDisplay

    for( let language of languages){
        console.log(language)
        let temp = `<p>${language.Name}</p>
        
        <h1>${language.Iso}</h1>
        
        <p>${language.Characters}</p>
        
        <p>${language.Speakers}</p>
        `
        newDisplay += temp
    }

    display.innerHTML = newDisplay

}

