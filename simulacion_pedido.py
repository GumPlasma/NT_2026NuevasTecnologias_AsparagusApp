import random
from datetime import datetime, timedelta

def simular_pedidos_con_errores(numeroSimulaciones):
    # Semillas
    identificadores = ["01", "02", "03", "04", "05"]
    estados_activo = ["Activo"] * 5
    fechas_actualizaciones = ["2026-02-01", "2026-02-10", "2026-02-08"]
    fechas_creacion = ["2026-01-01"]
    personas = ["8", "3", "4", "2", "5"]
    fechas_inicio = ["2026-04-17"]
    fechas_cierre = ["2026-04-17"]
    nombres_cliente = ["Fernando", "Mario", "Pedro", "Luis", "Angel"]
    numerosdepedidos = ["22", "23", "24", "25", "26"]
    observacionespedidos = ["n/a"]
    mesasid = ["13", "15", "09", "08", "05"]
    ventasid = ["02", "03", "04", "05", "06"]
    fechas_horas = ["2026-04-17 14:30:00"]
    totales = ["10000", "15000", "20000", "25000", "30000"]
    
    pedidos = []

    for _ in range(numeroSimulaciones):
        # 1. Generación de dato base
        pedido = {
            "id": random.choice(identificadores),
            "activo": random.choice(estados_activo),
            "fecha_actualizacion": random.choice(fechas_actualizaciones),
            "fecha_creacion": random.choice(fechas_creacion),
            "cantidad_personas": random.choice(personas),
            "estado": random.choice(estados_activo),
            "fecha_inicio": random.choice(fechas_inicio),
            "fecha_cierre": random.choice(fechas_cierre),
            "nombre_cliente": random.choice(nombres_cliente),
            "numero_pedido": random.choice(numerosdepedidos),
            "observaciones": random.choice(observacionespedidos),
            "mesa_id": random.choice(mesasid),
            "venta_id": random.choice(ventasid),
            "fecha_hora": random.choice(fechas_horas),
            "total": random.choice(totales)
        }

        # 2. Inyección de Errores (Probabilidad del 25%)
        probabilidad_error = random.random()

        if probabilidad_error < 0.25:
            error = random.randint(1, 5)

            if error == 1:
                # ERROR LÓGICO: Total negativo (devolución mal aplicada o error de sistema)
                pedido["total"] = "-50000"
                
            elif error == 2:
                # ERROR DE FECHA: Fecha de cierre anterior a la de inicio
                pedido["fecha_cierre"] = "2025-01-01" 
                
            elif error == 3:
                # ERROR DE INTEGRIDAD: Mesa ID vacío o inexistente
                pedido["mesa_id"] = ""
                
            elif error == 4:
                # ERROR DE TIPO: Cantidad de personas como texto no numérico
                pedido["cantidad_personas"] = "Mucha gente"
                
            elif error == 5:
                # ERROR DE DUPLICIDAD SIMULADA: ID nulo
                pedido["id"] = None

        pedidos.append(pedido)
        
    return pedidos