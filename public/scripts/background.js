
let current_index = 0;

async function getText(file) {
    let myObject = await fetch(file);
    let myText = await myObject.text();
    return myText;
}

function change_background(){
    const text = getText('./data/backgrounds.txt');

    const lines = text.finally();
    console.log(lines);

    // const im_url = getImage('./resources/backgrounds/background.jpg');
    // current_index = current_index + 1;
    // if (current_index > )
}

setInterval(change_background, 2000);