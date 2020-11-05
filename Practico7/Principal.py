from Practico7.Metodos import Persona
import json
def test_creacion_archivo():
    maria= Persona(nombre="Maria", apellido= "Lopez", dni="45990339", email= "maria.lopez@iresm.edu.ar", edad=20)
    alejandro= Persona(nombre="Alejandro", apellido="Perez", dni="30949303", email="alejandro.perez@iresm.edu.ar", edad=31)
    maria.save_person_file(maria)
    alejandro.save_person_file(alejandro)

test_creacion_archivo()

def test_edad_persona():
    natalia = Persona(nombre="Natalia", apellido="Lopez", dni="30990339", email="natalia.lopez@iresm.edu.ar", edad=25)
    natalia.save_person_file(natalia)
    natalia.adult_condition()

test_edad_persona()


def test_json_persona():
    marcos = Persona(nombre="Marcos", apellido="Gonzalez", dni="30990339", email="marcos.gonzalez@iresm.edu.ar", edad= 25)
    to_dict = json.loads(marcos.toJSON())

    print(f"\n Las keys del diccionario son: {to_dict.keys()}\n")
    print(f"\n Los values del diccionario son: {to_dict.values()}\n")
    print(f"\n Los items del diccionario son: {dict(to_dict.items())}\n")
    print(f" \n El valor de la key nombre es: "), to_dict.get('nombre')

    for keys, values in to_dict.items():
        print(keys, ":", values)

test_json_persona()