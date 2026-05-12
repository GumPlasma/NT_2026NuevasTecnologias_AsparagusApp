"""Simulación de datos de productos."""

import random


# Semillas de datos
_IDENTIFICADORES = ["01", "02", "03", "04", "05"]
_ESTADOS = ["activo", "inactivo"]
_FECHAS_ACTUALIZACION = [
    "2026-02-01", "2026-02-10", "2026-02-08", "2026-03-01", "2026-03-08"
]
_FECHAS_CREACION = ["2026-01-01"]
_NOMBRES = ["Esparragos", "Tomate", "Lechuga", "Zanahoria", "Papa"]
_CATEGORIAS = ["Verdura", "Fruta", "Hortaliza"]
_PRECIOS = [1500, 3000, 2500, 1800, 2000]
_STOCKS = [100, 50, 0, 200, 75]
_PROVEEDORES = ["01", "02", "03"]
_CODIGOS_BARRAS = [
    "7501234567890",
    "7501234567891",
    "7501234567892",
    "7501234567893",
    "7501234567894",
]
_DESCRIPCIONES = ["Fresco", "Organico", "Premium", "Estándar"]


def simular_productos(numero_simulaciones: int) -> list[dict]:
    """Genera una lista de diccionarios con datos simulados de productos.

    Args:
        numero_simulaciones: Cantidad de registros a generar.

    Returns:
        Lista de diccionarios con datos de productos.
    """
    productos = []

    for _ in range(numero_simulaciones):
        producto = {
            "id": random.choice(_IDENTIFICADORES),
            "activo": random.choice(_ESTADOS),
            "fecha_actualizacion": random.choice(_FECHAS_ACTUALIZACION),
            "fecha_creacion": random.choice(_FECHAS_CREACION),
            "nombre": random.choice(_NOMBRES),
            "categoria": random.choice(_CATEGORIAS),
            "precio": random.choice(_PRECIOS),
            "stock": random.choice(_STOCKS),
            "proveedor_id": random.choice(_PROVEEDORES),
            "codigo_barras": random.choice(_CODIGOS_BARRAS),
            "descripcion": random.choice(_DESCRIPCIONES),
        }

        # Inyección de errores aleatorios
        probabilidad_error = random.random()

        if probabilidad_error < 0.2:
            producto["id"] = None
        elif probabilidad_error < 0.4:
            producto["precio"] = random.choice([0, -1000, None])
        elif probabilidad_error < 0.6:
            producto["stock"] = random.choice([-10, "mucho", None])
        elif probabilidad_error < 0.8:
            producto["codigo_barras"] = " " + producto["codigo_barras"]
        else:
            producto["categoria"] = random.choice(["Carro", "Moto", "Avion"])

        productos.append(producto)

    return productos
