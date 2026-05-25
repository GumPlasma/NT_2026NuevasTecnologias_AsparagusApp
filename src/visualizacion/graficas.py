# Funciones para graficar los datos del POS
# se hacen 2 graficas por cada tabla principal
# ahora usando los datos reales del backend

import matplotlib.pyplot as plt
import seaborn as sns
import os

# Ruta donde se guardaran las graficas del proyecto
RUTA_GRAFICAS = os.path.join(os.path.dirname(__file__), "..", "..", "graficas")


def crear_ruta_si_no_existe(ruta_destino):
    # Se crea la carpeta destino en caso de que aun no exista
    os.makedirs(ruta_destino, exist_ok=True)


def graficar_barras(datos_agrupados, columna_categorias, columna_valores,
                    titulo="Grafico de barras", color_barras="#4CAF50",
                    nombre_archivo="barras.png", ruta_destino=RUTA_GRAFICAS):
    # Dibuja un grafico de barras verticales, util para comparar cantidades entre categorias
    # Recibe un DataFrame agrupado con una columna categorica y otra numerica

    # Se asegura de que la carpeta donde se guardara la imagen exista
    crear_ruta_si_no_existe(ruta_destino)

    # Se crea la figura y el area de dibujo con un tamano de 10 de ancho por 5 de alto
    figura, area_dibujo = plt.subplots(figsize=(10, 5))

    # Se dibujan las barras con el color recibido y borde negro para mejor contraste
    area_dibujo.bar(
        datos_agrupados[columna_categorias],
        datos_agrupados[columna_valores],
        color=color_barras,
        edgecolor="black"
    )

    # Se coloca el titulo del grafico con tamano de fuente 14
    area_dibujo.set_title(titulo, fontsize=14)

    # Se coloca la etiqueta del eje horizontal con el nombre de la columna categorica
    area_dibujo.set_xlabel(columna_categorias, fontsize=12)

    # Se coloca la etiqueta del eje vertical con el nombre de la columna de valores
    area_dibujo.set_ylabel(columna_valores, fontsize=12)

    # Se rotan las etiquetas del eje X a 45 grados para evitar sobreposicion
    plt.xticks(rotation=45)

    # Se ajusta el espaciado para que nada quede cortado
    plt.tight_layout()

    # Se construye la ruta completa del archivo y se guarda la imagen
    ruta_completa = os.path.join(ruta_destino, nombre_archivo)
    figura.savefig(ruta_completa)

    # Se cierra la figura para liberar memoria
    plt.close(figura)

    # Se imprime la ubicacion donde quedo guardada la imagen
    print(f"Grafico de barras guardado en: {ruta_completa}")


def graficar_torta(datos_agrupados, columna_etiquetas, columna_valores,
                   titulo="Grafico de torta", lista_colores=None,
                   nombre_archivo="torta.png", ruta_destino=RUTA_GRAFICAS):
    # Dibuja un grafico de torta con porcentajes, util para mostrar la proporcion de cada categoria
    # Recibe un DataFrame agrupado con etiquetas y valores numericos

    # Se asegura de que la carpeta donde se guardara la imagen exista
    crear_ruta_si_no_existe(ruta_destino)

    # Si no se recibe una lista de colores, se usa una paleta predeterminada
    if lista_colores is None:
        lista_colores = ["#FF9800", "#2196F3", "#4CAF50", "#E91E63", "#9C27B0"]

    # Se crea la figura y el area de dibujo con tamano cuadrado de 8 por 8
    figura, area_dibujo = plt.subplots(figsize=(8, 8))

    # Se obtiene la cantidad de categorias para recortar la lista de colores
    cantidad_categorias = len(datos_agrupados)

    # Se dibuja la torta con porcentajes, colores y borde negro en cada porcion
    area_dibujo.pie(
        datos_agrupados[columna_valores],
        labels=datos_agrupados[columna_etiquetas],
        autopct="%1.1f%%",
        colors=lista_colores[:cantidad_categorias],
        startangle=90,
        wedgeprops={"edgecolor": "black", "linewidth": 0.5}
    )

    # Se coloca el titulo del grafico con tamano de fuente 14
    area_dibujo.set_title(titulo, fontsize=14)

    # Se ajusta el espaciado para que nada quede cortado
    plt.tight_layout()

    # Se construye la ruta completa del archivo y se guarda la imagen
    ruta_completa = os.path.join(ruta_destino, nombre_archivo)
    figura.savefig(ruta_completa)

    # Se cierra la figura para liberar memoria
    plt.close(figura)

    # Se imprime la ubicacion donde quedo guardada la imagen
    print(f"Grafico de torta guardado en: {ruta_completa}")


