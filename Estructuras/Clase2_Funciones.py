"""
Parametros o Argumentos
Los Parametros son posicionales y requeridos
Para que los parametros no sean obligatorios se define un parametro por default
Ej:def user_info(nombre, edad, ciudad = "Cordoba"):
En pocas palabras, son valores que se reciben en una funcion a traves de los parentesis
"""

# def user_info(nombre, edad, ciudad):
#    print(f"{nombre} tiene {edad} anios y vive en {ciudad}")


# user_info(nombre="Nagu", edad=23, ciudad="Villa Carlos Paz")
# Podemos especificar los parametros con la variable para evitar errores de posicion


"""
Funciones con retorno
Son funciones que retornan un valor para ser usado en otra funcion
"""


def suma():
    a = int(input('Ingrese un numero: '))
    b = int(input('Ingrese otro numero: '))

    sum = a + b
    return sum

# s = suma()
# print('El resultado es : ' + str(s))

# retorno
# No se puede retornar un print de pantalla
# Tampoco se puede retornar mas de 1 vez a no ser que tengas un condicional

def que_temperatura_es():
    return '30 grados'

temp = que_temperatura_es()
print(f'La temperatura es: {temp}')

# Se puede llamar a una funcion dentro de otra funcion y que ambas tengan retorno

# otro ej

def que_temperatura_es_en_celcius(f):
    c = (5 / 9) * (f - 32)
    return c

g = que_temperatura_es_en_celcius(f = 32)
print(g)