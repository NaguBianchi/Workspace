# comentario simple, osea en una sola linea

"""
Este es un comentario multilinea
Normalmente se utilizan para los docstrings
o mofigicar indicaciones o codigo complejo
"""

#print ("Hello world") #para mostrar mensajes en pantalla

#input("Ingrese un numero: ") pero lo reconoce como caracteres

#Convencion de nombres
car = 10
CAR = 20
_car = 30

"""
Variables numericas:
int -> numeros enteros
float -> numeros decimales
"""

"""
str -> Variables string o de texto
"""
texto = 'Esta es una variable tipo string'
texto_uno = '10'
"""
Bool -> boolean (True or False)
"""

#suma = car + CAR
suma = texto_uno + str(car)
print (suma)

nombre = input ('Ingrese el nombre del alumno: ')
num1 = int(input('Ingrese primer numero'))
num2 = int(input('Ingrese segundo numero'))

sum = num1 + num2
print  ('El resultado de la suma es: ' + str(sum)) #la mas comun
print ('El resultado de la suma es: {}'.format(sum))
print (f'El resultado de la suma es: {sum}') #la forma mas comoda

#Creacion de una funcion
def calcular_nota():
    nombre = input('Ingrese el nombre del alumno: ')
    num1 = float(input('Ingrese la primera nota: '))
    num2 = float(input('Ingrese la segunda nota: '))

    prom = (num1 + num2) / 2
    print("El promedio de " + nombre + " es: " + str(prom))

    if prom >= 7: #Se puede usar if solo
        print('El alumno esta promocionado')
    elif prom >= 4: #Se puede agregar mas elif
        print('El alumno esta aprobado')
    else:
        print ('El alumno esta libre')

calcular_nota()
