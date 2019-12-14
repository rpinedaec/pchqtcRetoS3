
def ejercicio1():
    unoAlCien = []

    for i in range(100):
        unoAlCien.append(i+1)

    print(unoAlCien)

def convertirNumAMeses():
    meses = ['enero','febrero','marzo','abril','mayo','junio','julio','agosto','septiembre','octubre','noviembre','diciembre']
    mesInput = int(input("Ingrese un numero del 1 al 12 para ver que mes es: "))
    print(meses[mesInput-1])

def tablaDeMultip():
    base = int(input("Ingresa un numero para devolver su tabla de multiplicar: "))
    tablaDeMultiplicar = []

    for i in range(10):
        tablaDeMultiplicar.append(base*(i+1))

    print(tablaDeMultiplicar)

def enlistarNumOrdenados():
    numeros = []

    while True:
        numero = int(input("Ingresa un numero para enlistarlo, ingresa 0 para terminar: "))
        if(numero==0):
            break
        else:
            numeros.append(numero)

    numeros.sort()
    print(numeros)
    numeros.sort(reverse=True)
    print(numeros)

def sinEspacios():

    cadena = input("Ingrese una cadena de texto para eliminar los espacios: ")
    cadenaSinEspacios = []

    for i in range(len(cadena)):
        if(cadena[i]==' '):
            continue
        else:
            cadenaSinEspacios.append(cadena[i])

    print(cadenaSinEspacios)
    
def repetidos():
    cadena = input("Ingrese una cadena de texto para eliminar las repeticiones: ")
    cadenaSinRepetidos = []

    for i in range(len(cadena)):
        bandera = 1
        for j in range(len(cadenaSinRepetidos)):
            if(cadena[i]==cadenaSinRepetidos[j]):
                bandera = 0
                break
        if(bandera==1):
            cadenaSinRepetidos.append(cadena[i])

    print(cadenaSinRepetidos)

def listaRepetidasMaxMin():
    numeros = [1,2,3,4,5,6,1,3,5,1,6,2,2,1,5]
    numero = int(input("Ingresa un numero para saber cuantas veces se repiten: "))
    cantRepetidas = 0
    for i in range(len(numeros)):
        if(numeros[i]==numero):
            cantRepetidas += 1
    print(numeros)
    print("La cantidad de repetidas son:", cantRepetidas)
    print("El maximo valor es",max(numeros),". El minimo valor es",min(numeros))

def diccionarioContactos():
    contactos = {}
    while True:
        usuario = input("Ingrese nombre de usuario: ")
        telefono = input("Ingrese numero de telefono: ")
        contactos[usuario] = telefono
        continuar = input("Ingresar otro contacto? s/n: ")
        if(continuar == "n"):
            break
    print(contactos)

diccionarioContactos()

# ejercicio= input("Ingrese el ejercicio que quiere ejecutar:\n1:Imprimir del uno al cien, \n2: Convertir numeros a meses, \n3: Tabla de Multiplicar \n4: Enlistar numeros ordenados \n5: Eliminar espacios\n6: Eliminar repetidas\n0: Actual")
