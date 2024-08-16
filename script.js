function update_time() {
    const now = new Date()
    const currentDateTime = now.toLocaleString()
    
    document.querySelector('#datetime').textContent = currentDateTime;
}

setInterval(update_time, 1000);