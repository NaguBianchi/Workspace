import json
class User(json.JSONEncoder):

    def __init__(self, nombre, apellido, edad, email, dni):
        self.Nombre = nombre
        self.Apellido = apellido
        self.Edad = edad
        self.Email = email
        self.Dni = dni
    @classmethod
    def user_generator(self):
        nombre = input("Ingrese el nombre: ")
        apellido = input("Ingrese el apellido: ")
        edad = input("Ingrese la edad: ")
        dni = input("Ingrese el DNI: ")
        email = input("Ingrese el E-mail: ")
        usr = User(nombre=nombre, apellido=apellido, edad=edad, dni=dni, email=email)
        return usr

    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__, sort_keys = True, indent=4)

    def save_user(self, user):
        file = open(f'./data/{self.Dni}.json', "w")
        file.write(str(user.toJSON()))
        file.close()

    def modify(self, file):
        with open(f'{file}', 'r') as f:
            json_data = json.load(f)
            json_data['nombre'] = "jose"

        with open(f'{file}', 'w') as f:
            f.write(json.dumps(json_data))


