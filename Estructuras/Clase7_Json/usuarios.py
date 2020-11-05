import json
import uuid
class Usuario(json.JSONEncoder):


    def __init__(self, user_id, nombre, estado, dni, apellido):
        self.UserId = user_id
        self.Nombre = nombre
        self.Estado = estado
        self.Dni = dni
        self.Apellido = apellido

    @classmethod                 #Genera el usuario sin crear la clase o sin usar la clase, sino, necesitamos los parametros al llamarlo
    def generar_usuario(self):
        user_id = str(uuid.uuid4())   #Esto genera un valor aleatorio como id
        nombre = input("Ingrese el nombre: ")
        apellido = input("Ingrese el apellido: ")
        dni = input("Ingrese el DNI: ")
        estado = input("Ingrese el estado: ")
        usuario = Usuario(user_id = user_id, nombre = nombre, apellido = apellido, dni = dni, estado = estado)
        return usuario

        #Estamos generando un objeto del tipo usuario

    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__, sort_keys = True, indent=4)

        #Esto hace q se transforme en un obj. tipo json

