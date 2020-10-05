
def ejercicio_1_for_en_vector():
    nombre = ['Lucas', 'Franco','Luciano', 'Malena', 'Jonatan', 'Luciano', 'Rodrigo', 'MariaSol', 'Enzo', 'Milena']

    for index in nombre:
        print(index)

def ejercicio_2_for_en_vector():
     nombre = ['Lucas', 'Franco','Luciano', 'Malena', 'Jonatan', 'Luciano', 'Rodrigo', 'MariaSol', 'Enzo', 'Milena']
     size = len(nombre)
     for index in range(0, size):
        print(f"En la posicion: {index} se encuentra el nombre de {nombre[index]}")

def ejercicio_3_for_en_vector():
    nombre = ['Lucas', 'Franco', 'Luciano', 'Malena', 'Jonatan', 'Luciano', 'Rodrigo', 'MariaSol', 'Enzo', 'Milena']
    size = len(nombre)
    for index in range(4, size):
        print(f"el nombre en la posicion: {index}, es: {nombre[index]}")
    print('-------------------------------------')
    print(f'El elemento en la posicion 1 es: {nombre[1]}')

def ejercicio_4_while():
    count = 0
    acum = 0
    nota = float(input("Ingrese una nota: "))
    while nota != 0:
        acum = acum + nota
        count = count + 1
        print('Ingrese 0 para finalizar')
        nota = float(input("Ingrese una nota: "))


    if count == 0:
        print("No fue ingresada ninguna nota")

    else:
        prom = acum / count
        print(f"El promedio de las notas es: {prom}")

