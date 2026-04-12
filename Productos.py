import random (Productos.py)
def simular_productos(numeroSimulaciones):

    #semillas por cada atributo de mi tabla
    identificadores=["01","02", "03","04","05"]
    estados=["activo","activo", "activo", "activo", "activo"]
    fechas_actualizaciones=["2026-02-01","2026-02-10","2026-02-08","2026-03-01","2026-03-08"]
    fechas_creacion=["2026-01-01","2026-01-01","2026-01-01","2026-01-01","2026-01-01"]
    codigos=["res01","res02","res03","res04","res05"]
    nombres=["sopa","frijoles","arroz","ensalada","carne"]
    costos=["1000","2500","1500","900","3000"]
    descripciones=["Rica Sopa","Deliosos Frijoles","Excelnte Arroz","Ensalasa Peye","Carne tres cuarros"]
    disponibilidades=[True, False]
    precios=["5000","7500","6500", "3900", "4900", "8000"]
    requiere_preparacion=[True, False]
    tiempo_preparacion=[, 30, 45, 60, 90]
    categorias_id=["01", "02", "03", "04", "05"]
    productos=[]

    for _ in range(numeroSimulaciones):
        producto= {
            "id": random.choice(identificadores),
            "activo": random.choice(estados),
            "fecha_actualizacion": random.choice(fechas_actualizaciones),
            "fecha_creacion": random.choice(fechas_creacion),
            "codigo": random.choice(codigos),
            "costo": random.choice(costos),
            "descripcion": random.choice(descripciones),
            "disponible": random.choice(disponibilidades),
            "nombre": random.choice(nombres),
            "precio": random.choice(precios),
            "requiere_preparacion": random.choice(requiere_preparacion),
            "tiempo_preparacion": random.choice(tiempo_preparacion),
            "categoria_id": random.choice(categorias_id),       
        }
        productos.append(producto)
    return productos