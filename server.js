const express = require('express')
console.clear()
const app = express()
const path = require('path')
app.use(express.static(path.join(__dirname,"/resources")))
app.get('/',(req, res) => {
  res.sendFile(path.join(__dirname,"./Home.html"))
})
app.get('/test',(req, res) => {
    res.sendFile(path.join(__dirname,"./test.html"))
  })
app.get('/home',(req, res) => {
    res.sendFile(path.join(__dirname,"./Home.html"))
  })
app.get('/attendance', (req, res) => {
    res.sendFile(path.join(__dirname,"./Attendance.html"))
  })
  app.get('/graph', (req, res) => {
    res.sendFile(path.join(__dirname,"./Graph.html"))
  })
app.get("/get-data",(req,res)=>{
  res.sendFile(path.join(__dirname+"/resources/database/text.txt"));
})
app.listen(3000,(req,res)=>{
    console.log("Server is running")
})