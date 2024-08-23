var http = require('http');
var fs = require('fs');
var path = require('path');

port = 8080;
hostname = '127.0.0.1';

const server = http.createServer(function (req, res) {
    var filePath = req.url;
    if (filePath == '/') filePath = '/index.html';

    filePath = __dirname+filePath;
    var extname = path.extname(filePath);
    var contentType = 'text/html';

    switch (extname) {
        case '.js':
        contentType = 'text/javascript';
        break;
        case '.css':
        contentType = 'text/css';
        break;
    }

    fs.exists(filePath, function(exists) {
        if (exists) {
            fs.readFile(filePath, function(error, content) {
                if (error) {
                    res.writeHead(500);
                    res.end();
                }
                else {                   
                    res.writeHead(200, { 'Content-Type': contentType });
                    res.end(content, 'utf-8');                  
                }
            });
        }
    });
});

server.listen(port, hostname, () => {
    console.log(`Server running at http://${hostname}:${port}/`);
});