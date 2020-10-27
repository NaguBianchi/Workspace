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

def opc_3(notas):
    count = 0
    for item in notas:

        if item > 6:
            count = count + 1
            print(f"El alumno Num.{count}. Promociono con {item}.")

    print(f"La cantidad de alumnos promocionados es de: {count}")


def opc_4(notas):
    count = 0
    count1 = 0
    count2 = 0
    count3 = 0
    for item in notas:
        count = count + 1
        if item < 4:
            count1 = count1 + 1
        elif item >= 4 and item < 7:
            count2 = count2 + 1
        elif item >=7:
           count3 = count3 + 1

    print(f"La cantidad de alumnos reprobados es de: {count1}. Siendo el {(count1 / count) * 100}% del total de alumnos.")
    print(f"La cantidad de alumnos regulares es de: {count2}. Siendo el {(count2 / count) * 100}% del total de alumnos.")
    print(f"La cantidad de alumnos promocionados es de: {count3}. Siendo el {(count3 / count) * 100}% del total de alumnos.")


def opc_5():
    bestalumns = {}
    for i in range(1, 4):
        bestalumn = input(f"Ingrese el nombre del alumno Num. {i}: ")
        notabestalumn = float(input(f"Ingrese la calificación del alumno Num. {i}: "))
        bestalumns[bestalumn] = notabestalumn
    print(f"Los tres mejores estudiantes y sus calificaciones son: {bestalumns}")
