"""
Vector: coleccion de datos del mismo tipo
Van entre corchetes
for x(puede ser cualquier nombre por ej 'index' ya que es el indice) in vector a recorrer
"""
"""
Ciclo FOR
tenemos que saber la condicion de corte
"""

def ciclo_for_frutas():
    frutas = ['manzana', 'pera', 'anana']

    size = len(frutas)  # Con esto evitamos errores dei indice.
                        # Ya que guarda el tamanio total del vector

    for index in range(0, size):       #Recorre el vector de la posicion 0 a 3
        print(frutas[index])

    print(frutas[2])      #acceso al elemento en la posicion indicada


    for index in frutas:     #Por cada item en el vector frutas, recorre
        print(index)


def promedio_con_for():
    acum = 0
                                   #la palabra reservada range sirve para decidir
    for index in range (0, 10):    # cuantas veces recorrera el vector
        nota = int(input(f'Ingrese nota: {index}:    '))
        acum = acum + nota

    prom = acum / 10
    print(f'El promedio general del curso es: {prom}')


"""
Ciclo WHILE
No necesitamos saber de antemano cuantas veces se debe repetir el ciclo
Ya que queda en bucle dependiendo de la condicion que tenga
"""


def ciclo_while():
    temp = 20

    while temp > 0:
        print(f'El agua esta a {temp} grados. Aun no esta congelada')
        temp = temp - 1

    print(f'El agua llego a los {temp} grados, por lo tanto, se congelo')

#ciclo_while()
#promedio_con_for()
#ciclo_for_frutas()

def vector_suma_numeros():

    numeros = [1, 2, 3, 4, 5]

    a = numeros[0]
    b = numeros[1]
    c = numeros[2]
    d = numeros[3]
    e = numeros[4]

    suma = a + b + c + d + e

    print(suma)
    #Ambas retornan el mismo resultado
    size = len(numeros)
    acum = 0

    for i in range(0, size):
        acum = acum + numeros[i]
    print (suma)


def cargar_vector():

    notas = []

    size = int(input("Cuantas notas desea ingresar?: "))

    for index in range(0, size):
        nota = int(input("Ingrese nota: "))
        notas.append(nota)

    print(notas)

