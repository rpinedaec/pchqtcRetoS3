from random import randrange

def enlistarDeUnoAlCien():
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

    numeros = []

    for i in range(10):
        numeros.append(randrange(10))

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

def main():

    def convNumerosAFunc(argument):
        opciones = {
            1 : enlistarDeUnoAlCien,
            2 : convertirNumAMeses,
            3 : tablaDeMultip,
            4 : enlistarNumOrdenados,
            5 : sinEspacios,
            6 : repetidos,
            7 : listaRepetidasMaxMin,
            8 : diccionarioContactos
        }

        func = opciones.get(argument, lambda: "Opcion invalida")
        func()

    def ejecutaMenuRegresar():
        leyenda = [
            "1. Regresar al menu principal",
            "2. Cerrar"
        ]

        print("\n MENU REGRESAR")

        for i in range(len(leyenda)):
            print(leyenda[i])

        opcion = int(input("Opcion: "))

        if(opcion==1):
            ejecutaMenuPrinc()
        else:
            exit()

    def ejecutaMenuPrinc():
        leyenda = [
            "1. Enlistar del 1 al 100",
            "2. Convertir Numero a Meses",
            "3. Calcular la Tabla de Multiplicar",
            "4. Enlistar Numeros Ordenados",
            "5. Eliminar Espacios en Blanco",
            "6. Eliminar Caracteres Repetidos",
            "7. Ver Repetidas, Numero Maximo y Minimo de una Lista Aleatoria",
            "8. Ingresar Contactos al Diccionario"
        ]

        print("\n MENU PRINCIPAL \n Ingrese el numero de la funcion a ejecutar: ")

        for i in range(len(leyenda)):
            print(leyenda[i])

        opcion = int(input("Opcion: "))
        print("\n")
        convNumerosAFunc(opcion)
        ejecutaMenuRegresar()
        
    ejecutaMenuPrinc()

main()
