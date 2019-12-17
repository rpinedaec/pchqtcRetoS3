tablademultiplicar = []
numero = input('ingresa un numero aleatorio: ') 

limite = 2
while limite <=11:
    numerolimite = int(numero) * int(limite-1)
    tablademultiplicar.append(numerolimite)
    limite=limite + 1


print(tablademultiplicar)

