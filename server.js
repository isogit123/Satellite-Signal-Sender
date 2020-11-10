var fs = require('fs');
const exp = require('express');
const app = exp();

const server = require('http').createServer(app);
const io = require('socket.io')(server);
io.on('connection', client => { 
client.on('image', data => {
client.broadcast.emit('image', data);
 });
 
 client.on('roi', data => {
client.broadcast.emit('roi', data);
 });
 
 client.on('receiveSignal', data => {
client.broadcast.emit('receiveSignal', data);
 });
 
  client.on('resetRoi', data => {
client.broadcast.emit('resetRoi', data);
 });
 
});
app.use(exp.static(__dirname));

app.get('/rec', function(req, res){
  res.sendFile(__dirname + '/receiver.html');
});
server.listen(5022);