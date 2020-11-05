from Ejercicio_Integrador import MPrincipal
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
    importantes y muestre los nombres ingresados.
Para salir del sistema se debe agregar la opción “0”.
"""

def banco():
    nombre = []
    cuenta_bancaria = []
    opcion = MPrincipal.menu_opcion()


    while opcion != 0:
        if opcion == 1:
            nombre = str(input("Ingrese el nombre: "))
            monto = float(input("Ingrese el monto de la cuenta bancaria: "))
            cuenta_bancaria.append(nombre)
            cuenta_bancaria.append(monto)
            print(f"La cantidad de: ${monto} a nombre de: {nombre} \n"
                  f"Se ingreso exitosamente!")
        elif opcion == 2:
            print(MPrincipal.mostrar_lista(lista1 = nombre, lista2 = cuenta_bancaria))

        elif opcion == 3:
            MPrincipal.monto_sup_a_mil(lista2 = cuenta_bancaria)

        opcion = MPrincipal.menu_opcion()

banco()