"""
Parametros o Argumentos
Los Parametros son posicionales y requeridos
Para que los parametros no sean obligatorios se define un parametro por default
Ej:def user_info(nombre, edad, ciudad = "Cordoba"):
"""

def user_info(nombre, edad, ciudad):
    print(f"{nombre} tiene {edad} anios y vive en {ciudad}")


user_info(nombre="Nagu", edad=23, ciudad="Villa Carlos Paz")
# Podemos especificar los parametros con la variable para evitar errores de posicion
