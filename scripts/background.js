async function getText(file, id) {
    let myObject = await fetch(file);
    let myText = await myObject.text();

    document.getElementById(id).innerHTML = myText;
}

function change_background(){
    document.getElementById('main_body').style.backgroundImage = 'url("./resources/backgrounds/firewatch_day.jpg")';
}

setInterval(change_background, 5000);