function update_time() {
    const now = new Date()
    const currentDateTime = now.toLocaleString()
    // const edit = new Array()
    // for (let i = 0; i < currentDateTime.length; i++) {
    //     if (currentDateTime[i] != ','){
    //         edit.push(currentDateTime[i])
    //     }
    // }
    document.querySelector('#datetime').textContent = currentDateTime;
}

setInterval(update_time, 1000);