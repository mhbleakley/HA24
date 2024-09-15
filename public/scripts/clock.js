function leading_zeros(x) {
    if (x < 10){
        x = '0'.concat(x);
    }
    return x;
}

function dayToWord(day) {
    week = ['Sunday',
            'Monday',
            'Tuesday',
            'Wednesday',
            'Thursday',
            'Friday',
            'Saturday'
    ]
    return week[day];
}

function update_time() {
    const now = new Date();
    let mnth = now.getMonth();
    let day = now.getDate();
    let dayOfWeek = dayToWord(now.getDay());
    let h = leading_zeros(now.getHours());
    let m = leading_zeros(now.getMinutes());
    let s = leading_zeros(now.getSeconds());

    
    let date = ', '.concat(mnth, '/', day, ",\t")
    let time = ''.concat(h, ':', m, ':', s)
    document.querySelector('#datetime').textContent = dayOfWeek.concat(date, time);
}

setInterval(update_time, 1000);