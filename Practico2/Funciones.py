def caso_1():
    num = int(input('Escribe un numero: '))
    if num > 10:
        print(num)
    else:
        print('El numero es menor o igual a 10')

def caso_2(num1, num2, num3):
    #num1 = int(input('Ingrese un numero: '))
    #num2 = int(input('Ingrese otro numero: '))
    #num3 = int(input('Ingrese otro numero: '))
    suma = num1 + num2
    if suma == num3:
        print(f'La suma de los 2 primeros numeros da como resultado el 3er numero: {num3}')
    else:
        print(f'La suma de los 2 primeros numeros es distinta al 3ero: {num3}')
        print(f'El resultado de la suma fue: {suma}')

def caso_3(num1, num2):
    #num1 = int(input('Ingrese un numero: '))
    #num2 = int(input('Ingrese otro numero: '))
    if num1 == num2:
        r = num1 / num2
        return r
    elif num1 > num2:
        result = (num1 * num1) / (num2 * num2)
        return result
    else:
        result = (num1 * num1) /(num2 * num2)
        return result

def caso_4():
    temp = float(input('Ingrese la temperatura en Fahrenheit a convertir a Celcius: '))
    celc = (5 / 9) * (temp - 32)
    return celc


