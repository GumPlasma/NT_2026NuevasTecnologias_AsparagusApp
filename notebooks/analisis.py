# Toda rutina de analisis debe describir el data set

# 1. Es importante conocer cuantos registros tengo
# 2. Es importante conocer cuantos atributos tengo
# 3. Es util tener acceso a una lista con los nombres de los atributos
# 4. Es util hacer conteos de algunas columnas de interes
# 5. Es util conocer las estadisticas descriptivas de los campos numericos
#    Media-max-min-std-percentiles
# Si tengo fechas es util conocer cual es la fecha mas antigua y la fecha
# mas nueva

import pandas as pd


def describir_datos(data_frame_limpio):
    print("*** DESCRIPCION DEL DATASET ***")
    print(f"Numero de filas del dataset: {data_frame_limpio.shape[0]}")
    print(f"Numero de columnas del dataset: {data_frame_limpio.shape[1]}")
    print(f"Lista de columnas disponibles: {list(data_frame_limpio.columns)}")
    print(f"Tipos de dato de cada atributo: {data_frame_limpio.dtypes}")

    # Estadisticas (SOLO APLICA PARA DATOS NUMERICOS)
    print("*** ESTADISTICAS ***")
    cols_num = data_frame_limpio.select_dtypes(include="number").columns
    if len(cols_num) > 0:
        print(data_frame_limpio[cols_num].describe())
    else:
        print("No hay columnas numericas")

    # Informacion de conteos valiosos
    print("*** CONTEOS ***")
    cols_cat = data_frame_limpio.select_dtypes(include=["object", "category"]).columns
    for col in cols_cat[:2]:
        print(f"\nConteo de '{col}':")
        print(data_frame_limpio[col].value_counts())

    # Describiendo las fechas
    print("*** DESCRIPCION DE FECHAS ***")
    cols_fecha = data_frame_limpio.select_dtypes(include="datetime").columns
    for col in cols_fecha[:2]:
        print(f"\nRango de '{col}':")
        print(f"  Min: {data_frame_limpio[col].min()}")
        print(f"  Max: {data_frame_limpio[col].max()}")
