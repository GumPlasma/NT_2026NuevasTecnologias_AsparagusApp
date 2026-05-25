# Script para poblar la base de datos del backend POS
# Inserta clientes, proveedores y productos mediante la API REST

import requests
import random

URL_BASE = "http://localhost:8080/api"


def _post(endpoint, payload):
    """Envia un POST al backend y retorna la respuesta JSON."""
    url = f"{URL_BASE}{endpoint}"
    try:
        resp = requests.post(url, json=payload, timeout=10)
        if resp.status_code in (200, 201):
            print(f"  [OK] {endpoint} -> {payload.get('nombre', payload.get('razonSocial', 'item'))}")
            return resp.json()
        else:
            print(f"  [AVISO] {endpoint} status={resp.status_code}: {resp.text[:100]}")
            return None
    except Exception as e:
        print(f"  [ERROR] {endpoint}: {e}")
        return None


def poblar_clientes():
    print("\n=== POBLANDO CLIENTES ===")
    clientes = [
        {"nombre": "Maria", "apellido": "Gonzalez", "dni": "10203040", "telefono": "3001112233", "email": "maria.g@email.com", "direccion": "Centro", "notas": "Cliente frecuente", "totalCompras": 0, "activo": True},
        {"nombre": "Carlos", "apellido": "Martinez", "dni": "20304050", "telefono": "3102223344", "email": "carlos.m@email.com", "direccion": "Norte", "notas": "Prefiere mesa 5", "totalCompras": 0, "activo": True},
        {"nombre": "Ana", "apellido": "Rodriguez", "dni": "30405060", "telefono": "3203334455", "email": "ana.r@email.com", "direccion": "Sur", "notas": "Alergia a mariscos", "totalCompras": 0, "activo": True},
        {"nombre": "Luis", "apellido": "Hernandez", "dni": "40506070", "telefono": "3304445566", "email": "luis.h@email.com", "direccion": "Oriente", "notas": "Paga con tarjeta", "totalCompras": 0, "activo": True},
        {"nombre": "Carmen", "apellido": "Lopez", "dni": "50607080", "telefono": "3405556677", "email": "carmen.l@email.com", "direccion": "Occidente", "notas": "Cumpleanos en junio", "totalCompras": 0, "activo": True},
        {"nombre": "Pedro", "apellido": "Sanchez", "dni": "60708090", "telefono": "3506667788", "email": "pedro.s@email.com", "direccion": "Centro", "notas": "Trae a la familia", "totalCompras": 0, "activo": True},
        {"nombre": "Diana", "apellido": "Ramirez", "dni": "70809001", "telefono": "3607778899", "email": "diana.r@email.com", "direccion": "Norte", "notas": "Vegetariana", "totalCompras": 0, "activo": True},
        {"nombre": "Jorge", "apellido": "Torres", "dni": "80900102", "telefono": "3708889900", "email": "jorge.t@email.com", "direccion": "Sur", "notas": "Siempre pide delivery", "totalCompras": 0, "activo": True},
        {"nombre": "Sofia", "apellido": "Flores", "dni": "90102030", "telefono": "3809990011", "email": "sofia.f@email.com", "direccion": "Oriente", "notas": "Fan de postres", "totalCompras": 0, "activo": True},
        {"nombre": "Miguel", "apellido": "Diaz", "dni": "11223344", "telefono": "3900001122", "email": "miguel.d@email.com", "direccion": "Occidente", "notas": "Pide factura", "totalCompras": 0, "activo": True},
    ]
    for c in clientes:
        _post("/clientes", c)


