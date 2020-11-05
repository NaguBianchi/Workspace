from Estructuras.Clase7_Json.usuarios import Usuario
import json



def test_usuario():
    usr = Usuario.generar_usuario()
    print(usr.toJSON())
    print(usr) #En este print imprimio el espacio en memoria donde esta

#test_usuario()

def crear_archivo(nombre_archivo, datos):
    archivo = open(nombre_archivo, "w")  #la w permite escribir, es el modo. la r por ej, permite solo lectura
    #esto crea el archivo si no existe, y si existe lo abre
    archivo.write(str(datos)) #pasamos los datos a string y lo grabamos en el archivo abierto
    archivo.close()


def leer_archivo(nom):
    file = open(nom, "r") #La r es solo lectura y esto nos va a abrir un string
    datos = json.load(file) #esto es para transformar el string en un jason
    #Con el .load lo levantamos como un objeto tipo json
    print(datos)
    return datos


def test_crear_archivo(): #este metodo es para guardar el archivo creado
    filename = "./nuevo_archivo.Json"
    #luego del ./ ponemos el nombre del archivo.
    #El ./ lo guarda en la misma carpeta donde corre el sistema
    usr = Usuario.generar_usuario()
    crear_archivo(nombre_archivo = filename, datos = usr.toJSON())
    leer_archivo(filename)


#test_crear_archivo()


def test_json():
    usr = leer_archivo("./nuevo_archivo.json")
    print(usr)

test_json()


