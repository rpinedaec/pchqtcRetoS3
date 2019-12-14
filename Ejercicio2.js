var readline = require('readline');
var rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout
});
meses=["Enero","Febrero","Marzo","Abril","Mayo","Junio","Agosto","Setiembre",
       "Octubre","Noviembre","Diciembre"]
while (true){
    var num = prompt(); 
    if (num>12 || num<1)
        break;
    else
        console.log(meses[num-1]);
}