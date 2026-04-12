import random
def simular_usuarios(numeroSimulaciones):

    #semillas por cada atributo de mi tabla
    identificadores=["01","02", "03","04","05"]
    estados=["activo","activo", "activo", "activo", "activo"]
    fechas_actualizaciones=["2026-02-01","2026-02-10","2026-02-08","2026-03-01","2026-03-08"]
    fechas_creacion=["2026-01-01","2026-01-01","2026-01-01","2026-01-01","2026-01-01"]
    nombres=["Alejandro","Alejo","Gustavo","Ricardo","Pedro"]
    apellidos=["Gallego","Arroyave","Rendon","Jimemez","Alvarez"]
    correos=["ale@alejo.com","elbro@superprogramador.com","burro@gmail.com","viejoriqui@gmail.com","prueba@prueba.com"]
    claves=["bilingue", "thanoselmastesodelcesde","burro","supervdendedor","pruebas"]
    telefonos=["4446589", "4446658", "4446478", "4446214", "4446587"]
    usuarios=["alebikingue","Thanosfullstack","tavoburro","riquiventas","pruebas"]
    idroles=["user","CEO","menosqueuser","ventas","pruebas"]
    usuarios=[]

    for _ in range(numeroSimulaciones):
        usuario = {
            "id": random.choice(identificadores),
            "activo": random.choice(estados),
            "fecha_actualizacion": random.choice(fechas_actualizaciones),
            "fecha_creacion": random.choice(fechas_creacion),
            "nombre": random.choice(nombres),
            "apellido": random.choice(apellidos),
            "email": random.choice(correos),
            "pasword": random.choice(claves),
            "telefono": random.choice(telefonos),
            "username": random.choice(usuarios),
            "rol_id": random.choice(idroles),
        }
        usuarios.append(usuario)
    return usuarios