import random
from datetime import datetime, timedelta

def simular_usuarios_con_errores(numeroSimulaciones):
    # Semillas
    identificadores = ["01", "02", "03", "04", "05"]
    estados = ["activo"] * 5
    fechas_actualizaciones = ["2026-02-01", "2026-02-10", "2026-02-08"]
    fechas_creacion = ["2026-01-01"]
    nombres = ["Alejandro", "Alejo", "Gustavo", "Ricardo", "Pedro"]
    apellidos = ["Gallego", "Arroyave", "Rendon", "Jimemez", "Alvarez"]
    correos = ["ale@alejo.com", "elbro@superprogramador.com", "burro@gmail.com"]
    claves = ["bilingue", "thanoselmastesodelcesde", "burro", "supervdendedor"]
    telefonos = ["4446589", "4446658", "4446478"]
    usernames_semilla = ["alebikingue", "Thanosfullstack", "tavoburro", "riquiventas"]
    idroles = ["user", "CEO", "ventas"]
    
    lista_usuarios_final = []

    for _ in range(numeroSimulaciones):
        # 1. Generación base
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
            "username": random.choice(usernames_semilla),
            "rol_id": random.choice(idroles),
        }

        # 2. Inyección de Errores de Usuario (Probabilidad 30%)
        prob_error = random.random()
        
        if prob_error < 0.30:
            tipo_error = random.randint(1, 5)
            
            if tipo_error == 1:
                # ERROR DE SEGURIDAD: Password vacío o demasiado corto
                usuario["pasword"] = random.choice(["123", "", "admin"])
                
            elif tipo_error == 2:
                # ERROR DE FORMATO: Email sin el arroba o dominio
                usuario["email"] = usuario["nombre"].lower() + "sin_correo.com"
                
            elif tipo_error == 3:
                # ERROR DE ROL: Asignar un rol de sistema inexistente o "hacker"
                usuario["rol_id"] = "SUPER_ADMIN_GOD_MODE"
                
            elif tipo_error == 4:
                # ERROR DE TIPO: Teléfono con letras
                usuario["telefono"] = "LLAMAR-A-CASA"
                
            elif tipo_error == 5:
                # ERROR DE LÓGICA: Usuario inactivo pero con fecha de actualización futura
                usuario["activo"] = "inactivo"
                usuario["fecha_actualizacion"] = "2099-12-31"

        lista_usuarios_final.append(usuario)
        
    return lista_usuarios_final