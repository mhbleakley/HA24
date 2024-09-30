async function getText(file, id) {
    let myObject = await fetch(file);
    let myText = await myObject.text();

    document.getElementById(id).innerHTML = myText;
}

async function getStuff() {
    getText("./data/backgrounds.txt", 'background_holder');
}

getStuff();

// setInterval(getStuff,  1800000);