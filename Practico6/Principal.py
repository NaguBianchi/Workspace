"""
Realice un programa con dos archivos .py, uno que contenga los métodos y otro que contenga
al menú principal

En el menú se debe crear una lista para ingresar las notas del final de los alumnos de AED I

Las opciones deben permitir realizar las tareas listadas a continuación:
1. Cargar una nota: esta opción debe agregar un nuevo registro en la lista
2. Mostrar el listado de las notas: esta opción debe recorrer la lista y mostrar las notas cargadas
3. Mostrar el listado de los alumnos promocionados: esta opción debe llamar a un método sin retorno
y que reciba como parámetro la lista cargada en el punto anterior y muestre las notas mayores o
iguales a 7 con su respectivo indice.
4. Esta opción debe llamar a un método que reciba como parámetro la lista cargada y muestre el
porcentaje de reprobados (nota menor a 4), regulares (nota igual o mayor a cuatro y menor que 7)
y promocionados (nota mayor a 7)
5. Método sin parámetro y sin retorno que solicite cargar los 3 alumnos con el mejor promedio en un
diccionario de datos, donde la key es el nombre del alumno y el valor de la key su calificación.
Una vez cargado el diccionario imprimir en pantalla todos los items del mismo, ejemplo:
abanderados = {Luis: 10, 'Maria': 9.5, 'Jose':9}


Para salir del sistema se debe agregar la opción “0”.
"""
from Practico6 import Metodos

def menu():
    nombres = []
    notas = []
    size = len(nombres)
    opc = int(input("Ingrese una opcion:\n"
            "1. Para cargar una nota.\n"
            "2. Para mostrar la lista.\n"
            "3. Para mostrar la lista de alumnos promocionados.\n"
            "4. Para mostrar el porcentaje de alumnos reprobados, regulares y promocionados.\n"
            "5. Para cargar en diccionario y mostrarlos.\n"
            "0. Para salir.\n"
            " "))

    while opc != 0:
        if opc == 1:
            nombre = str(input("Ingrese el nombre del alumno: "))
            nota = float(input("Ingrese la nota del alumno: "))
            nombres.append(nombre)
            notas.append(nota)
            size = len(nombres)
        elif opc == 2:
            for i in range (0, size):
                print(f"Nombre: {nombres[i]} - Nota: {notas[i]}")
        elif opc == 3:
            Metodos.opc_3(notas=notas)
        elif opc == 4:
            Metodos.opc_4(notas)
        elif opc == 5:
            Metodos.opc_5()

        else:
            print("Opcion incorrecta.")




        opc = int(input("Ingrese una opcion:\n"
                "1. Para cargar una nota.\n"
                "2. Para mostrar la lista.\n"
                "3. Para mostrar la lista de alumnos promocionados.\n"
                "4. Para mostrar el porcentaje de alumnos reprobados, regulares y promocionados.\n"
                "5. Para cargar en diccionario y mostrarlos.\n"
                "0. Para salir\n"
                " "))
    print("Gracias por utilizar el programa!")

menu()