def poblar_proveedores():
    print("\n=== POBLANDO PROVEEDORES ===")
    proveedores = [
        {"nombre": "Carnes del Valle S.A.S.", "ruc": "900123456", "contacto": "Juan Pardo", "telefono": "3111111111", "email": "ventas@carnesdelvalle.com", "direccion": "Zona Industrial", "categoria": "CARNES", "notas": "Cortes premium", "activo": True},
        {"nombre": "Verduras Fresh", "ruc": "900234567", "contacto": "Ana Maria", "telefono": "3222222222", "email": "pedidos@verdurasfresh.com", "direccion": "Mercado Central", "categoria": "VERDURAS", "notas": "Organicas", "activo": True},
        {"nombre": "Bebidas Nacional", "ruc": "900345678", "contacto": "Luis Gomez", "telefono": "3333333333", "email": "distribucion@bebnac.com", "direccion": "Av. Principal 45", "categoria": "BEBIDAS", "notas": "Descuento por volumen", "activo": True},
        {"nombre": "Mariscos del Pacifico", "ruc": "900456789", "contacto": "Carla Ruiz", "telefono": "3444444444", "email": "compras@mariscospac.com", "direccion": "Puerto", "categoria": "MARISCOS", "notas": "Pescado fresco diario", "activo": True},
        {"nombre": "Lacteos La Granja", "ruc": "900567890", "contacto": "Pedro Leon", "telefono": "3555555555", "email": "info@lacteoslagranja.com", "direccion": "Carretera Norte km 10", "categoria": "LACTEOS", "notas": "Quesos artesanales", "activo": True},
        {"nombre": "Panaderia El Trigo", "ruc": "900678901", "contacto": "Sofia Mendez", "telefono": "3666666666", "email": "eltrigo@pan.com", "direccion": "Centro Historico", "categoria": "PANADERIA", "notas": "Pan del dia", "activo": True},
        {"nombre": "Condimentos Andinos", "ruc": "900789012", "contacto": "Ricardo Silva", "telefono": "3777777777", "email": "exporta@condandinos.com", "direccion": "Zona Franca", "categoria": "CONDIMENTOS", "notas": "Especias importadas", "activo": True},
        {"nombre": "Postres Dulce Hogar", "ruc": "900890123", "contacto": "Diana Castro", "telefono": "3888888888", "email": "dulcehogar@postres.com", "direccion": "Barrio Nuevo", "categoria": "POSTRES", "notas": "Helados y tortas", "activo": True},
    ]
    for p in proveedores:
        _post("/proveedores", p)


def poblar_productos():
    print("\n=== POBLANDO PRODUCTOS ===")
    # categorias disponibles en BD: 1=Bebbidas, 2=Bebidas, 3=Especiales, 4=Entradas
    productos = [
        {"codigo": "beb01", "nombre": "Jugo de Naranja", "descripcion": "Jugo natural exprimido", "precio": 6500, "costo": 2000, "categoriaId": 2, "disponible": True, "requierePreparacion": False, "tiempoPreparacion": 0},
        {"codigo": "beb02", "nombre": "Limonada", "descripcion": "Limonada natural con hierbabuena", "precio": 5500, "costo": 1500, "categoriaId": 2, "disponible": True, "requierePreparacion": False, "tiempoPreparacion": 0},
        {"codigo": "beb03", "nombre": "Cerveza Artesanal", "descripcion": "Cerveza local rubia", "precio": 12000, "costo": 5000, "categoriaId": 2, "disponible": True, "requierePreparacion": False, "tiempoPreparacion": 0},
        {"codigo": "ent01", "nombre": "Rollos Primavera", "descripcion": "4 rollos con salsa agridulce", "precio": 18000, "costo": 7000, "categoriaId": 4, "disponible": True, "requierePreparacion": True, "tiempoPreparacion": 10},
        {"codigo": "ent02", "nombre": "Edamames", "descripcion": "Frijol de soya al vapor con sal", "precio": 12000, "costo": 4000, "categoriaId": 4, "disponible": True, "requierePreparacion": True, "tiempoPreparacion": 8},
        {"codigo": "ent03", "nombre": "Gyozas de Cerdo", "descripcion": "6 unidades con salsa de soya", "precio": 22000, "costo": 9000, "categoriaId": 4, "disponible": True, "requierePreparacion": True, "tiempoPreparacion": 12},
        {"codigo": "esp01", "nombre": "Sushi Combo 20", "descripcion": "20 piezas variadas para 2 personas", "precio": 45000, "costo": 18000, "categoriaId": 3, "disponible": True, "requierePreparacion": True, "tiempoPreparacion": 15},
        {"codigo": "esp02", "nombre": "Sashimi Mixto", "descripcion": "12 cortes de salmon y atun", "precio": 38000, "costo": 16000, "categoriaId": 3, "disponible": True, "requierePreparacion": True, "tiempoPreparacion": 10},
        {"codigo": "esp03", "nombre": "Tataki de Atun", "descripcion": "Atun sellado con sesame y salsa ponzu", "precio": 32000, "costo": 14000, "categoriaId": 3, "disponible": True, "requierePreparacion": True, "tiempoPreparacion": 12},
        {"codigo": "beb04", "nombre": "Agua con Gas", "descripcion": "Agua mineral con gas", "precio": 4500, "costo": 1200, "categoriaId": 2, "disponible": True, "requierePreparacion": False, "tiempoPreparacion": 0},
        {"codigo": "ent04", "nombre": "Ensalada Wakame", "descripcion": "Algas marinas con sabor oriental", "precio": 15000, "costo": 5000, "categoriaId": 4, "disponible": True, "requierePreparacion": True, "tiempoPreparacion": 5},
        {"codigo": "esp04", "nombre": "Temaki Salmon", "descripcion": "Cono de alga con salmon y aguacate", "precio": 16000, "costo": 6000, "categoriaId": 3, "disponible": True, "requierePreparacion": True, "tiempoPreparacion": 8},
        {"codigo": "beb05", "nombre": "Té Verde", "descripcion": "Té verde caliente tradicional", "precio": 5000, "costo": 1000, "categoriaId": 2, "disponible": True, "requierePreparacion": False, "tiempoPreparacion": 0},
        {"codigo": "esp05", "nombre": "Udon de Mariscos", "descripcion": "Fideos gruesos con camarones y calamares", "precio": 28000, "costo": 11000, "categoriaId": 3, "disponible": True, "requierePreparacion": True, "tiempoPreparacion": 18},
        {"codigo": "ent05", "nombre": "Calamar Frito", "descripcion": "Anillos de calamar apanados", "precio": 20000, "costo": 8000, "categoriaId": 4, "disponible": True, "requierePreparacion": True, "tiempoPreparacion": 10},
    ]
    for p in productos:
        _post("/productos", p)


