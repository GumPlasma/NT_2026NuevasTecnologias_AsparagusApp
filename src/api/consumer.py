"""Módulo para el consumo de APIs del backend local."""

import requests


_BASE_URL = "http://localhost:8080/api"


def consumir_categorias_backend() -> None:
    """Consulta y muestra las categorías desde el API."""
    url = f"{_BASE_URL}/categorias"
    try:
        respuesta = requests.get(url, timeout=10)
        respuesta.raise_for_status()
        datos = respuesta.json()
        print("Categorías:")
        print(datos)
        print("*" * 66)
    except requests.RequestException as e:
        print(f"Error al consumir categorías: {e}")


def consumir_productos_backend() -> None:
    """Consulta y muestra los productos desde el API."""
    url = f"{_BASE_URL}/productos"
    try:
        respuesta = requests.get(url, timeout=10)
        respuesta.raise_for_status()
        datos = respuesta.json()
        print("Productos:")
        print(datos)
        print("*" * 66)
    except requests.RequestException as e:
        print(f"Error al consumir productos: {e}")


def consumir_mesas_backend() -> None:
    """Consulta y muestra las mesas desde el API."""
    url = f"{_BASE_URL}/mesas"
    try:
        respuesta = requests.get(url, timeout=10)
        respuesta.raise_for_status()
        datos = respuesta.json()
        print("Mesas:")
        print(datos)
        print("*" * 66)
    except requests.RequestException as e:
        print(f"Error al consumir mesas: {e}")


def consumir_clientes_backend() -> None:
    """Consulta y muestra los clientes desde el API."""
    url = f"{_BASE_URL}/clientes"
    try:
        respuesta = requests.get(url, timeout=10)
        respuesta.raise_for_status()
        datos = respuesta.json()
        print("Clientes:")
        print(datos)
        print("*" * 66)
    except requests.RequestException as e:
        print(f"Error al consumir clientes: {e}")


if __name__ == "__main__":
    consumir_categorias_backend()
    consumir_productos_backend()
    consumir_mesas_backend()
    consumir_clientes_backend()
