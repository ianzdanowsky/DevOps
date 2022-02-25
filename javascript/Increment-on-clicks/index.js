let count = 0
let saveEl = document.getElementById("save-el")
let welcomeEl = document.getElementById("welcome-el")
let countEl = document.getElementById("count-el")



function increment(){
    count += 1
    countEl.innerHTML = count
}


// Save last entries

function save(){
    let lastCount = count + " - "
    saveEl.innerHTML += lastCount
}

// Add welcoming greet

name = "Ian Zdanowsky"
greetings = "Welcome back, "

welcomeEl.innerHTML = greetings + name
welcomeEl.innerHTML += "!"

//