def _get(endpoint):
    """Hace un GET al backend y retorna el JSON."""
    try:
        resp = requests.get(f"{URL_BASE}{endpoint}", timeout=10)
        resp.raise_for_status()
        return resp.json()
    except Exception as e:
        print(f"  [ERROR] GET {endpoint}: {e}")
        return None


def poblar_ventas():
    print("\n=== POBLANDO VENTAS ===")

    # Traemos productos y clientes actuales para usar sus IDs
    productos = _get("/productos")
    clientes = _get("/clientes")
    usuarios_resp = _get("/usuarios")

    # Normalizamos respuestas: algunas vienen como lista directa, otras como dict con "value"
    if isinstance(productos, dict) and "value" in productos:
        lista_productos = productos["value"]
    elif isinstance(productos, list):
        lista_productos = productos
    else:
        lista_productos = []

    if isinstance(clientes, dict) and "value" in clientes:
        lista_clientes = clientes["value"]
    elif isinstance(clientes, list):
        lista_clientes = clientes
    else:
        lista_clientes = []

    if not lista_productos:
        print("  [AVISO] No hay productos para generar ventas")
        return

    if not lista_clientes:
        print("  [AVISO] No hay clientes para generar ventas")
        return

    # Extraemos IDs de productos disponibles
    ids_productos = [p["id"] for p in lista_productos if p.get("disponible")]

    # Extraemos IDs de clientes
    ids_clientes = [c["id"] for c in lista_clientes]

    # Extraemos IDs de usuarios (vendedores)
    ids_vendedores = [1, 2, 4]  # admin, vendedor, adminSM (conocidos del sistema)
    if usuarios_resp and isinstance(usuarios_resp, dict) and "datos" in usuarios_resp:
        ids_vendedores = [u["id"] for u in usuarios_resp["datos"]]

    metodos_pago = ["EFECTIVO", "TARJETA", "TRANSFERENCIA"]
    tipos_venta = ["LLEVAR", "MESA", "DELIVERY"]

    # Generamos 15 ventas variadas
    ventas = []
    for i in range(1, 16):
        # Cada venta tendra entre 1 y 3 productos aleatorios
        cantidad_productos = random.randint(1, 3)
        productos_venta = random.sample(ids_productos, min(cantidad_productos, len(ids_productos)))

        detalles = []
        for pid in productos_venta:
            detalles.append({
                "productoId": pid,
                "cantidad": random.randint(1, 5),
                "descuento": 0,
                "notas": random.choice(["", "Sin picante", "Extra salsa", "Para llevar rapido"])
            })

        venta = {
            "vendedorId": random.choice(ids_vendedores),
            "tipoVenta": random.choice(tipos_venta),
            "tipoComprobante": random.choice(["TICKET", "BOLETA", "FACTURA"]),
            "metodoPago": random.choice(metodos_pago),
            "descuento": random.choice([0, 1000, 2500, 5000]),
            "montoRecibido": random.choice([20000, 50000, 100000, 150000]),
            "observaciones": random.choice(["", "Cliente frecuente", "Pide factura", "Delivery express"]),
            "direccionEntrega": random.choice(["Calle 1 # 10-20", "Av Principal 45", "Barrio Nuevo", None]),
            "telefonoContacto": random.choice(["3001112233", "3102223344", None]),
            "detalles": detalles
        }
        ventas.append(venta)

    for v in ventas:
        resp = _post("/ventas/directa", v)
        if resp:
            print(f"    Venta creada: {v['metodoPago']} - {v['tipoVenta']} - {len(v['detalles'])} productos")


def main():
    print("=" * 50)
    print("POBLANDO BASE DE DATOS DEL POS")
    print("=" * 50)
    poblar_clientes()
    poblar_proveedores()
    poblar_productos()
    poblar_ventas()
    print("\n[FIN] Proceso de poblacion completado.")


if __name__ == "__main__":
    main()
