# Pide números y mételos en una lista, cuando el usuario meta un 0 ya dejaremos de insertar. Por último,
# muestra los números ordenados de menor a mayor.


Num=[]
n=int(input("Ingrese un nro: "))

while n!=0:
    Num.append(n)
    n=int(input("Ingrese un nro: "))
print(sorted(Num))