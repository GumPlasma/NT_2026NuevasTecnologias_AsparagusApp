# Simulacion de datos de productos
import random

ids = ["01", "02", "03", "04", "05"]
estados = ["activo", "inactivo"]
fechas_act = ["2026-02-01", "2026-02-10", "2026-02-08", "2026-03-01", "2026-03-08"]
fechas_crea = ["2026-01-01"]
nombres = ["Esparragos", "Tomate", "Lechuga", "Zanahoria", "Papa"]
categorias = ["Verdura", "Fruta", "Hortaliza"]
precios = [1500, 3000, 2500, 1800, 2000]
stocks = [100, 50, 0, 200, 75]
proveedores = ["01", "02", "03"]
codigos = [
    "7501234567890",
    "7501234567891",
    "7501234567892",
    "7501234567893",
    "7501234567894",
]
descripciones = ["Fresco", "Organico", "Premium", "Estandar"]


def simular_productos(cantidad):
    productos = []

    for _ in range(cantidad):
        producto = {
            "id": random.choice(ids),
            "activo": random.choice(estados),
            "fecha_actualizacion": random.choice(fechas_act),
            "fecha_creacion": random.choice(fechas_crea),
            "nombre": random.choice(nombres),
            "categoria": random.choice(categorias),
            "precio": random.choice(precios),
            "stock": random.choice(stocks),
            "proveedor_id": random.choice(proveedores),
            "codigo_barras": random.choice(codigos),
            "descripcion": random.choice(descripciones),
        }

        # metemos errores aleatorios
        prob = random.random()

        if prob < 0.2:
            producto["id"] = None
        elif prob < 0.4:
            producto["precio"] = random.choice([0, -1000, None])
        elif prob < 0.6:
            producto["stock"] = random.choice([-10, "mucho", None])
        elif prob < 0.8:
            producto["codigo_barras"] = " " + producto["codigo_barras"]
        else:
            producto["categoria"] = random.choice(["Carro", "Moto", "Avion"])

        productos.append(producto)

    return productos
