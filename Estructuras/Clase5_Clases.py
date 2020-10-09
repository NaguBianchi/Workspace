from Estructuras.Clase5_ClasesyObjetos import Persona


maria = Persona(nombre = 'Maria', apellido = 'Gonzalez', salud = 95, amistad = True)
martin = Persona('Martin', 'Paez', 88, False)
leo = Persona('Leo', 'Williams', 72, True)
nagu = Persona('Nagu', 'Bianchi', 31, True)

maria.presentarse()
martin.presentarse()
leo.presentarse()
nagu.presentarse()

nombre = input("Ingrese el nombre: ")
apellido = input("Ingrese el apellido: ")
salud = int(input("Ingrese el porcentaje de salud: "))
amistad = bool(input("Ingrese el estado de amistad"))

per = Persona(nombre, apellido, salud, amistad)

print(f"Como esta {maria.nombre} hoy?")
maria.estado_salud()

personas = []
personas.append(maria)
personas.append(martin)
personas.append(leo)
personas.append(nagu)
personas.append(per)
#La p en el for es cada persona. Por cada persona q va pasando, realizara las operaciones
for p in personas:
    p.presentarse()
    print(f"Como esta {p.nombre} hoy?")
    p.estado_salud()
    print(f"{p.nombre} es amig@ mio?")
    print(p.amistad)
