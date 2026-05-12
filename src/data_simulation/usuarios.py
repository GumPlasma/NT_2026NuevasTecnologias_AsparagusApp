"""Simulación de datos de usuarios con errores."""

import random


# Semillas de datos
_IDENTIFICADORES = ["01", "02", "03", "04", "05"]
_ESTADOS = ["activo"] * 5
_FECHAS_ACTUALIZACION = ["2026-02-01", "2026-02-10", "2026-02-08"]
_FECHAS_CREACION = ["2026-01-01"]
_NOMBRES = ["Alejandro", "Alejo", "Gustavo", "Ricardo", "Pedro"]
_APELLIDOS = ["Gallego", "Arroyave", "Rendon", "Jimemez", "Alvarez"]
_CORREOS = [
    "ale@alejo.com",
    "elbro@superprogramador.com",
    "burro@gmail.com",
]
_CLAVES = ["bilingue", "thanoselmastesodelcesde", "burro", "supervdendedor"]
_TELEFONOS = ["4446589", "4446658", "4446478"]
_USERNAMES = ["alebikingue", "Thanosfullstack", "tavoburro", "riquiventas"]
_ROLES = ["user", "CEO", "ventas"]


def simular_usuarios_con_errores(numero_simulaciones: int) -> list[dict]:
    """Genera una lista de diccionarios con datos simulados de usuarios.

    Args:
        numero_simulaciones: Cantidad de registros a generar.

    Returns:
        Lista de diccionarios con datos de usuarios.
    """
    usuarios = []

    for _ in range(numero_simulaciones):
        usuario = {
            "id": random.choice(_IDENTIFICADORES),
            "activo": random.choice(_ESTADOS),
            "fecha_actualizacion": random.choice(_FECHAS_ACTUALIZACION),
            "fecha_creacion": random.choice(_FECHAS_CREACION),
            "nombre": random.choice(_NOMBRES),
            "apellido": random.choice(_APELLIDOS),
            "email": random.choice(_CORREOS),
            "pasword": random.choice(_CLAVES),
            "telefono": random.choice(_TELEFONOS),
            "username": random.choice(_USERNAMES),
            "rol_id": random.choice(_ROLES),
        }

        # Inyección de errores (probabilidad del 30%)
        probabilidad_error = random.random()

        if probabilidad_error < 0.30:
            tipo_error = random.randint(1, 5)

            if tipo_error == 1:
                # Password vacío o demasiado corto
                usuario["pasword"] = random.choice(["123", "", "admin"])
            elif tipo_error == 2:
                # Email sin arroba o dominio
                usuario["email"] = f"{usuario['nombre'].lower()}sin_correo.com"
            elif tipo_error == 3:
                # Rol inexistente
                usuario["rol_id"] = "SUPER_ADMIN_GOD_MODE"
            elif tipo_error == 4:
                # Teléfono con letras
                usuario["telefono"] = "LLAMAR-A-CASA"
            elif tipo_error == 5:
                # Usuario inactivo con fecha futura
                usuario["activo"] = "inactivo"
                usuario["fecha_actualizacion"] = "2099-12-31"

        usuarios.append(usuario)

    return usuarios
