from Practico5.Clase import Alquiler

def menu():
    alquileres = []
    opc = int(input("Ingrese la opcion deseada: \n"
                    "1. Para cargar un nuevo alquiler. \n"
                    "2. Mostrar la lista de alquileres. \n"
                    "3. Para ver datos especificos. \n"
                    "0. Finalizar: \n"
                    ""))
    while opc != 0:
        if opc == 1:
            marca = input("Ingrese la marca: ")
            modelo = input("Ingrese el modelo: ")
            fecha = input("Ingrese la fecha: ")
            dni = input("Ingrese el DNI: ")
            nombre = input("Ingrese el nombre: ")
            kmrecorridos = int(input("Ingrese los kilometros que se estiman recorrer: "))

            alq = Alquiler(marca, modelo, fecha, dni, nombre, kmrecorridos, precioxkm=20, seguro=100)

            alquileres.append(alq)

        elif opc == 2:
            for a in alquileres:
                print(f"Fecha: {a.fecha}, Nombre: {a.nombre}, DNI: {a.dni}, Marca: {a.marca}, Modelo: {a.modelo}, Kms Recorridos: {a.kmrecorridos}, Precio por Km: ${a.precioxkm}, Seguro: ${a.seguro}" )
                #No me salio como mostrar la lista de otra forma
        elif opc == 3:
           for a in alquileres:
               print("Los datos son: ")
               a.datos()
               a.calcular_monto()
        else:
            print("Opcion incorrecta!")

        opc = int(input("Ingrese la opcion deseada: \n"
                        "1. Para cargar un nuevo alquiler \n"
                        "2. Mostrar la lista de alquileres \n"
                        "3. Para ver datos especificos. \n"
                        "0. Finalizar: \n"
                        ""))

    print("Gracias por utilizar el programa!")

menu()
"""
for a in alquileres:
print(f"En la fecha: {a.fecha}\n"
f"El senior {a.nombre}. DNI: {a.dni}\n"
f"Retiro el vehiculo marca {a.marca}. Mod: {a.modelo}. \n"
f"Deberia abonar el monto fijo del seguro de {a.seguro} y el monto fijo de {a.precioxkm} por cada kilometro. \n"
f"Se estima que el cliente recorrera {a.kmrecorridos}.\n"
f"Dando una suma total y aproximada de: {(a.precioxkm * a.kmrecorridos) + a.seguro}.")
#Para hacerlo sin funcion e objeto
"""