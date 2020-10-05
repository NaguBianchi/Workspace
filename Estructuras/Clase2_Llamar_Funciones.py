import Estructuras.Clase2_Funciones
# tambien se puede hacer asi: from Estructuras import funciones


"""
Hacer una funcion que solicite dos numeros, los sume y muestre
el resultado multiplicado por 2
"""
def suma_x_2():
    s = Estructuras.Clase2_Funciones.suma()
    sum2 = s * 2
    print(f'La suma multiplicada por 2 es: {sum2}')
    # print(f'La suma multiplicada por 2 es: {Estructuras.funciones.suma() * 2}') #Para hacerlo en una sola linea de code


suma_x_2()
