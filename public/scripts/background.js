

// let lightMode = checkLightMode()

// function checkLightMode(){
//     const darkModeBegin = [14, 1] // hours and minutes
//     const lightModeBegin = [8, 0]

//     const now = new Date()
//     const h = now.getHours()
//     const m = now.getMinutes()

//     if(h >= darkModeBegin[0] && m >= darkModeBegin[1]){ // darkModeBegin to 00:00
//         return false
//     }else if(h < lightModeBegin[0]){ // 00:00 to lightModeBegin
//         return false
//     }else if(m < lightModeBegin[1]){ // lightModeBegin[0] to lightModeBegin[1] i.e. 8:00 to 8:30
//         return false
//     }else{ // after lightModeBegin and before darkModeBegin
//         return true
//     }
// }

// function lmao1(){
//     lightMode = checkLightMode()
// }

// setInterval(checkLightMode, 1000)

// function lmao(){
//     console.log(lightMode)
// }

// setInterval(lmao, 1000)

// // function setBackground(){
// //     const lightMode = checkLightMode()

// //     console.log(lightMode)
// // }

// // setInterval(setBackground, 1000)


startImageTransition();
    
function startImageTransition() {
    let images = document.getElementsByClassName("background_img");

    for (let i = 0; i < images.length; ++i) { // set all images to opacity 1
        images[i].style.opacity = 1;
        images[i].style.zIndex = -2; // all -2
    }

    let topZIndex = 0; // topZIndex will store index of top-most image
    let currentImageIndex = images.length - 1; // last image listed in html

    setInterval(changeImage, 1800000);

    async function changeImage() {
        let nextImageIndex = (1 + currentImageIndex) % images.length; // rotates through list i.e. len = 10: 9, 10=0, 11=1, 12=2, etc.

        images[currentImageIndex].style.zIndex = topZIndex;
        images[nextImageIndex].style.zIndex = topZIndex - 1;

        await transition(); // fade current image to total transparency

        images[currentImageIndex].style.zIndex = -2; // send faded image back behind
        images[nextImageIndex].style.zIndex = topZIndex; // moving this up to 0, hopefully changing nothing
        images[currentImageIndex].style.opacity = 1;
        currentImageIndex = nextImageIndex;
    }

    function transition() {
        return new Promise(function (resolve, reject) {

            let del = 0.01;
            let id = setInterval(changeOpacity, 10);

            function changeOpacity() {
                images[currentImageIndex].style.opacity -= del;
                if (images[currentImageIndex].style.opacity <= 0) {
                    clearInterval(id);
                    resolve();
                }
            }
        })
    }
}