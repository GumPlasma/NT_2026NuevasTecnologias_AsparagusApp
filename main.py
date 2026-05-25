# Punto de entrada principal del proyecto AsparagusApp
import pandas as pd

# Consumo de datos reales del backend POS
from src.api.consumo_datos import (
    obtener_clientes_backend,
    obtener_productos_backend,
    obtener_usuarios_backend,
    obtener_ventas_backend,
)

# Graficas con datos reales
from src.visualizacion.graficas import (
    graficar_clientes,
    graficar_productos,
    graficar_usuarios,
    graficar_ventas,
)


def main():
    print("=" * 50)
    print("CARGANDO DATOS DESDE EL BACKEND")
    print("=" * 50)

    # Se traen los datos reales de cada tabla del backend
    df_clientes = obtener_clientes_backend()
    df_productos = obtener_productos_backend()
    df_usuarios = obtener_usuarios_backend()
    df_ventas = obtener_ventas_backend()

    # Descripciones de los datasets reales
    datasets = {
        "CLIENTES DEL BACKEND": df_clientes,
        "PRODUCTOS DEL BACKEND": df_productos,
        "USUARIOS DEL BACKEND": df_usuarios,
        "VENTAS DEL BACKEND": df_ventas,
    }

    for titulo, df in datasets.items():
        print("\n" + "=" * 50)
        print(titulo)
        print("=" * 50)
        if not df.empty:
            print(f"Registros: {len(df)}, Columnas: {list(df.columns)}")
            print(df.head())
        else:
            print("[AVISO] No se pudieron cargar datos para esta tabla")

    # Generamos las graficas de las 4 tablas principales con datos reales
    print("\n" + "=" * 50)
    print("GENERANDO GRAFICAS CON DATOS REALES")
    print("=" * 50)

    if not df_clientes.empty:
        graficar_clientes(df_clientes)

    if not df_productos.empty:
        graficar_productos(df_productos)

    if not df_usuarios.empty:
        graficar_usuarios(df_usuarios)

    if not df_ventas.empty:
        graficar_ventas(df_ventas)

    print("\n[FIN] Proceso completado. Revisa la carpeta 'graficas/'.")


if __name__ == "__main__":
    main()
