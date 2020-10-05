"""
Diccionarios:
    El contenido esta formado por una key y su valor que es clave valor ej: key=apellido valor=bianchi
    son mutables osea se pueden modificar
    Pueden mantener un orden de entrada(como se fueron creando)
    Su sintaxis es entre llaves que contienen una key y son separados por coma
"""

anios = {'Laila': 1974, 'Matias': 1997}

cosas = {'comida': 15, 'energia': 100, 'enemigos': 3}

e = cosas.get('energia') #Metodo que retorna el valor de una key
                         #Si la key no existe, retornara 'none' a no ser que seguido de una coma escribamos algo
print(e)                 #Ej cosas.get('clase', 'No existe')

print(cosas.items()) #Imprime todos los elementos del diccionario

print(cosas.keys()) #Imprime todas las keys

cosas.popitem() #Te remueve el ultimo objeto que esta dentro del diccionario
print(cosas.items())

new_items = {'rocas': 4, 'flechas':  5}

cosas.update(new_items) #Actualiza las keys con el valor nuevo que proporcionemos
print(cosas.items())

up_new = {'comida': 3, 'redes': 2}

cosas.update(up_new) #Tambien puede agergar mas keys
print(cosas.items())

cosas.setdefault('red', 100) #Este unicamente sirve para agregar keys y valores
print(cosas.items())

cosas['comida'] = 100 #Actualiza el valor de una key, funciona igual que el setdefault
print(cosas)

comida = cosas['comida']
print(f'La cantidad de comida es: {comida}')

comida1 = cosas.get('comida')
print(f'La cantidad de comida es: {comida1}')
