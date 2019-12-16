let texto=prompt("Ingresa el texto: ");
lista_caracteres=[];
for (i=0;i<texto.length;i++){
    lista_caracteres.push(texto[i]);
}
for (i=0;i<texto.length;i++){
    console.log(lista_caracteres[i]," ");
}