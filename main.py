# Punto de entrada principal del proyecto AsparagusApp
import pandas as pd

# Simulacion de datos
from src.simulacion.clientes import simular_clientes
from src.simulacion.clientes_erroneos import simular_clientes as simular_clientes_error
from src.simulacion.productos import simular_productos
from src.simulacion.usuarios import simular_usuarios_con_errores
from src.simulacion.pedidos import simular_pedidos_con_errores

# Limpieza de datos
from src.limpieza.limpieza import (
    limpiar_clientes,
    limpiar_productos,
    limpiar_usuarios,
    limpiar_pedidos,
)

# Descripcion de datos
from src.descripcion.descripcion import describir_datos


def main():
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
        "DESCRIPCION CLIENTES": df_clientes_limpio,
        "DESCRIPCION CLIENTES CON ERROR": df_clientes_err_limpio,
        "DESCRIPCION PRODUCTOS": df_productos_limpio,
        "DESCRIPCION USUARIOS": df_usuarios_limpio,
        "DESCRIPCION PEDIDOS": df_pedidos_limpio,
    }

    for titulo, df in datasets.items():
        print("\n" + "=" * 50)
        print(titulo)
        print("=" * 50)
        describir_datos(df)


if __name__ == "__main__":
    main()
