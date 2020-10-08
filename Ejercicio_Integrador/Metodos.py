

def menu_opcion():
    opcion = int(input("Ingrese la opcion deseada: \n"
                       "1. Para cargar una cuenta \n"
                       "2. Para mostrar el listado de cuentas \n"
                       "3. Para mostrar montos superiores a $1000 \n"
                       "4. Para mostrar la suma total de todas las cuentas bancarias \n"
                       "5. Para solicitar el porcentaje de comision \n"
                       "6. Para mostrar los 5 clientes mas importantes \n"
                       "0. Para salir: "))
    return opcion

def mostrar_lista(lista):
    print(lista)


def monto_sup_1000(lista):
    print("Los montos superiores a 1000 son: ")
    mil = lista[0]
    cont = 0
    for index in lista:
        if index > 1000:
            print(index)
            cont = cont + 1
    print(f"Un total de: {cont} Clientes con montos superiores a $1000")


def sum_total(lista):
    acum = 0
    for monto in lista:
        acum = acum + monto
    return acum

def comision(lista):
    comision = int(input("Ingrese el porcentaje de comision: "))
    for item in lista:
        result = (item * comision) / 100
        print(f"El porcentaje de comision de esta cuenta es de: {result}")
#No logre hacerla sin parametros y con retorno


def clientes_importantes():
    nombre = []
    for index in range(0, 5):
        cliente = str(input(f"Ingrese el nombre del cliente numero {index +1} : "))
        nombre.append(cliente)
    print(f"Los clientes mas importantes son: {nombre}")


"""
Realice un programa con dos archivos .py, uno que contenga los métodos y otro que contenga al menú principal
En el menú se debe crear una lista para ingresar el monto total de cada cuenta bancaria.
Las opciones deben permitir realizar las tareas listadas a continuación:
1. Cargar una cuenta: esta opcion debe agregar un nuevo registro en la lista
2. Mostrar el listado de cuentas: esta opción debe llamar a un método sin retorno y que reciba como parámetro la lista
cargada en el punto anterior y muestre los montos de las cuentas ingresadas.
3. Mostrar el listado de cuentas con monto superior a 1000: esta opción debe llamar a un método sin retorno y que reciba
como parámetro la lista cargada en el punto anterior y muestre las cuentas ingresadas con su respectivo índice.
4. Esta opción debe llamar a un método que reciba como parámetro la lista cargada y retorne el resultado de la suma de
todos los montos. En el menú se debe mostrar el resultado recibido.
5. Esta opción debe llamar a un método sin parámetro y con retorno, este método debe solicitar al usuario un porcentaje
de comisión que se aplicará por igual a todas las cuentas y retornarlo al menú. En el menú se debe mostrar cada uno
de los elementos de la lista multiplicado por el porcentaje recibido.
6. Método sin parámetro y sin retorno que solicite cargar en una nueva lista con los nombres de los 5 clientes más
importantes y muestre los nombres ingresados. Para salir del sistema se debe agregar la opción “0”. 
"""