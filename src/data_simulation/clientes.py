"""Simulación de datos de clientes."""

import random


# Semillas de datos
_IDENTIFICADORES = ["01", "02", "03", "04", "05"]
_ESTADOS = ["activo"] * 5
_FECHAS_ACTUALIZACION = [
    "2026-02-01", "2026-02-10", "2026-02-08", "2026-03-01", "2026-03-08"
]
_FECHAS_CREACION = ["2026-01-01"]
_NOMBRES = ["Alejandro", "Elbro", "Gustavo", "Ricardo", "Pedro"]
_APELLIDOS = ["Gallego", "Arroyave", "Rendon", "Jimemez", "Alvarez"]
_PROGRAMA_FRECUENTES = [True, False]
_DIRECCIONES = ["Belen", "Aranjuez", "Guayabal", "Laureles", "Envigado"]
_CORREOS = [
    "ale@alejo.com",
    "elbro@superprogramador.com",
    "burro@gmail.com",
    "viejoriqui@gmail.com",
    "prueba@prueba.com",
]
_NOTAS = ["n/a"]
_TIPO_DOCUMENTOS = ["cc", "ti", "pasaporte"]
_NUMEROS_IDENTIFICACION = ["12345", "67890", "54321", "09876", "11223", "44556"]
_PUNTOS = [10, 30, 45, 60, 90]
_TELEFONOS = ["4446589", "4446658", "4446478", "4446214", "4446587"]


def simular_clientes(numero_simulaciones: int) -> list[dict]:
    """Genera una lista de diccionarios con datos simulados de clientes.

    Args:
        numero_simulaciones: Cantidad de registros a generar.

    Returns:
        Lista de diccionarios con datos de clientes.
    """
    clientes = []

    for _ in range(numero_simulaciones):
        cliente = {
            "id": random.choice(_IDENTIFICADORES),
            "activo": random.choice(_ESTADOS),
            "fecha_actualizacion": random.choice(_FECHAS_ACTUALIZACION),
            "fecha_creacion": random.choice(_FECHAS_CREACION),
            "apellido": random.choice(_APELLIDOS),
            "cliente_frecuente": random.choice(_PROGRAMA_FRECUENTES),
            "direccion": random.choice(_DIRECCIONES),
            "e-mail": random.choice(_CORREOS),
            "nombre": random.choice(_NOMBRES),
            "nota": random.choice(_NOTAS),
            "numero_documento": random.choice(_NUMEROS_IDENTIFICACION),
            "punto": random.choice(_PUNTOS),
            "telefono": random.choice(_TELEFONOS),
            "tipo_documento": random.choice(_TIPO_DOCUMENTOS),
        }

        # Inyección de errores aleatorios
        probabilidad_error = random.random()

        if probabilidad_error < 0.2:
            cliente["id"] = None
        elif probabilidad_error < 0.4:
            cliente["activo"] = None
        elif probabilidad_error < 0.6:
            cliente["fecha_actualizacion"] = None
        elif probabilidad_error < 0.8:
            cliente["direccion"] = random.choice(["usa", "canada", "mexico"])
        else:
            cliente["telefono"] = random.choice(["543", "128495", "++9574"])

        clientes.append(cliente)

    return clientes
