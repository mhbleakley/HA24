

let lightMode = checkLightMode()

function checkLightMode(){
    const darkModeBegin = [14, 1] // hours and minutes
    const lightModeBegin = [8, 0]

    const now = new Date()
    const h = now.getHours()
    const m = now.getMinutes()

    if(h >= darkModeBegin[0] && m >= darkModeBegin[1]){ // darkModeBegin to 00:00
        return false
    }else if(h < lightModeBegin[0]){ // 00:00 to lightModeBegin
        return false
    }else if(m < lightModeBegin[1]){ // lightModeBegin[0] to lightModeBegin[1] i.e. 8:00 to 8:30
        return false
    }else{ // after lightModeBegin and before darkModeBegin
        return true
    }
}

function lmao1(){
    lightMode = checkLightMode()
}

setInterval(checkLightMode, 1000)

function lmao(){
    console.log(lightMode)
}

setInterval(lmao, 1000)

// function setBackground(){
//     const lightMode = checkLightMode()

//     console.log(lightMode)
// }

// setInterval(setBackground, 1000)