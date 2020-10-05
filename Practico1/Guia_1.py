
def ejercicio_1():
    num = int(input('Ingrese un numero:'))
    if num > 10:
        print('El numero es ' + str(num))
    else:
        print('El numero es igual o menor a 10')

    """
    Escribir un algoritmo que lea un número entero y verifique si es mayor a 10. Si lo es
    escribir el número y si no lo es escribir un mensaje que diga que el número es menor o
    igual
    """
#ejercicio_1()


def ejercicio_2():
    num1 = int(input('Ingrese el primer valor'))
    num2 = int(input('Ingrese el segundo valor'))
    result1 = pow(num1, 2)
    result2 = pow(num2, 2)

    if result1 == result2:
        print('Los valores son iguales')
    elif num1 > num2:
        result = result1 / result2
        print('El resultado de la division es: ', result)
    else:
        result = result1 / result2
        print('El resultado de la division es: ', result)
    """
    Dados dos número enteros, se necesita saber el resultado de dividir el cuadrado del
    mayor de ellos y el cuadrado del menor de ellos. Si los números son iguales escribir un
    mensaje.
    """
#ejercicio_2()


def ejercicio_3():
    f = float(input("Ingrese la temperatura en grados Fahrenheit a convertir en Celcius: "))
    c = (5/9) * (f -32)
    print(f"La temperatura en grados Celcius es: {c}")

    """
    Escribir un algoritmo que convierta temperaturas de Fahrenheit a Celcius. Utilizar la
    fórmula ºC = (5/9)·(ºF – 32).
    """
#ejercicio_3()


def ejercicio_4():
    num = float(input("Ingrese un numero: "))
    if num == 0:
        print("El numero ingresado es: 0")
    elif num < 0:
        print(f"El numero ingresado es un numero negativo: {num}")
    else:
        print(f"El numero ingresado es un numero positivo: {num}")

    """
    Determinar si un número ingresado es: negativo, cero o positivo e imprimir, de
    acuerdo a cada caso, el mensaje correspondiente.
    """
#ejercicio_4()


def ejercicio_5():
    num1 = float(input("Ingrese el primer valor: "))
    num2 = float(input("Ingrese el segundo valor: "))
    num3 = float(input("Ingrese el tercer valor: "))
    sum = num1 + num2
    if sum == num3:
        print(f"La suma de los 2 primeros valores da como resultado el 3er valor, es decir: {num3}")
    else:
        print(f"La suma de los 2 primeros valores da como resultado un valor distinto al 3ero, es decir: {sum}")
        print(f"Y el 3er valor era: {num3}")

    """
    Dados 3 números, determinar si la suma del primero y el segundo es igual al tercero.
    Si se cumple, escribir "La suma es igual al tercero";, si no, escribir &quot;La suma es distinta
    al tercero&quot;.
    """
#ejercicio_5()