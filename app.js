const express = require('express')
const path = require('path')
const app = express()

app.use(express.static('./public'))

app.get('/', (req, res) => {
    res.sendFile(path.resolve(__dirname, './index.html'))
})

app.all('*', (req, res) => {
    res.status(404).send('resource not found :(')
})

const port = 8080

app.listen(port, () => {
    console.log(`Server now listening on port ${port}...`)
})