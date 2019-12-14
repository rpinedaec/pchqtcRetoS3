# Lo mismo que el anterior pero ordenando de mayor a menor.

Num=[]
n=int(input("Ingrese un nro: "))

while n!=0:
    Num.append(n)
    n=int(input("Ingrese un nro: "))


print(sorted(Num, reverse=True))