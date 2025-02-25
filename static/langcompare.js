

document.addEventListener('DOMContentLoaded' ,async function (){

    let languages = await getLanguages()

    console.log(languages)
    loadLanguagesOptions(languages)
    

})


function loadLanguagesOptions(languages){

    let lang_a = document.getElementById('language_a')
    let lang_b = document.getElementById('language_b')

    let option = document.createElement("option")
    for(let language of languages){
        let option = document.createElement("option")

        let name = language.name

        option.value = name
        option.text = name

        lang_a.appendChild(option)
        
    }


    for(let language of languages){
        let option = document.createElement("option")

        let name = language.name

        option.value = name
        option.text = name

        lang_b.appendChild(option)
        
    }

}



async function getLanguages(){
    let promesa = await fetch("/get_languages")
    let languages = await promesa.json()

    return languages

}
