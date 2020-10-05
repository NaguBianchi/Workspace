from Practico2 import Funciones

def menu():

    print("****************************** MENU ******************************")
    print("1. Numero mayor, menor o igual a 10.")
    print("2. Suma igual o distinta al tercer numero.")
    print("3. Dividir el cuadrado de 2 numeros segun cual sea el mayor.")
    print("4. Convertidor de grados Far a grados Celc.")
    print("-------------------------------------------------------------------")
    num = int(input("Ingrese la opcion que desea realizar:"))

    if num == 1:
        Funciones.caso_1()

    elif num == 2:
        n1 = int(input('Ingrese un numero: '))
        n2 = int(input('Ingrese otro numero: '))
        n3 = int(input('Ingrese otro numero: '))
        Funciones.caso_2(num1 = n1, num2 = n2, num3 = n3)


    elif num == 3:
        val1 = int(input('Ingrese un numero: '))
        val2 = int(input('Ingrese otro numero: '))
        re = Funciones.caso_3(num1 = val1, num2 = val2)
        return print(f"El resultado de la division es: {re}")
    elif num == 4:
        r = Funciones.caso_4()
        return print(f"El resultado de la conversion es: {r}")
    else:
        print("La opcion ingresada no es valida")


menu()