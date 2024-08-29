function leading_zeros(x) {
    if (x < 10){
        x = '0'.concat(x);
    }
    return x;
}

function update_time() {
    const now = new Date();
    let h = leading_zeros(now.getHours());
    let m = leading_zeros(now.getMinutes());
    let s = leading_zeros(now.getSeconds());

    let time = ''.concat(h, ':', m, ':', s)
    document.querySelector('#datetime').textContent = time;
}

setInterval(update_time, 1000);