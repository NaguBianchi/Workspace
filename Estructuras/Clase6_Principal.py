from Estructuras.Clase6_Busqueda_Json import Empleado, Gestionar_empleados

def opciones_menu():
    print("--------------------------------------------------------------------------\n"
          "Ingrese una opcion\n"
          "1. Para cargar los datos de un empleado.\n"
          "2. Para mostrar la lista de empleados.\n"
          "3. Para buscar un empleado por legajo y mostrar sus datos.\n"
          "4. Para buscar un empleado por nombre y asignarle horas trabajadas.\n"
          "5. Para conocer el porcentaje de empleados con un sueldo menor a $30.000\n"
          "0. Para salir")
    return int(input("Ingrese opcion: "))


def menu():
    gestor_empleados = Gestionar_empleados()
    empleados = []

    opc = opciones_menu()
    while opc != 0:

        if opc == 1:
            nombre = input("Ingrese nombre: ")
            apellido = input("Ingrese apellido: ")
            dni = input("Ingrese DNI: ")
            legajo = int(input("Ingrese legajo: "))
            puesto = input("Ingrese puesto: ")
            salarioxhr = float(input("Ingrese el salario por hora: "))
            empleado = Empleado(nombre=nombre, apellido=apellido, dni=dni, legajo=legajo, puesto=puesto, salarioxhr=salarioxhr)
            empleados.append(empleado)

        elif opc == 2:
            gestor_empleados.imprimir_lista(lista = empleados)

        elif opc == 3:
            gestor_empleados.buscar_empleado_por_legajo(empleados)

        elif opc == 4:
            gestor_empleados.asignar_horas(empleados)

        elif opc == 5:
            gestor_empleados.porcentaje_menor_3mil(empleados)


        opc = opciones_menu()

menu()