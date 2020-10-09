class Alquiler:
    def __init__(self, marca, modelo, fecha, dni, nombre, kmrecorridos, precioxkm = 20, seguro = 100):

        self.marca = marca
        self.modelo = modelo
        self.fecha = fecha
        self.precioxkm = precioxkm
        self.seguro = seguro
        self.dni = dni
        self.nombre = nombre
        self.kmrecorridos = kmrecorridos

    def datos(self):
        print(f"En la fecha: {self.fecha}\n"
              f"El senior {self.nombre}. DNI: {self.dni}\n"
              f"Retiro el vehiculo marca {self.marca}. Mod: {self.modelo}. \n"
              f"Deberia abonar el monto fijo del seguro de ${self.seguro} y el monto fijo de ${self.precioxkm} por cada kilometro. \n")


    def calcular_monto(self):
        if self.kmrecorridos >= 100:
            print(f"Se aniadira un adicional de $200 por exceder los 100km")
            print(f"Por lo que su total aproximado sera de ${(self.precioxkm * self.kmrecorridos) + self.seguro + 200} ")
        elif self.kmrecorridos >= 200:
            print(f"Se aniadira un adicional de $400 por exceder los 200km")
            print(f"Por lo que su total aproximado sera de ${(self.precioxkm * self.kmrecorridos) + self.seguro + 400} ")
        elif self.kmrecorridos >= 400:
            print(f"Se aniadira un adicional de $600 por exceder los 400km")
            print(f"Por lo que su total aproximado sera de ${(self.precioxkm * self.kmrecorridos) + self.seguro + 600} ")
        else:
            print(f"Se estima que el cliente recorrera {self.kmrecorridos}.\n"
            f"Dando una suma total y aproximada de: ${(self.precioxkm * self.kmrecorridos) + self.seguro}.")

