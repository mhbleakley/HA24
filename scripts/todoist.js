// Create a blob containing the text
const blob = new Blob([
    document.getElementById("data").textContent
], { type: "text/plain" })

// Read the "file"
const fileReader = new FileReader();
fileReader.onload = function() {
    console.log("Contents:");
    for (const line of fileReader.result.split(/\r?\n/)) {
        console.log(line);
    }
};
fileReader.readAsText(blob);