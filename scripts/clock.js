function update_time() {
    const now = new Date();
    const currentDateTime = now.toLocaleString();
    var edit = new Array();
    for (let i = 0; i < currentDateTime.length; i++) {
        if (currentDateTime[i] !== ','){
            edit.push(currentDateTime[i]);
        }
    }
    const editstr = edit.join("")
    document.querySelector('#datetime').textContent = editstr;
}

setInterval(update_time, 1000);