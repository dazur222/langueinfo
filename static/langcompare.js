

document.addEventListener('DOMContentLoaded' ,async function (){

    let languages = await getLanguages()

    console.log(languages)
    loadLanguagesOptions(languages)
    

})

async function getSimilarities() {
    let option_a = document.getElementById('language_a').value
    let option_b = document.getElementById('language_b').value


    let languages = await getLanguages()
    let lang_a,lang_b

    for(let language of languages){
        if (language.name == option_a){
            lang_a = language
        }
    }

    for(let language of languages){
        if (language.name == option_b){
            lang_b = language
        }
    }

    let promesa = await fetch("/get_similarities" ,{
        method : "POST",
        headers : {
            'Content-Type' : 'application/json'
        },
        body : JSON.stringify({lang_a : lang_a, lang_b : lang_b})
    })
    let sim = await promesa.json()

    let display = document.getElementById('similarities_display')

    if(sim.similarities == "no similarities"){
        display.innerHTML = '<h1>There are no similarities</h1>'
    }
    else{
            

        let info = `
        <p>The percentage of similiraty is of ${sim.percentage}%</p>
        <p>This are their characthers in common ${sim.similarities}</p>`


        display.innerHTML = info        
    }

    console.log(sim)
}

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
