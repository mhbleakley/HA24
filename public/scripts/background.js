async function getImage(file){
    let image = await fetch(file);
    let blob = await image.blob();
    let image_url = await URL.createObjectURL(blob);
    document.getElementById('main_body').style.backgroundImage = `url(${image_url})`;
}

function change_background(){
    const im_url = getImage('./resources/backgrounds/background.jpg');
}

setInterval(change_background, 3600000);