"""Funciones de limpieza y validación para diferentes datasets."""

import re

import pandas as pd


# Constantes de validación
_DIRECCIONES_VALIDAS = ["Belen", "Aranjuez", "Guayabal", "Laureles", "Envigado"]
_ROLES_VALIDOS = ["user", "CEO", "ventas", "admin"]
_CATEGORIAS_VALIDAS = ["Verdura", "Fruta", "Hortaliza"]


def limpiar_clientes(df: pd.DataFrame) -> pd.DataFrame:
    """Limpia y valida el DataFrame de clientes.

    Args:
        df: DataFrame con datos de clientes.

    Returns:
        DataFrame limpio y validado.
    """
    df = df.copy()

    # Eliminar filas sin ID
    df = df.dropna(subset=["id"])

    # Convertir fechas
    for col in ["fecha_actualizacion", "fecha_creacion"]:
        df[col] = pd.to_datetime(df[col], errors="coerce")

    # Estandarizar email
    if "e-mail" in df.columns:
        df["e-mail"] = df["e-mail"].str.lower().str.strip()
        df = df[df["e-mail"].str.contains("@", na=False)]

    # Teléfono: solo dígitos
    df["telefono"] = df["telefono"].astype(str).str.replace(r"\D", "", regex=True)

    # Dirección válida
    df["direccion"] = df["direccion"].apply(
        lambda x: x if x in _DIRECCIONES_VALIDAS else "Desconocida"
    )

    # Activo: rellenar nulos
    df["activo"] = df["activo"].fillna("inactivo")

    return df


def limpiar_usuarios(df: pd.DataFrame) -> pd.DataFrame:
    """Limpia y valida el DataFrame de usuarios.

    Args:
        df: DataFrame con datos de usuarios.

    Returns:
        DataFrame limpio y validado.
    """
    df = df.copy()

    df = df.dropna(subset=["id"])

    for col in ["fecha_actualizacion", "fecha_creacion"]:
        df[col] = pd.to_datetime(df[col], errors="coerce")

    # Email
    df["email"] = df["email"].str.lower().str.strip()
    df = df[df["email"].str.contains("@", na=False)]

    # Password: mínimo 6 caracteres
    df["pasword"] = df["pasword"].apply(
        lambda x: x if isinstance(x, str) and len(x) >= 6 else "Temporal123"
    )

    # Teléfono
    df["telefono"] = df["telefono"].astype(str).str.replace(r"\D", "", regex=True)

    # Rol válido
    df["rol_id"] = df["rol_id"].apply(
        lambda x: x if x in _ROLES_VALIDOS else "user"
    )

    return df


def limpiar_pedidos(df: pd.DataFrame) -> pd.DataFrame:
    """Limpia y valida el DataFrame de pedidos.

    Args:
        df: DataFrame con datos de pedidos.

    Returns:
        DataFrame limpio y validado.
    """
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

    # Total no negativo
    df["total"] = pd.to_numeric(df["total"], errors="coerce")
    df = df[df["total"] >= 0]

    # Fecha cierre >= fecha inicio
    mask = df["fecha_cierre"] >= df["fecha_inicio"]
    df = df[mask | df["fecha_cierre"].isna()]

    # mesa_id no vacío
    df = df[df["mesa_id"].astype(str).str.strip() != ""]

    # cantidad_personas numérica
    df["cantidad_personas"] = pd.to_numeric(df["cantidad_personas"], errors="coerce")
    df = df.dropna(subset=["cantidad_personas"])

    return df


def limpiar_productos(df: pd.DataFrame) -> pd.DataFrame:
    """Limpia y valida el DataFrame de productos.

    Args:
        df: DataFrame con datos de productos.

    Returns:
        DataFrame limpio y validado.
    """
    df = df.copy()

    df = df.dropna(subset=["id"])

    for col in ["fecha_actualizacion", "fecha_creacion"]:
        df[col] = pd.to_datetime(df[col], errors="coerce")

    # Precio válido
    df["precio"] = pd.to_numeric(df["precio"], errors="coerce")
    df = df[df["precio"] > 0]

    # Stock numérico
    df["stock"] = pd.to_numeric(df["stock"], errors="coerce")
    df["stock"] = df["stock"].fillna(0)

    # Código de barras limpio
    df["codigo_barras"] = (
        df["codigo_barras"].astype(str).str.strip().str.replace(" ", "")
    )

    # Categoría válida
    df["categoria"] = df["categoria"].apply(
        lambda x: x if x in _CATEGORIAS_VALIDAS else "Otra"
    )

    return df
