lista=[]
while (true){
    var num=prompt("Ingresa numero: ");
    if (num==0)
        break;
    else
        lista.push(num);
 }
lista.sort(function(a, b){return b-a});
console.log(lista);