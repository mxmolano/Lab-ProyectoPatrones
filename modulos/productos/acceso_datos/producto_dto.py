
from datetime import datetime

class ProductoDTO:
    def __init__(self, id=None, nombre="", descripcion="", precio=0.0, fecha=None):
        self.id = id
        self.nombre = nombre
        self.descripcion = descripcion
        self.precio = precio
        self.fecha = fecha or datetime.now()

    def __str__(self):
        return f"ProductoDTO(id={{self.id}}, nombre='{{self.nombre}}', descripcion='{{self.descripcion}}', precio={{self.precio}}, fecha={{self.fecha}})"
