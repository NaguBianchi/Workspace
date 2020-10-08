"""
Una librería de la ciudad de Carlos Paz requiere de un programa que permita
cargar los montos de todas las ventas realizadas en el mes. Para ello el programa
debe permitir guardar ese valor en una lista.
Se debe generar un menú que permita realizar las siguientes operaciones:

Agregar el monto de una venta.
Mostrar todos los datos en la lista.
Mostrar la venta más baja.
Mostrar la ganancia total (Suma de todas las ventas).
Calcular el promedio de Ventas.

Cada opción debe llamar a una función que se encargue de hacer
el calculo correspondiente recibiendo la lista por parametro
y retornando el valor correspondiente.
"""
from Integrando_conocimientos import Funciones_para_venta
def menu():
    lista_ventas = []
    opcion = Funciones_para_venta.opcion_venta()


    while opcion != 0:
        if opcion == 1:
            venta = float(input("Ingrese el monto de la venta: "))
            lista_ventas.append(venta)
        elif opcion == 2:
            Funciones_para_venta.imprimir_lista(lista = lista_ventas)
            # print(lista_ventas) #Metodo sin funcion
        elif opcion ==3:
            r = Funciones_para_venta.venta_minima(lista = lista_ventas)
            print(f"La venta minima es: {r}")
            # print(f"La menor venta es: {min(lista_ventas)}") #Metodo sin funcion
        elif opcion == 4:
            r = Funciones_para_venta.venta_total(lista = lista_ventas)
            print(f"El monto de las ventas totales es: {r}")
            # print(f"El monto de las ventas totales es: {sum(lista_ventas)}") #Metodo sin funcion
        elif opcion == 5:
            r = Funciones_para_venta.promedio_ventas(lista = lista_ventas)
            print(f"El promedio de las ventas es: {r}")
        else:
            print("Opcion incorrecta!")

        opcion = Funciones_para_venta.opcion_venta()

menu()
