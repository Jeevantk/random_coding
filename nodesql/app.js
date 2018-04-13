var db = require('./db');

// var insertElement ={id:5,tempValue:10.09};
var temp = 30;
db.query('INSERT INTO tempurature (tempValue) VALUES (?)',temp,function(err,result){
	if(err) throw err;
	console.log("Inserted");
});