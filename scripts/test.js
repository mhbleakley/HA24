getText("./data/martin_currently_due.txt");

async function getText(file) {
    let myObject = await fetch(file);
    let myText = await myObject.text();

    document.getElementById("todo").innerHTML = myText;
}