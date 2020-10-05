

def ejercicio_1_cargar_lista():

    alumnos = []

    for index in range(0, 10):
        nombre = str(input(f"Ingrese el nombre del alumno de la posicion: {index + 1} : "))
        alumnos.append(nombre)
    print(alumnos)

    """
    Ejercicio 1:
    Nombre de la función: ejercicio_1_cargar_lista
    Esta función debe:
    Solicitar que se ingresen en una lista los nombres de 10 alumnos. Después de ingresarlos debe imprimir la lista
    """
#ejercicio_1_cargar_lista()


def ejercicio_2_modificar_lista():

    frutas = [' manzana ', ' pera ', ' durazno ']
    verduras = [' acelga ', ' lechuga ']

    newfruit = str(input("Ingrese una nueva fruta: "))
    frutas.insert(2, newfruit)
    print(frutas)

    verduras.extend(frutas)
    print(verduras)

    verduras.remove(newfruit)
    print(verduras)

    frutas.pop(-1)
    print(frutas)

    """
    Nombre de la función: ejercicio_2_modificar_lista
    Dadas las siguientes listas:
    frutas = ['manzana', 'peras', 'durazno']
    verduras = ['acelga', 'lechuga']
    Esta función debe:
    Pedir el ingreso de una nueva fruta  e ingresarlo en la posición nro 2 de la lista de frutas, imprimir la nueva lista de frutas.
    Unir a la lista de verduras todos los items en la lista de frutas, imprimir la lista de verduras
    De la lista de verduras eliminar el item agregado en el inciso ‘a’ e imprimir la lista
    De la lista de frutas eliminar la ultima fruta e imprimir la lista frutas 
    """
#ejercicio_2_modificar_lista()


def ejercicio_3_ordenar_y_buscar_lista():

    frutas = [1998, 1989, 1970, 2020, 1990]
    print(frutas)

    frutas.sort()
    print(frutas)


    year = int(input("Ingrese un anio para comprobar si este se encuentra en la lista: "))
    print(year in frutas)
    #if year in frutas:
    #    print("El anio ingresado se encuentra en la lista")
    #else:
    #    print("El anio ingresado no se encuentra en la lista")

    print(f"Se encuentra en la posicion: {frutas.index(1989)}")

    """
    Nombre de la función: ejercicio_3_ordenar_y_buscar_lista
    Dadas la siguiente lista: frutas = [1998, 1989, 1970, 2020, 1990]
    Esta función debe:
    Imprimir la lista
    Ordenarla de forma ascendente e imprimirla de nuevo
    Pedirle al usuario que ingrese un año y le responda si ese año se encuentra o no en la lista
    En la lista ordenada, consultar en que index se encuentra el numero 1989
    """
#ejercicio_3_ordenar_y_buscar_lista()


def ejercicio_4_diccionarios():
    player = {' comida ': 15, ' energia ': 100, ' enemigos ': 3}
    new_wpn = {'rocas': 4, 'flechas': 5}

    print(player.items())
    print(player.keys())

    player.update(new_wpn)
    print(player)

    player.setdefault(' amigos ', 10)
    print(player.items())

    player [' comida '] = 30
    print(player.items())

    energy = (player.get(' energia '))
    print(f"La cantidad de energia es: {energy}" )

    """
    Nombre de la función: ejercicio_4_dicionarios
    Dado el siguiente diccionario:
    jugador = {'comida': 15, 'energia': 100, 'enemigos':3}
    Imprimir todos los elementos del diccionario con sus respectivas claves
    Imprimir solo las claves
    Al diccionario dado agregarle los items del siguiente diccionario: nuevas_armas = {'rocas': 4, 'flechas': 5}e imprimir de nuevo todos los items
    Al diccionario generado en el inciso anterior agregarle un nuevo elemento amigos = 10, e imprimir todos los elementos
    Actualizar comida a 30 e imprimir el diccionario completo
    Imprimir solo cantidad de energía que tiene disponible el jugador
    """
#ejercicio_4_diccionarios()