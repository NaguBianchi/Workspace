def mayor_a_10():
    num = int(input("Ingrese un número: "))
    if(num > 10):
       print(num)
    else:
        print(f"El número {num} es menor a diez")



def suma( a=0 , b=0, c=0 ):
    sumar = int(a + b)
    if (sumar == c):
        print(f"La suma de {a} y {b} es igual a {c}")
    else:
        print(f"La suma de {a} y {b} es distinta a {c}")



def dividir_al_cuadrado(num1=1, num2=1):
    mayor = 0
    menor = 0

    if (num1 == num2):
        return str("Los numeros ingresados son iguales")
    elif (num1 >  num2):
        mayor = num1
        menor = num2
    else:
        mayor = num2
        menor = num1

    div = int((mayor * mayor) / (menor * menor))
    return str(f"El resultado es: {div}")

def celcius():
    far = int(input("Ingrese la temperatura en fahrenheit: "))
    cel = int((5/9) * (far - 32))

    return cel