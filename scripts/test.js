async function getText(file, id) {
    let myObject = await fetch(file);
    let myText = await myObject.text();

    document.getElementById(id).innerHTML = myText;
}

async function getStuff() {
    getText("./data/martin_currently_due.txt", 'mb_todo');
    getText('./data/izzy_GROCERY_LIST_section.txt', 'grocery');
    getText('./data/izzy_currently_due.txt', 'in_todo');
}

setInterval(getStuff, 60000);