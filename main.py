import pandas as pd

# Zona para importar simulaciones
from utils.clientes import simular_clientes
from utils.clientes_error import simular_clientes as simular_clientes_error
from utils.productos import simular_productos
from utils.usuarios import simular_usuarios_con_errores
from utils.pedidos import simular_pedidos_con_errores

# Zona para importar limpiezas
from limpieza.limpieza import limpiar_clientes, limpiar_usuarios, limpiar_pedidos, limpiar_productos

# Zona para importar descripciones
from limpieza.descripcion import describir_datos

if __name__ == "__main__":
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
    print("=" * 50)
    print("DESCRIPCIÓN CLIENTES")
    print("=" * 50)
    describir_datos(df_clientes_limpio)

    print("\n" + "=" * 50)
    print("DESCRIPCIÓN CLIENTES CON ERROR")
    print("=" * 50)
    describir_datos(df_clientes_err_limpio)

    print("\n" + "=" * 50)
    print("DESCRIPCIÓN PRODUCTOS")
    print("=" * 50)
    describir_datos(df_productos_limpio)

    print("\n" + "=" * 50)
    print("DESCRIPCIÓN USUARIOS")
    print("=" * 50)
    describir_datos(df_usuarios_limpio)

    print("\n" + "=" * 50)
    print("DESCRIPCIÓN PEDIDOS")
    print("=" * 50)
    describir_datos(df_pedidos_limpio)
