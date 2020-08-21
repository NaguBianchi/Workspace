num = int(input('Ingrese un numero: ')) #Pedimos el valor
if num < 0:                             #Iniciamos un condicional anidado para ofrecer 3 posibles resultados
    print('El numero ingresado es un numero negativo:  (', num, ')')
elif num == 0:
    print('El numero ingresado es:  (', num, ')')
else:
    print('El numero ingresado es un numero positivo:  (', num, ')')
 #Imprimimos en pantalla cada resultado dependiendo de su valor

"""
Determinar si un número ingresado es: negativo, cero o positivo e imprimir, de
acuerdo a cada caso, el mensaje correspondiente.
"""