# Modulo para consumir los endpoints del backend POS y traer los datos reales
# Se usan para graficar en lugar de los datos simulados

import requests
import pandas as pd

# URL base del backend local
URL_BASE = "http://localhost:8080/api"

# Configuracion de SQL Server (del application-sqlserver.yml)
SQL_SERVER_CONN = (
    "DRIVER={ODBC Driver 17 for SQL Server};"
    "SERVER=localhost,1433;"
    "DATABASE=pos_restaurante;"
    "UID=sa;"
    "PWD=Sa123456;"
    "TrustServerCertificate=yes;"
)


def _get_json(url):
    """Hace peticion GET y devuelve el JSON parseado."""
    try:
        respuesta = requests.get(url, timeout=15)
        respuesta.raise_for_status()
        return respuesta.json()
    except Exception as e:
        print(f"[ERROR] No se pudo consumir {url}: {e}")
        return None


def obtener_clientes_backend():
    # Consume el endpoint de clientes del backend
    datos = _get_json(f"{URL_BASE}/clientes")
    if datos is None:
        return pd.DataFrame()

    # El endpoint devuelve una lista directa
    df = pd.DataFrame(datos)

    # Se normalizan las columnas para que coincidan con lo esperado en graficas
    df = df.rename(columns={
        "totalCompras": "total_compras",
    })

    print(f"[OK] Clientes cargados desde backend: {len(df)} registros")
    return df


def obtener_productos_backend():
    # Consume el endpoint de productos del backend
    datos = _get_json(f"{URL_BASE}/productos")
    if datos is None:
        return pd.DataFrame()

    # El endpoint devuelve una lista directa
    df = pd.DataFrame(datos)

    # La columna categoria viene como objeto anidado, se extrae el nombre
    if "categoria" in df.columns:
        df["categoria_nombre"] = df["categoria"].apply(
            lambda x: x["nombre"] if isinstance(x, dict) and "nombre" in x else "Sin categoria"
        )
        df = df.drop(columns=["categoria"])
        df = df.rename(columns={"categoria_nombre": "categoria"})

    print(f"[OK] Productos cargados desde backend: {len(df)} registros")
    return df


def obtener_usuarios_backend():
    # Consume el endpoint de usuarios del backend
    # Este endpoint devuelve un ApiResponse, los datos estan dentro de la clave "datos"
    respuesta = _get_json(f"{URL_BASE}/usuarios")
    if respuesta is None:
        return pd.DataFrame()

    # Extraemos la lista de usuarios del wrapper ApiResponse
    if isinstance(respuesta, dict) and "datos" in respuesta:
        datos = respuesta["datos"]
    else:
        datos = respuesta

    df = pd.DataFrame(datos)

    # El rol viene como objeto anidado, se extrae el nombre del rol
    if "rol" in df.columns:
        df["rol_nombre"] = df["rol"].apply(
            lambda x: x["nombre"] if isinstance(x, dict) and "nombre" in x else "Sin rol"
        )
        df = df.drop(columns=["rol"])
        df = df.rename(columns={"rol_nombre": "rol_id"})

    print(f"[OK] Usuarios cargados desde backend: {len(df)} registros")
    return df


def obtener_ventas_backend():
    # El endpoint de ventas tiene un bug de recursion infinita en JSON
    # Se lee directamente de SQL Server para evitar el problema
    try:
        import pyodbc
        conn = pyodbc.connect(SQL_SERVER_CONN)
        query = """
            SELECT
                id,
                numero_comprobante,
                tipo_comprobante,
                fecha,
                hora,
                tipo_venta,
                estado,
                subtotal,
                porcentaje_impuesto,
                monto_impuesto,
                descuento,
                total,
                metodo_pago,
                monto_recibido,
                vuelto,
                mesa_numero,
                propina,
                observaciones,
                direccion_entrega,
                telefono_contacto
            FROM venta
            WHERE activo = 1
        """
        df = pd.read_sql(query, conn)
        conn.close()

        # Se asegura que total sea numerico
        df["total"] = pd.to_numeric(df["total"], errors="coerce").fillna(0)

        print(f"[OK] Ventas cargadas desde SQL Server: {len(df)} registros")
        return df
    except Exception as e:
        print(f"[ERROR] No se pudieron cargar ventas desde SQL Server: {e}")
        print("        Asegurate de que SQL Server este corriendo.")
        return pd.DataFrame()
