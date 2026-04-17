import random
def simular_pedidos(numeroSimulaciones):

    #semillas por cada atributo de mi tabla
    identificadores=["01","02", "03","04","05"]
    estados=["activo","activo", "activo", "activo", "activo"]
    fechas_actualizaciones=["2026-02-01","2026-02-10","2026-02-08","2026-03-01","2026-03-08"]
    fechas_creacion=["2026-01-01","2026-01-01","2026-01-01","2026-01-01","2026-01-01"]
    personas=["8", "3","4","2","5"]
    estados=["Activo","Activo","Activo","Activo","Activo"]
    fechas_inicio=["2026-04-17", "2026-04-17","2026-04-17","2026-04-17","2026-04-17"]
    fechas_cierre=["2026-04-17", "2026-04-17","2026-04-17","2026-04-17","2026-04-17"]
    nombres_cliente=["Fernando","Mario","Pedro","Luis","Angel"]
    numerosdepedidos=["22","23","24","25","26"]
    observacionespedidos=["n/a","n/a","n/a","n/a","n/a"]
    mesasid=["13","15","09","08","05"]
    ventasid=["02", "03", "04", "05", "06"]
    #pendiente saber que formato se le va a dar a este atributo.
    fechas_horas=["2026-04-17", "2026-04-17","2026-04-17","2026-04-17","2026-04-17"]
    Totales=["10000","15000","20000","25000","30000"]
    pedidos=[]

    for _ in range(numeroSimulaciones):
        pedido = {
            "id": random.choice(identificadores),
            "activo": random.choice(estados),
            "fecha_actualizacion": random.choice(fechas_actualizaciones),
            "fecha_creacion": random.choice(fechas_creacion),
            "cantidad_personas": random.choice(personas),
            "estado": random.choice(estados),
            "fecha_inicio": random.choice(fechas_inicio),
            "fecha_cierre": random.choice(fechas_cierre),
            "nombre_cliente": random.choice(nombres_cliente),
            "numero_pedido": random.choice(numerosdepedidos),
            "observaciones": random.choice(observacionespedidos),
            "mesa_id": random.choice(mesasid),
            "venta_id": random.choice(ventasid),
            "fecha_hora": random.choice(fechas_horas),
            "total": random.choice(Totales)
        }
        pedidos.append(pedido)
    return pedidos