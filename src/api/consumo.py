# Rutina para consumir APIs en python
import requests

url_base = "http://localhost:8080/api"


def consumir_categorias_backen():
    url = url_base + "/categorias"
    try:
        respuesta = requests.get(url, timeout=10)
        respuesta.raise_for_status()
        datos = respuesta.json()
        print("Categorias:")
        print(datos)
        print("******************************************************************")
    except Exception as e:
        print("Error consumiendo categorias:", e)


def consumir_productos_backen():
    url = url_base + "/productos"
    try:
        respuesta = requests.get(url, timeout=10)
        respuesta.raise_for_status()
        datos = respuesta.json()
        print("Productos:")
        print(datos)
        print("******************************************************************")
    except Exception as e:
        print("Error consumiendo productos:", e)


def consumir_mesas_backen():
    url = url_base + "/mesas"
    try:
        respuesta = requests.get(url, timeout=10)
        respuesta.raise_for_status()
        datos = respuesta.json()
        print("Mesas:")
        print(datos)
        print("******************************************************************")
    except Exception as e:
        print("Error consumiendo mesas:", e)


def consumir_clientes_backen():
    url = url_base + "/clientes"
    try:
        respuesta = requests.get(url, timeout=10)
        respuesta.raise_for_status()
        datos = respuesta.json()
        print("Clientes:")
        print(datos)
        print("******************************************************************")
    except Exception as e:
        print("Error consumiendo clientes:", e)


if __name__ == "__main__":
    consumir_categorias_backen()
    consumir_productos_backen()
    consumir_mesas_backen()
    consumir_clientes_backen()
