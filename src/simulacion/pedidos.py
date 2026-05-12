# Simulacion de datos de pedidos con errores
import random

ids = ["01", "02", "03", "04", "05"]
estados_activo = ["Activo"] * 5
fechas_act = ["2026-02-01", "2026-02-10", "2026-02-08"]
fechas_crea = ["2026-01-01"]
personas = ["8", "3", "4", "2", "5"]
fechas_inicio = ["2026-04-17"]
fechas_cierre = ["2026-04-17"]
nombres_cliente = ["Fernando", "Mario", "Pedro", "Luis", "Angel"]
nums_pedido = ["22", "23", "24", "25", "26"]
observaciones = ["n/a"]
mesas = ["13", "15", "09", "08", "05"]
ventas = ["02", "03", "04", "05", "06"]
fechas_hora = ["2026-04-17 14:30:00"]
totales = ["10000", "15000", "20000", "25000", "30000"]


def simular_pedidos_con_errores(cantidad):
    pedidos = []

    for _ in range(cantidad):
        pedido = {
            "id": random.choice(ids),
            "activo": random.choice(estados_activo),
            "fecha_actualizacion": random.choice(fechas_act),
            "fecha_creacion": random.choice(fechas_crea),
            "cantidad_personas": random.choice(personas),
            "estado": random.choice(estados_activo),
            "fecha_inicio": random.choice(fechas_inicio),
            "fecha_cierre": random.choice(fechas_cierre),
            "nombre_cliente": random.choice(nombres_cliente),
            "numero_pedido": random.choice(nums_pedido),
            "observaciones": random.choice(observaciones),
            "mesa_id": random.choice(mesas),
            "venta_id": random.choice(ventas),
            "fecha_hora": random.choice(fechas_hora),
            "total": random.choice(totales),
        }

        # inyeccion de errores (25% de probabilidad)
        prob = random.random()

        if prob < 0.25:
            error = random.randint(1, 5)

            if error == 1:
                # total negativo
                pedido["total"] = "-50000"
            elif error == 2:
                # fecha de cierre antes que la de inicio
                pedido["fecha_cierre"] = "2025-01-01"
            elif error == 3:
                # mesa vacia
                pedido["mesa_id"] = ""
            elif error == 4:
                # cantidad de personas como texto
                pedido["cantidad_personas"] = "Mucha gente"
            elif error == 5:
                # id nulo
                pedido["id"] = None

        pedidos.append(pedido)

    return pedidos
