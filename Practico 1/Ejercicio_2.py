num1 = int(input('Ingrese el primer valor'))
num2 = int(input('Ingrese el segundo valor')) #Pedimos ambos valores
result1 = pow(num1, 2)
result2 = pow(num2, 2)                        #Calculamos el cuadrado de cada uno

if result1 == result2:                        #Alpicamos condicional para mostrar resultados
    print('Los valores son iguales')
else:
    result = result1 / result2
    print('El resultado de la division es: ', result) # Falta evaluacion para verificar cual es el mayor y cual es el menor si num1 > num2 entonces el 
                                                      # resultado esta bien calculado, pero si es al reves el resul deberia ser igual a result2/result1

"""
Dados dos número enteros, se necesita saber el resultado de dividir el cuadrado del
mayor de ellos y el cuadrado del menor de ellos. Si los números son iguales escribir un
mensaje.
"""
