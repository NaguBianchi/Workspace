from Parcial.Clase import Transaccion
import json

def test_creacion_archivo():
    transaccion_a = Transaccion(dni_cliente= "45990339", tipo_movimiento= "CONSUMO", monto_movimiento=2000, estado= "RECHAZADO", nombre_comercio= "MUSIMUNDO")
    transaccion_b = Transaccion(dni_cliente= "45990339", tipo_movimiento= "CONSUMO", monto_movimiento=2000, estado= "APROBADO", nombre_comercio= "MUSIMUNDO")
    transaccion_c = Transaccion(dni_cliente= "30949303", tipo_movimiento= "CASH_IN", monto_movimiento=50000, estado= "APROBADO", nombre_comercio= "PAGOFACIL")
    transaccion_a.save_trans(transaccion_a)
    transaccion_b.save_trans(transaccion_b)
    transaccion_c.save_trans(transaccion_c)

test_creacion_archivo()

def test_monto_movimiento():
    transaccion_a = Transaccion(dni_cliente= "45990339", tipo_movimiento= "CONSUMO", monto_movimiento= 200000, estado= "APROBADO", nombre_comercio= "DISCO")
    transaccion_a.save_trans(transaccion_a)
    transaccion_a.trans_mayor_100000()

test_monto_movimiento()

def test_json_movimiento():
    transaccion_a = Transaccion(dni_cliente= "30949303", tipo_movimiento= "CASH_IN", monto_movimiento= 500, estado= "APROBADO", nombre_comercio= "PAGOFACIL")
    to_dict = json.loads(transaccion_a.toJSON())

    print(f"\n Las keys del diccionario son: {to_dict.keys()}\n"
          f"Los values del diccionario son: {to_dict.values()}\n"
          f"Los items del diccionario son: {dict(to_dict.items())}\n"
          f"El valor de la key de tipo de movimiento es: "), to_dict.get('tipo_movimiento')

    for keys, values in to_dict.items():
        print(keys, ":", values)

test_json_movimiento()
