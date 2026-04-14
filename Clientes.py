import random
def simular_productos(numeroSimulaciones):

    #semillas por cada atributo de mi tabla
    identificadores=["01","02", "03","04","05"]
    estados=["activo","activo", "activo", "activo", "activo"]
    fechas_actualizaciones=["2026-02-01","2026-02-10","2026-02-08","2026-03-01","2026-03-08"]
    fechas_creacion=["2026-01-01","2026-01-01","2026-01-01","2026-01-01","2026-01-01"]
    nombre=["Alejandro", "Elbro","Gustavo","Ricardo","Pedro"]
    apellidos=["Gallego","Arroyave","Rendon","Jimemez","Alvarez"]
    programa_frecuentes=[True, False]
    direccion=["Belen","Aranjuez","Guayabal","Lauereles","Envigado"]
    correo=["ale@alejo.com","elbro@superprogramador.com","burro@gmail.com","viejoriqui@gmail.com","prueba@prueba.com"]
    notas=["n/a","n/a","n/a","n/a","n/a","n/a"]
    tipo_documentos=["cc","ti","pasaporte","cc","cc"]
    numero_identificacion=["12345,""67890","54321","09876","11223","44556"]
    puntos=[10, 30, 45, 60, 90]
    telefonos=["4446589", "4446658", "4446478", "4446214", "4446587"]
    clientes=[]

    for _ in range(numeroSimulaciones):
        cliente = {
            "id": random.choice(identificadores),
            "activo": random.choice(estados),
            "fecha_actualizacion": random.choice(fechas_actualizaciones),
            "fecha_creacion": random.choice(fechas_creacion),
            "apellido": random.choice(apellidos),
            "cliente_frecuente": random.choice(programa_frecuentes),
            "direccion": random.choice(direccion),
            "e-mail": random.choice(correo),
            "nombre": random.choice(nombre),
            "nota": random.choice(notas),
            "numero_documento": random.choice(numero_identificacion),
            "punto": random.choice(puntos),
            "telefono": random.choice(telefonos),
            "tipo_documento": random.choice(tipo_documentos),
        }
        clientes.append(cliente)
    return clientes