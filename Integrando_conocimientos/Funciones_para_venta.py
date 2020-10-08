"""
Agregar el monto de una venta.
Mostrar todos los datos en la lista.
Mostrar la venta más baja.
Mostrar la ganancia total (Suma de todas las ventas).
Calcular el promedio de Ventas.
"""

def imprimir_lista(lista):
    for item in lista:
        print(item)
    print("El listado de ventas es: ")
    i = 1
    for venta in lista:
        print(f"Venta Numero {i}: {venta}")
        i = i + 1
    for i in range(0, len(lista)):
        print(f"Venta numero {i + 1}: {lista[i]}")

    #2 formas de imprimir la lista

def opcion_venta():
    opcion = int(input("Ingrese: \n"
                       "1. Para cargar una venta\n"
                       "2. Para mostrar la lista de ventas\n"
                       "3. Para mostrar la venta mas baja\n"
                       "4. Para mostrar la ganancia total\n"
                       "5. Para calcular el promedio de ventas\n"
                       "0. Para salir\n"
                       "Ingrese la opcion: "))
    return opcion


def venta_total(lista):
    acum = 0
    for item in lista:
        acum = acum + item
    return acum
    # return sum(lista) #Este metodo retorna la suma de todas las ventas
def venta_minima(lista):
    min = lista [0]
    for item in lista:
        if item < min:
            min = item
    return min
    # return min(lista) #Metodo que retorna el minimo de la lista


def promedio_ventas(lista):
    """
    totalventas = 0
    cantventas = 0
    for item in lista:
        totalventas = totalventas + item
        cantventas = cantventas + 1
    prom = totalventas / cantventas
    # return prom
    """
    return venta_total(lista) / len(lista)

