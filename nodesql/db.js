var mysql = require('mysql');
var con = mysql.createConnection({
	host:"localhost",
	user:"root",
	password:"theeta",
	database : 'btp'
});

con.connect(function(err){
	if(err) throw err;
	console.log("Connected to the MySQL DataBase");
});

module.exports = con;