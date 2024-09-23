

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
        console.log(images[i].style.zIndex)
    }

    let top = -1;
    let cur = images.length - 1;

    setInterval(changeImage, 10000);

    async function changeImage() {
        let nextImage = (1 - cur) % images.length;

        images[cur].style.zIndex = top - 1;
        images[nextImage].style.zIndex = top;

        await transition();

        images[cur].style.zIndex = top;
        images[nextImage].style.zIndex = top - 1;
        top = top - 1;
        images[cur].style.opacity = 1;
        cur = nextImage;
    }

    function transition() {
        return new Promise(function (resolve, reject) {

            let del = 0.01;
            let id = setInterval(changeOpacity, 10);

            function changeOpacity() {
                images[cur].style.opacity -= del;
                if (images[cur].style.opacity <= 0) {
                    clearInterval(id);
                    resolve();
                }
            }
        })
    }
}