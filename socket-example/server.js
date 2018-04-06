var application_root = __dirname;
var express = require('express');
var path 	= require("path");
var bodyParser = require('body-parser');
var logger = require('morgan');

var app = express();
	
var	server = require('http').createServer(app);
var io = require('socket.io').listen(server);


app.use(logger('dev'));
app.use(bodyParser());
app.use(express.static(path.join(__dirname, 'public')));


///DATA
function getRandomInt(min, max) {
	return Math.floor(Math.random() * (max - min + 1)) + min;
}

io.sockets.on('connection', function (socket) {
	
	setInterval(function(){
		var data = getRandomInt(0,100);
		io.sockets.emit('pushdata', data);
	},1000);
	
});

server.listen(8070);
console.log('Server is listening on port 8070...');
