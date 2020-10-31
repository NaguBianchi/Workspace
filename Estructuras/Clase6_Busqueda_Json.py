

class Empleado:

    def __init__(self, nombre, apellido, dni, legajo, puesto, salarioxhr):
    #Aqui construimos como el molde de los objetos que van a estar, sus atributos
        self.nombre = nombre
        self.apellido = apellido
        self.dni = dni
        self.legajo = legajo
        self.puesto = puesto
        self.salarioxhr = salarioxhr
        self.hrstrabajadas = 0
        #A fines academicos podemos poner los datos del empleado y del puesto y demas. pero en realidad
        #el salario y las horas trabajadas estarian en otra clase

    #def __int__(self):
    #    self.nombre = ""
    #    self.apellido = ""
    #    self.dni = ""
    #    self.legajo = 0
    #    self.puesto = ""
    #    self.salarioxhr = 0
    #    self.hrstrabajadas = 0
        #La dif de este y el de arriba, es que el otro recibe datos de afuera y este tiene valores por defecto
        #Y con el metodo de cargar puedo ir asignando valores

    def mostrar_datos(self):
        print("------------------------------------------------------")
        print(f'Nombre: {self.nombre}')
        print(f'Apellido: {self.apellido}')
        print(f'DNI: {self.dni}')
        print(f'Legajo: {self.legajo}')
        print(f'Puesto: {self.puesto}')
        print(f'Salario por hora: {self.salarioxhr}')
        print(f'Horas trabajadas: {self.hrstrabajadas}')
        print(f'Sueldo calculado: {self.salarioxhr * self.hrstrabajadas}')

    def cantidad_de_horas(self, cantidad_hs):
        self.hrstrabajadas = cantidad_hs

    def calcular_sueldo(self):
        return self.hrstrabajadas * self.salarioxhr


class Gestionar_empleados:

    def imprimir_lista(self, lista):
        for item in lista:
            item.mostrar_datos()


    def buscar_empleado_por_legajo(self, lista):
        legajo = int(input("Ingrese legajo a buscar: "))
        bandera = False
        for item in lista:
            item: Empleado #item: tipo empleado osea ese item es igual a la clase empleado
            if legajo == item.legajo:
                print("------------------------------------------------------")
                print("Empleado encontrado: ")
                item.mostrar_datos()
                print("------------------------------------------------------")
                bandera = True
                break #Esto sirve para salir de la estructura, cuando encuentre el legajo
                      # no hay necesidad de que siga recorriendo
        if bandera == False:
            print("------------------------------------------------------")
            print("Empleado no encontrado")
            print("------------------------------------------------------")
    #Una bandera es un valor booleano y sirve en estos casos para esot


    def asignar_horas(self, lista):
        nombre = input("Ingrese el nombre del empleado al que le quiere ingresar horas: ")
        flag = False
        for item in lista:
            item: Empleado
            if nombre == item.nombre:
                cant_hs = int(input(f"Ingrese la cantidad de horas que trabajo {item.nombre}: "))
                item.cantidad_de_horas(cant_hs)
                flag = True
                break

        if flag == False:
             print("------------------------------------------------------")
             print("El empleado no existe")
             print("------------------------------------------------------")


    def porcentaje_menor_3mil(self, lista):
        count = 0
        tamanio = len(lista)
        for item in lista:
            item:Empleado
            sueldo = item.calcular_sueldo()
            if sueldo < 30000:
                count = count +1

        print(f"El porcentaje de empleados con sueldo menor a $30.000 es de %{count / tamanio * 100}")


"""
    def cargar_empleado(self):
        self.nombre = input("Ingrese nombre: ")
        self.apellido = input("Ingrese apellido: ")
        self.dni = input("Ingrese DNI: ")
        self.legajo = int(input("Ingrese legajo: "))
        self.puesto = input("Ingrese puesto: ")
        self.salarioxhr = float(input("Ingrese el salario por hora: "))
        self.hrstrabajadas = 0
        # A fines academicos podemos podemos hacerlo de esta forma pero en la vida real no se utiliza
        # Ya q los datos a cargar se piden desde otro lugar y nunca desde el mismo constructor
"""