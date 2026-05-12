# NT_2026NuevasTecnologias_AsparagusApp

Repositorio para la materia de Nuevas Tecnologías.

## Integrantes

- Alejandro Arroyave – Experto FullStack
- Alejandro Gallego – Experto en JS
- Ricardo Jimenez – Experto Análisis de Datos

## Estructura del proyecto

```
.
├── main.py                      # Punto de entrada principal
├── requirements.txt             # Dependencias del proyecto
├── README.md                    # Documentación general
├── config/                      # Configuración global
├── notebooks/                   # Análisis y scripts exploratorios
│   └── analisis_exploratorio.py
└── src/                         # Código fuente
    ├── data_simulation/         # Generación de datos de prueba
    │   ├── clientes.py
    │   ├── clientes_error.py
    │   ├── productos.py
    │   ├── usuarios.py
    │   └── pedidos.py
    ├── data_cleaning/           # Limpieza y validación de datos
    │   └── cleaners.py
    ├── data_description/        # Descripción y análisis de datos
    │   └── descriptores.py
    └── api/                     # Consumo de APIs externas
        └── consumer.py
```

## Buenas prácticas aplicadas

- **Organización por responsabilidad**: cada módulo tiene una única responsabilidad (simulación, limpieza, descripción, API).
- **Paquete `src/`**: centraliza el código fuente separándolo de configuraciones y notebooks.
- **Docstrings**: todas las funciones y módulos incluyen documentación descriptiva.
- **PEP 8**: nombres en `snake_case`, constantes en `MAYÚSCULAS`, imports ordenados.
- **Type hints**: uso de anotaciones de tipo en argumentos clave.
- **Constantes externadas**: listas de validación y semillas se definen como constantes de módulo.
- **Manejo de errores**: el consumo de APIs incluye `try/except` y timeouts.
- **Punto de ejecución controlado**: `main.py` usa `if __name__ == "__main__":` para evitar ejecuciones accidentales al importar.

## Instalación

```bash
pip install -r requirements.txt
```

## Uso

```bash
python main.py
```
