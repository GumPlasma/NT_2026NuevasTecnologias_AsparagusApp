# Simulacion de datos de usuarios con errores
import random

ids = ["01", "02", "03", "04", "05"]
estados = ["activo"] * 5
fechas_act = ["2026-02-01", "2026-02-10", "2026-02-08"]
fechas_crea = ["2026-01-01"]
nombres = ["Alejandro", "Alejo", "Gustavo", "Ricardo", "Pedro"]
apellidos = ["Gallego", "Arroyave", "Rendon", "Jimemez", "Alvarez"]
correos = [
    "ale@alejo.com",
    "elbro@superprogramador.com",
    "burro@gmail.com",
]
claves = ["bilingue", "thanoselmastesodelcesde", "burro", "supervdendedor"]
telefonos = ["4446589", "4446658", "4446478"]
usernames = ["alebikingue", "Thanosfullstack", "tavoburro", "riquiventas"]
roles = ["user", "CEO", "ventas"]


def simular_usuarios_con_errores(cantidad):
    usuarios = []

    for _ in range(cantidad):
        usuario = {
            "id": random.choice(ids),
            "activo": random.choice(estados),
            "fecha_actualizacion": random.choice(fechas_act),
            "fecha_creacion": random.choice(fechas_crea),
            "nombre": random.choice(nombres),
            "apellido": random.choice(apellidos),
            "email": random.choice(correos),
            "pasword": random.choice(claves),
            "telefono": random.choice(telefonos),
            "username": random.choice(usernames),
            "rol_id": random.choice(roles),
        }

        # inyeccion de errores (30% de probabilidad)
        prob = random.random()

        if prob < 0.30:
            tipo_error = random.randint(1, 5)

            if tipo_error == 1:
                # password vacio o muy corto
                usuario["pasword"] = random.choice(["123", "", "admin"])
            elif tipo_error == 2:
                # email sin arroba
                usuario["email"] = usuario["nombre"].lower() + "sin_correo.com"
            elif tipo_error == 3:
                # rol que no existe
                usuario["rol_id"] = "SUPER_ADMIN_GOD_MODE"
            elif tipo_error == 4:
                # telefono con letras
                usuario["telefono"] = "LLAMAR-A-CASA"
            elif tipo_error == 5:
                # inactivo pero con fecha futura
                usuario["activo"] = "inactivo"
                usuario["fecha_actualizacion"] = "2099-12-31"

        usuarios.append(usuario)

    return usuarios
