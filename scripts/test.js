// function loadDoc(){
//     var xhttp = new XMLHttpRequest();

//     xhttp.onreadystatechange = function () {
//         if (this.readyState == 4 && this.status == 200){
//             document.getElementById('demo').innerHTML = this.responseText();
//         }
//     };

//     xhttp.open('GET', 'lmao.txt', true);
//     xhttp.send();
// }
getText("lmao.txt");

async function getText(file) {
    let myObject = await fetch(file);
    let myText = await myObject.text();
    document.getElementById("demo").innerHTML = myText;
}