def graficar_lineas(datos_agrupados, columna_eje_x, columna_eje_y,
                    titulo="Grafico de lineas", color_linea="#2196F3",
                    nombre_archivo="lineas.png", ruta_destino=RUTA_GRAFICAS):
    # Dibuja un grafico de lineas con marcadores, util para mostrar tendencias en el tiempo
    # Recibe un DataFrame agrupado y los nombres de las columnas para cada eje

    # Se asegura de que la carpeta donde se guardara la imagen exista
    crear_ruta_si_no_existe(ruta_destino)

    # Se crea la figura y el area de dibujo con un tamano de 10 de ancho por 5 de alto
    figura, area_dibujo = plt.subplots(figsize=(10, 5))

    # Se dibuja la linea con marcadores circulares usando el color recibido
    area_dibujo.plot(
        datos_agrupados[columna_eje_x],
        datos_agrupados[columna_eje_y],
        marker="o",
        color=color_linea,
        linewidth=2
    )

    # Se coloca el titulo del grafico con tamano de fuente 14
    area_dibujo.set_title(titulo, fontsize=14)

    # Se coloca la etiqueta del eje horizontal
    area_dibujo.set_xlabel(columna_eje_x, fontsize=12)

    # Se coloca la etiqueta del eje vertical
    area_dibujo.set_ylabel(columna_eje_y, fontsize=12)

    # Se activa la cuadricula con linea punteada y transparencia para mejor lectura
    area_dibujo.grid(True, linestyle="--", alpha=0.6)

    # Se rotan las etiquetas del eje X a 45 grados para que no se sobrepongan
    plt.xticks(rotation=45)

    # Se ajusta el espaciado para que nada quede cortado
    plt.tight_layout()

    # Se construye la ruta completa del archivo y se guarda la imagen
    ruta_completa = os.path.join(ruta_destino, nombre_archivo)
    figura.savefig(ruta_completa)

    # Se cierra la figura para liberar memoria
    plt.close(figura)

    # Se imprime la ubicacion donde quedo guardada la imagen
    print(f"Grafico de lineas guardado en: {ruta_completa}")


# ======================================================================
# Funciones especificas para cada una de las 4 tablas principales del POS
# usando los datos reales del backend
# ======================================================================


def graficar_clientes(df):
    # Grafica 1: barras de clientes por direccion
    datos_direccion = df.groupby("direccion").size().reset_index(name="cantidad")

    graficar_barras(
        datos_agrupados=datos_direccion,
        columna_categorias="direccion",
        columna_valores="cantidad",
        titulo="Clientes por Direccion",
        color_barras="#2196F3",
        nombre_archivo="clientes_direccion.png"
    )

    # Grafica 2: torta de clientes activos vs inactivos
    # En el backend el campo se llama "activo" (booleano)
    datos_activos = df.groupby("activo").size().reset_index(name="cantidad")
    datos_activos["activo"] = datos_activos["activo"].astype(str).replace({
        "True": "Activo",
        "False": "Inactivo"
    })

    graficar_torta(
        datos_agrupados=datos_activos,
        columna_etiquetas="activo",
        columna_valores="cantidad",
        titulo="Clientes Activos vs Inactivos",
        lista_colores=["#4CAF50", "#FF9800"],
        nombre_archivo="clientes_activos.png"
    )


def graficar_productos(df):
    # Grafica 1: barras de precio promedio por categoria
    datos_precio = df.groupby("categoria")["precio"].mean().reset_index(name="precio_promedio")

    graficar_barras(
        datos_agrupados=datos_precio,
        columna_categorias="categoria",
        columna_valores="precio_promedio",
        titulo="Precio Promedio por Categoria",
        color_barras="#FF9800",
        nombre_archivo="productos_precio_categoria.png"
    )

    # Grafica 2: barras de margen de ganancia por producto
    # El backend devuelve margenGanancia calculado automaticamente
    if "margenGanancia" in df.columns:
        datos_margen = df.groupby("nombre")["margenGanancia"].mean().reset_index(name="margen")
    else:
        # Si no existe margenGanancia se calcula aproximado
        df["margen"] = ((df["precio"] - df["costo"]) / df["costo"] * 100).fillna(0)
        datos_margen = df.groupby("nombre")["margen"].mean().reset_index(name="margen")

    graficar_barras(
        datos_agrupados=datos_margen,
        columna_categorias="nombre",
        columna_valores="margen",
        titulo="Margen de Ganancia por Producto (%)",
        color_barras="#4CAF50",
        nombre_archivo="productos_margen.png"
    )


def graficar_usuarios(df):
    # Grafica 1: barras de usuarios por rol
    datos_roles = df.groupby("rol_id").size().reset_index(name="cantidad")

    graficar_barras(
        datos_agrupados=datos_roles,
        columna_categorias="rol_id",
        columna_valores="cantidad",
        titulo="Usuarios por Rol",
        color_barras="#9C27B0",
        nombre_archivo="usuarios_rol.png"
    )

    # Grafica 2: torta de distribucion de roles
    graficar_torta(
        datos_agrupados=datos_roles,
        columna_etiquetas="rol_id",
        columna_valores="cantidad",
        titulo="Distribucion de Roles",
        lista_colores=["#2196F3", "#E91E63", "#FF9800"],
        nombre_archivo="usuarios_roles_torta.png"
    )


def graficar_ventas(df):
    # Grafica 1: barras de total por metodo de pago
    datos_pago = df.groupby("metodo_pago")["total"].sum().reset_index(name="total_ventas")

    graficar_barras(
        datos_agrupados=datos_pago,
        columna_categorias="metodo_pago",
        columna_valores="total_ventas",
        titulo="Total de Ventas por Metodo de Pago",
        color_barras="#E91E63",
        nombre_archivo="ventas_metodo_pago.png"
    )

    # Grafica 2: barras de cantidad de ventas por tipo (MESA, LLEVAR, DELIVERY)
    datos_tipo = df.groupby("tipo_venta").size().reset_index(name="cantidad")

    graficar_barras(
        datos_agrupados=datos_tipo,
        columna_categorias="tipo_venta",
        columna_valores="cantidad",
        titulo="Cantidad de Ventas por Tipo",
        color_barras="#2196F3",
        nombre_archivo="ventas_tipo.png"
    )
