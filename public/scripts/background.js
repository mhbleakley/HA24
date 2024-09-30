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