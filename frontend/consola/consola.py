import requests
import json

# Cargar configuración desde config.json
with open("modulos/productos/configuracion/config.json") as f:
    config = json.load(f)

API = config["api_base"]
ENDPOINTS = config["endpoints"]

def menu():
    print("\n===== Menú Principal =====")
    print("1. Ingresar nuevo producto")
    print("2. Listar productos")
    print("3. Obtener producto por ID")
    print("4. Actualizar producto")
    print("5. Eliminar producto")
    print("6. Salir")

def ingresar():
    id = input("ID del Producto: ")
    nombre = input("Nombre: ")
    descripcion = input("Descripción: ")
    precio = input("Precio: ")
    fecha = input("Fecha: ")
    r = requests.post(f"{API}{ENDPOINTS['create']}", json={
        "id": id,
        "nombre": nombre,
        "descripcion": descripcion,
        "precio": float(precio),
        "fecha": fecha
    })
    print(r.json())

def listar():
    r = requests.get(f"{API}{ENDPOINTS['read_all']}")
    for c in r.json():
        print(c)

def obtener():
    id = input("ID del Producto: ")
    url = ENDPOINTS["read_one"].replace("{id}", id)
    r = requests.get(f"{API}{url}")
    print(r.json() if r.status_code == 200 else "Producto no encontrado.")

def actualizar():
    id = input("ID a actualizar: ")
    texto = input("Nuevo texto: ")
    email = input("Nuevo email: ")
    calificacion = input("Nueva calificación: ")
    url = ENDPOINTS["update"].replace("{id}", id)
    r = requests.put(f"{API}{url}", json={
        id: id,
        "nombre": input("Nuevo nombre: "),
        "descripcion": input("Nueva descripción: "),
        "precio": float(input("Nuevo precio: ")),
        "fecha": input("Nueva fecha: "),
    })
    print(r.json())

def eliminar():
    id = input("ID a eliminar: ")
    url = ENDPOINTS["delete"].replace("{id}", id)
    r = requests.delete(f"{API}{url}")
    print(r.json())

if __name__ == "__main__":
    while True:
        menu()
        opcion = input("Seleccione una opción: ")
        if opcion == "1": ingresar()
        elif opcion == "2": listar()
        elif opcion == "3": obtener()
        elif opcion == "4": actualizar()
        elif opcion == "5": eliminar()
        elif opcion == "6": break
        else: print("Opción inválida.")
