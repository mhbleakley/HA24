
async function getText(file, id) {
    let myObject = await fetch(file);
    let myText = await myObject.text();
    document.getElementById(id).innerHTML = myText;
}

function updateSpotify(){
    getText('./data/martin_spotify.txt', 'mb_spotify')
}

setInterval(updateSpotify, 1000)