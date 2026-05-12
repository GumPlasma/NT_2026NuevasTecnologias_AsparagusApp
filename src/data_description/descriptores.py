"""Funciones para la descripción y análisis exploratorio de datos."""

import pandas as pd


def describir_datos(df: pd.DataFrame) -> None:
    """Muestra un resumen descriptivo del DataFrame.

    Incluye información general, estadísticas descriptivas,
    primeras filas y conteo de valores nulos.

    Args:
        df: DataFrame a describir.
    """
    print("\n--- Info ---")
    df.info()

    print("\n--- Describe ---")
    print(df.describe(include="all"))

    print("\n--- Primeras filas ---")
    print(df.head())

    print("\n--- Nulos ---")
    print(df.isnull().sum())
