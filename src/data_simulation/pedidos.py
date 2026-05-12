"""Simulación de datos de pedidos con errores."""

import random


# Semillas de datos
_IDENTIFICADORES = ["01", "02", "03", "04", "05"]
_ESTADOS_ACTIVO = ["Activo"] * 5
_FECHAS_ACTUALIZACION = ["2026-02-01", "2026-02-10", "2026-02-08"]
_FECHAS_CREACION = ["2026-01-01"]
_PERSONAS = ["8", "3", "4", "2", "5"]
_FECHAS_INICIO = ["2026-04-17"]
_FECHAS_CIERRE = ["2026-04-17"]
_NOMBRES_CLIENTE = ["Fernando", "Mario", "Pedro", "Luis", "Angel"]
_NUMEROS_PEDIDO = ["22", "23", "24", "25", "26"]
_OBSERVACIONES = ["n/a"]
_MESAS_ID = ["13", "15", "09", "08", "05"]
_VENTAS_ID = ["02", "03", "04", "05", "06"]
_FECHAS_HORA = ["2026-04-17 14:30:00"]
_TOTALES = ["10000", "15000", "20000", "25000", "30000"]


def simular_pedidos_con_errores(numero_simulaciones: int) -> list[dict]:
    """Genera una lista de diccionarios con datos simulados de pedidos.

    Args:
        numero_simulaciones: Cantidad de registros a generar.

    Returns:
        Lista de diccionarios con datos de pedidos.
    """
    pedidos = []

    for _ in range(numero_simulaciones):
        pedido = {
            "id": random.choice(_IDENTIFICADORES),
            "activo": random.choice(_ESTADOS_ACTIVO),
            "fecha_actualizacion": random.choice(_FECHAS_ACTUALIZACION),
            "fecha_creacion": random.choice(_FECHAS_CREACION),
            "cantidad_personas": random.choice(_PERSONAS),
            "estado": random.choice(_ESTADOS_ACTIVO),
            "fecha_inicio": random.choice(_FECHAS_INICIO),
            "fecha_cierre": random.choice(_FECHAS_CIERRE),
            "nombre_cliente": random.choice(_NOMBRES_CLIENTE),
            "numero_pedido": random.choice(_NUMEROS_PEDIDO),
            "observaciones": random.choice(_OBSERVACIONES),
            "mesa_id": random.choice(_MESAS_ID),
            "venta_id": random.choice(_VENTAS_ID),
            "fecha_hora": random.choice(_FECHAS_HORA),
            "total": random.choice(_TOTALES),
        }

        # Inyección de errores (probabilidad del 25%)
        probabilidad_error = random.random()

        if probabilidad_error < 0.25:
            error = random.randint(1, 5)

            if error == 1:
                # Total negativo
                pedido["total"] = "-50000"
            elif error == 2:
                # Fecha de cierre anterior a la de inicio
                pedido["fecha_cierre"] = "2025-01-01"
            elif error == 3:
                # Mesa ID vacío
                pedido["mesa_id"] = ""
            elif error == 4:
                # Cantidad de personas no numérica
                pedido["cantidad_personas"] = "Mucha gente"
            elif error == 5:
                # ID nulo
                pedido["id"] = None

        pedidos.append(pedido)

    return pedidos
