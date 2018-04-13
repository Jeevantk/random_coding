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




function getAngFreq(time) {
	return Math.PI*2 * time * this.freq;
};


var amplitude=50;
var phase=4;

function sinewave(time) {
	var y= amplitude*Math.sin(getAngFreq(time)+phase);
	return y;
}

console.log(sinewave(5));
var i=0;

io.sockets.on('connection', function (socket) {
	
	setInterval(function(){
		var data = getRandomInt(10,100);
		// var data=sinewave(i)+30;
		io.sockets.emit('pushdata', data);
		console.log("Data Pushed ",data);
		i=i+1;
	},1000);
	
});

server.listen(8070);
console.log('Server is listening on port 8070...');
