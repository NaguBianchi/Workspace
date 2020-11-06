import json
import uuid
class Transaccion(json.JSONEncoder):

    def __init__(self, dni_cliente, tipo_movimiento, monto_movimiento, estado, nombre_comercio):

        self.transaccion_id = str(uuid.uuid4())
        self.DniCliente = dni_cliente
        self.TipoMovimiento = tipo_movimiento
        self.MontoMovimiento = monto_movimiento
        self.Estado = estado
        self.NombreComercio = nombre_comercio

    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__, sort_keys=True, indent=4)


    def save_trans(self, data):
        file = open(f'./data/{self.transaccion_id}.json', "w")
        file.write(str(data.toJSON))
        file.close()


    def trans_mayor_100000(self):
        if self.MontoMovimiento < 100000:
            print("El movimiento no requiere justificacion.")
        else:
            print("Se debe solicitar documentacion que requiera la justificacion del movimiento.")


