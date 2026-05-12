# Funciones para limpiar y validar los diferentes datasets
import pandas as pd

direcciones_ok = ["Belen", "Aranjuez", "Guayabal", "Laureles", "Envigado"]
roles_ok = ["user", "CEO", "ventas", "admin"]
categorias_ok = ["Verdura", "Fruta", "Hortaliza"]


def limpiar_clientes(df):
    df = df.copy()
    # quitar filas sin id
    df = df.dropna(subset=["id"])

    # convertir fechas
    for col in ["fecha_actualizacion", "fecha_creacion"]:
        df[col] = pd.to_datetime(df[col], errors="coerce")

    # estandarizar email
    if "e-mail" in df.columns:
        df["e-mail"] = df["e-mail"].str.lower().str.strip()
        df = df[df["e-mail"].str.contains("@", na=False)]

    # telefono: solo digitos
    df["telefono"] = df["telefono"].astype(str).str.replace(r"\D", "", regex=True)

    # direccion valida
    df["direccion"] = df["direccion"].apply(
        lambda x: x if x in direcciones_ok else "Desconocida"
    )

    # activo: rellenar nulos
    df["activo"] = df["activo"].fillna("inactivo")
    return df


def limpiar_usuarios(df):
    df = df.copy()
    df = df.dropna(subset=["id"])

    for col in ["fecha_actualizacion", "fecha_creacion"]:
        df[col] = pd.to_datetime(df[col], errors="coerce")

    # email
    df["email"] = df["email"].str.lower().str.strip()
    df = df[df["email"].str.contains("@", na=False)]

    # password: minimo 6 caracteres
    df["pasword"] = df["pasword"].apply(
        lambda x: x if isinstance(x, str) and len(x) >= 6 else "Temporal123"
    )

    # telefono
    df["telefono"] = df["telefono"].astype(str).str.replace(r"\D", "", regex=True)

    # rol valido
    df["rol_id"] = df["rol_id"].apply(lambda x: x if x in roles_ok else "user")
    return df


def limpiar_pedidos(df):
    df = df.copy()
    df = df.dropna(subset=["id"])

    for col in [
        "fecha_actualizacion",
        "fecha_creacion",
        "fecha_inicio",
        "fecha_cierre",
        "fecha_hora",
    ]:
        df[col] = pd.to_datetime(df[col], errors="coerce")

    # total no negativo
    df["total"] = pd.to_numeric(df["total"], errors="coerce")
    df = df[df["total"] >= 0]

    # fecha cierre >= fecha inicio
    mask = df["fecha_cierre"] >= df["fecha_inicio"]
    df = df[mask | df["fecha_cierre"].isna()]

    # mesa_id no vacio
    df = df[df["mesa_id"].astype(str).str.strip() != ""]

    # cantidad_personas numerica
    df["cantidad_personas"] = pd.to_numeric(df["cantidad_personas"], errors="coerce")
    df = df.dropna(subset=["cantidad_personas"])
    return df


def limpiar_productos(df):
    df = df.copy()
    df = df.dropna(subset=["id"])

    for col in ["fecha_actualizacion", "fecha_creacion"]:
        df[col] = pd.to_datetime(df[col], errors="coerce")

    # precio valido
    df["precio"] = pd.to_numeric(df["precio"], errors="coerce")
    df = df[df["precio"] > 0]

    # stock numerico
    df["stock"] = pd.to_numeric(df["stock"], errors="coerce")
    df["stock"] = df["stock"].fillna(0)

    # codigo de barras limpio
    df["codigo_barras"] = (
        df["codigo_barras"].astype(str).str.strip().str.replace(" ", "")
    )

    # categoria valida
    df["categoria"] = df["categoria"].apply(
        lambda x: x if x in categorias_ok else "Otra"
    )
    return df
