import json

def cargar_datos(ruta):
    try:
        with open(ruta, 'r') as archivo:
            return json.load(archivo)
    except FileNotFoundError:
        return []

def guardar_datos(ruta, datos):
    with open(ruta, 'w') as archivo:
        json.dump(datos, archivo, indent=4)


