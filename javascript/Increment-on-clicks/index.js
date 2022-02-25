count = 0

function increment(){
    count += 1
    document.getElementById("count-el").innerHTML = count
}

function save(){
    console.log(count)
}


welcomeEl = document.getElementById("welcome-el")
name = "Ian Zdanowsky"
greetings = "Welcome back, "

welcomeEl.innerHTML = greetings + name
welcomeEl.innerHTML += "!"
