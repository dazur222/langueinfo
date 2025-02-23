async function getLanguages(){
    let promesa = await fetch("get_languages")
    let languages = await promesa.json()

    console.log(languages)
}


function displayLanguages(languages){
    let display = document.getElementById("languages_display")

    let newDisplay

    for( let language in languages){
        let temp = ``
    }

}