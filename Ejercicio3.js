numero = prompt("Ingrese numero: ");
lista_num=[]
for (i=1;i<11;i++){
    lista_num.push(numero*i);
}
for (i=0;i<10;i++){
    console.log(lista_num[i]);
}