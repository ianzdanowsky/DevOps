count = 0

function increment(){
    count = count + 2
    document.getElementById("count-el").innerHTML = count
}

function save(){
    console.log(count)
}