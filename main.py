"""Punto de entrada principal del proyecto AsparagusApp.

Este script coordina la simulación, limpieza y descripción
de datos para clientes, productos, usuarios y pedidos.
"""

import pandas as pd

# Simulación de datos
from src.data_simulation.clientes import simular_clientes
from src.data_simulation.clientes_error import simular_clientes as simular_clientes_error
from src.data_simulation.productos import simular_productos
from src.data_simulation.usuarios import simular_usuarios_con_errores
from src.data_simulation.pedidos import simular_pedidos_con_errores

# Limpieza de datos
from src.data_cleaning.cleaners import (
    limpiar_clientes,
    limpiar_productos,
    limpiar_usuarios,
    limpiar_pedidos,
)

# Descripción de datos
from src.data_description.descriptores import describir_datos


def main() -> None:
    """Ejecuta el pipeline completo de datos."""
    n = 20

    # Clientes
    clientes = simular_clientes(n)
    df_clientes = pd.DataFrame(clientes)
    df_clientes_limpio = limpiar_clientes(df_clientes)

    # Clientes con error
    clientes_err = simular_clientes_error(n)
    df_clientes_err = pd.DataFrame(clientes_err)
    df_clientes_err_limpio = limpiar_clientes(df_clientes_err)

    # Productos
    productos = simular_productos(n)
    df_productos = pd.DataFrame(productos)
    df_productos_limpio = limpiar_productos(df_productos)

    # Usuarios
    usuarios = simular_usuarios_con_errores(n)
    df_usuarios = pd.DataFrame(usuarios)
    df_usuarios_limpio = limpiar_usuarios(df_usuarios)

    # Pedidos
    pedidos = simular_pedidos_con_errores(n)
    df_pedidos = pd.DataFrame(pedidos)
    df_pedidos_limpio = limpiar_pedidos(df_pedidos)

    # Descripciones
    datasets = {
        "DESCRIPCIÓN CLIENTES": df_clientes_limpio,
        "DESCRIPCIÓN CLIENTES CON ERROR": df_clientes_err_limpio,
        "DESCRIPCIÓN PRODUCTOS": df_productos_limpio,
        "DESCRIPCIÓN USUARIOS": df_usuarios_limpio,
        "DESCRIPCIÓN PEDIDOS": df_pedidos_limpio,
    }

    for titulo, df in datasets.items():
        print("\n" + "=" * 50)
        print(titulo)
        print("=" * 50)
        describir_datos(df)


if __name__ == "__main__":
    main()
