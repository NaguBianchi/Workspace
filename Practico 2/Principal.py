import Funciones

def menu():

        print("****************** MENU ********************")
        print("1. Número mayor a 10.")
        print("2. Suma igual o distinta al tercer numero.")
        print("3. Dividir el cuadrado.")
        print("4. Convertidor de grados far en cel.")
        print("--------------------------------------------------")
        num = int(input(">>Ingrese la opción que desea realizar: "))

        if (num == 1):
            funciones.mayor_a_10()

        elif (num == 2):
            n1 = int(input("Ingrese un número: "))
            n2 = int(input("Ingrese otro número: "))
            n3 = int(input("Ingrese un último número: "))
            funciones.suma(a=n1, b=n2, c=n3)

        elif (num == 3):
            n3 = int(input("Ingrese un número: "))
            n4 = int(input("Ingrese otro número: "))
            j = funciones.dividirCuadrado(num1=n3, num2=n4)
            print(f"El resultado es: {j}")
        elif (num == 4):
            l = funciones.celcius()
            print(str(f"{l}°"))



menu()
