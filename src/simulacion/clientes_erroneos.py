# Simulacion de datos de clientes con errores
import random

ids = ["01", "02", "03", "04", "05"]
estados = ["activo"] * 5
fechas_act = ["2026-02-01", "2026-02-10", "2026-02-08", "2026-03-01", "2026-03-08"]
fechas_crea = ["2026-01-01"]
nombres = ["Alejandro", "Elbro", "Gustavo", "Ricardo", "Pedro"]
apellidos = ["Gallego", "Arroyave", "Rendon", "Jimemez", "Alvarez"]
frecuentes = [True, False]
direcciones = ["Belen", "Aranjuez", "Guayabal", "Laureles", "Envigado"]
correos = [
    "ale@alejo.com",
    "elbro@superprogramador.com",
    "burro@gmail.com",
    "viejoriqui@gmail.com",
    "prueba@prueba.com",
]
notas = ["n/a"]
tipos_doc = ["cc", "ti", "pasaporte"]
nums_id = ["12345", "67890", "54321", "09876", "11223", "44556"]
puntos = [10, 30, 45, 60, 90]
telefonos = ["4446589", "4446658", "4446478", "4446214", "4446587"]


def simular_clientes(cantidad):
    clientes = []

    for _ in range(cantidad):
        cliente = {
            "id": random.choice(ids),
            "activo": random.choice(estados),
            "fecha_actualizacion": random.choice(fechas_act),
            "fecha_creacion": random.choice(fechas_crea),
            "apellido": random.choice(apellidos),
            "cliente_frecuente": random.choice(frecuentes),
            "direccion": random.choice(direcciones),
            "e-mail": random.choice(correos),
            "nombre": random.choice(nombres),
            "nota": random.choice(notas),
            "numero_documento": random.choice(nums_id),
            "punto": random.choice(puntos),
            "telefono": random.choice(telefonos),
            "tipo_documento": random.choice(tipos_doc),
        }

        # metemos errores aleatorios
        prob = random.random()

        if prob < 0.2:
            cliente["id"] = None
        elif prob < 0.4:
            cliente["activo"] = None
        elif prob < 0.6:
            cliente["fecha_actualizacion"] = None
        elif prob < 0.8:
            cliente["direccion"] = random.choice(["usa", "canada", "mexico"])
        else:
            cliente["telefono"] = random.choice(["543", "128495", "++9574"])

        clientes.append(cliente)

    return clientes
