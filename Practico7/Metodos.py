import json
import uuid
class Persona(json.JSONEncoder):

    def __init__(self, nombre, apellido, dni, email, edad):

        self.UserId = str(uuid.uuid4())
        self.Nombre = nombre
        self.Apellido = apellido
        self.Dni = dni
        self.Email = email
        self.Edad = edad

    @classmethod
    def crear_persona(self):
        nombre = input("Ingrese el nombre: ")
        apellido = input("Ingrese el apellido: ")
        edad = input("Ingrese la edad: ")
        dni = input("Ingrese el DNI: ")
        email = input("Ingrese el E-mail: ")
        persona = Persona(nombre=nombre, apellido=apellido, edad=edad, dni=dni, email=email)
        return persona

    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__, sort_keys = True, indent=4)


    def save_person_file(self, person):
        file = open(f'./data/{self.UserId}.json', "w")
        file.write(str(person.toJSON()))
        file.close()


    def adult_condition(self):
        if self.Edad >= 21:
            print(f"\n {self.Nombre} tiene {self.Edad} anios, por lo que es mayor de edad.")
        else:
            print(f"\n {self.Nombre} Tiene {self.Edad} anios, por lo que es menor de edad")