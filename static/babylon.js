

async function getLanguages(){
    let promesa = await fetch("/get_languages")
    let languages = await promesa.json()

    console.log(languages)

    displayLanguages(languages)
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
function displayLanguages(languages){
    
    let display = document.getElementById("languages_display")

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