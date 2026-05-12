"""
Ejemplo de rutina de análisis exploratorio de un dataset.

Puntos clave a considerar:
1. Conocer cuántos registros tiene el dataset.
2. Conocer cuántos atributos (columnas) tiene.
3. Tener acceso a la lista de nombres de atributos.
4. Realizar conteos de columnas de interés.
5. Conocer las estadísticas descriptivas de campos numéricos
   (media, máximo, mínimo, desviación estándar, percentiles).
6. Si hay fechas, conocer la fecha más antigua y la más nueva.
"""

import pandas as pd


def describir_datos(data_frame_limpio: pd.DataFrame) -> None:
    """Realiza un análisis exploratorio básico de un dataset.

    Args:
        data_frame_limpio: DataFrame previamente limpio.
    """
    print("*** DESCRIPCIÓN DEL DATASET ***")
    print(f"Número de filas del dataset: {data_frame_limpio.shape[0]}")
    print(f"Número de columnas del dataset: {data_frame_limpio.shape[1]}")
    print(f"Lista de columnas disponibles: {list(data_frame_limpio.columns)}")
    print(f"Tipos de dato de cada atributo:\n{data_frame_limpio.dtypes}")

    # Estadísticas (solo aplica para datos numéricos)
    print("\n*** ESTADÍSTICAS ***")
    columnas_numericas = data_frame_limpio.select_dtypes(include="number").columns
    if not columnas_numericas.empty:
        print(data_frame_limpio[columnas_numericas].describe())
    else:
        print("No se encontraron columnas numéricas.")

    # Información de conteos valiosos
    print("\n*** CONTEOS ***")
    columnas_categoricas = data_frame_limpio.select_dtypes(
        include=["object", "category"]
    ).columns
    for col in columnas_categoricas[:2]:
        print(f"\nConteo de '{col}':")
        print(data_frame_limpio[col].value_counts())

    # Describiendo las fechas
    print("\n*** DESCRIPCIÓN DE FECHAS ***")
    columnas_fecha = data_frame_limpio.select_dtypes(include="datetime").columns
    for col in columnas_fecha[:2]:
        print(f"\nRango de '{col}':")
        print(f"  Mínimo: {data_frame_limpio[col].min()}")
        print(f"  Máximo: {data_frame_limpio[col].max()}")
