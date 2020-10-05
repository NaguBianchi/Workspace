"""
Listas:
Coleccion de datos, tienen diferentes elementos y pueden contener distintos tipos de datos
Incluso pueden contener listas dentro de las listas, diccionarios, tuplas como elementos dentro de las listas
Es autable: Se pueden agregar, remover o cambiar items
Pueden mantener un orden, por lo que se puede acceder a los elemenentos mediante un indice
"""

frutas = ['pera', 'durazno','tomate', 'manzana', 'banana']
numeros = [3, '1998', 2.5, 234, 943]

print(frutas, numeros)

frutas.append('naranja') #append es el metodo para agregar elementos en la lista

print(frutas)

frutas.extend(numeros) #Metodo para combinar listas

print(frutas)

frutas.remove('naranja') #metodo para remover un item

print(frutas)

frutas.pop(0) #Metodo para remover por posicion
frutas.pop(-1) #El -1 se lo utiliza para romover el item que esta al final

print(frutas)

# Para ordenar una lista se utiliza el metodo sort y funciona solo con elementos del mismo tipo

num = [3, 1563, 125.36, 542]
print(num) #aca los muestra tal cual estan ordenados

num.sort() #metodo para ordenarlos
print(num) #Aqui los muestra ya ordenados

#Como saber si un elemento es miembro de una lista

print('manzana' in frutas) #Aqui esta preguntando si manzana esta en la lista frutas(imprime true o false)
print('anana' in frutas)

print(frutas.count('manzana')) #Este metodo sirve para saber cuantos elementos llamados igual hay en la lista

print(frutas.index('durazno')) #muestra la posicion en la lista

frutas.insert(2, 'mandarina') #Esto es para agragar un item en una posicion especifica
print(frutas)

corona = ['negative', 'positive', 'negative', 'negative']
hay_casos = any(c == 'positive' for c in corona)
#Esto se puede traducir como si alguno de todos los elementos(any) son positivos dentro de corona.
# c = Todos los elementos.
print(hay_casos) #si almenos uno de los casos es 'positive', devolvera true

corona = ['negative', 'positive', 'negative', 'negative']
hay_casos1 = all(c == 'positive' for c in corona) #Aca usamos la palabra reservada all para 'Todos'
print(hay_casos1)