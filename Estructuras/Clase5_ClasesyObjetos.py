"""
Clases:
Las clases se pueden escribir en un unico .py o pueden agruparse en uno mismo, siempre y cuando
compartan funcionalidades similares

Todos los metodos comienzan con self y representa a la instancia de la clase
se usa para hacer referencia a las variables y metodos de la clase
De esta forma podemos compartir informacion eficiente y facilmente dentro de la  clase

Para crear instancias(objeto) en una clase con parametros especificos
    asignamos valores a los atributos o propiedades
    No es requerido, pero se usa para asignar el estado por defecto a los objetos al crearlos
    Siempre es el primer metodo de la clase

"""

class Persona:

    def __init__(self, nombre, apellido, salud, amistad): #El self de aqui hace referencia a la class
        """
        Inicializamos los atributos que seran usados en los metodos de esta clase y por los objetos
        que fueron creados a partir de ella
        """
        self.nombre = nombre
        self.apellido = apellido         #Estos self son como decir "Esta clase tiene apellido q sera igual
        self.salud = salud               # al valor que me pasen por parametro
        self.amistad = amistad

    def presentarse(self):
        print(f"Hola, mi nombre es {self.nombre} {self.apellido}")

    def estado_salud(self):
        if self.salud == 100:
            print(f"{self.nombre} esta joya")
        elif self.salud >= 76:
            print(f"Hoy, {self.nombre} esta con cansancio")
        elif self.salud >= 51:
            print(f"{self.nombre} debe ir al medico ")
        elif self.salud >= 31:
            print(f"{self.nombre} esta inconsciente ")

