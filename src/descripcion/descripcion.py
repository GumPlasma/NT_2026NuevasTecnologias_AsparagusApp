# Funciones para describir y hacer analisis exploratorio de los datos
import pandas as pd


def describir_datos(df):
    print("\n--- Info ---")
    df.info()
    print("\n--- Describe ---")
    print(df.describe(include="all"))
    print("\n--- Primeras filas ---")
    print(df.head())
    print("\n--- Nulos ---")
    print(df.isnull().sum())
