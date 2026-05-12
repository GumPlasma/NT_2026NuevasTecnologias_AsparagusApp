# NT_2026NuevasTecnologias_AsparagusApp

Repositorio para la materia de Nuevas Tecnologías.

## Integrantes

- Alejandro Arroyave – Experto FullStack
- Alejandro Gallego – Experto en JS
- Ricardo Jimenez – Experto Análisis de Datos

## Estructura del proyecto

```
.
├── main.py                  # Punto de entrada principal
├── requirements.txt         # Dependencias
├── README.md                # Este archivo
├── config/                  # Configuración global
├── notebooks/               # Análisis y scripts exploratorios
│   └── analisis.py
└── src/                     # Código fuente
    ├── simulacion/          # Generación de datos de prueba
    │   ├── clientes.py
    │   ├── clientes_erroneos.py
    │   ├── productos.py
    │   ├── usuarios.py
    │   └── pedidos.py
    ├── limpieza/            # Limpieza y validación de datos
    │   └── limpieza.py
    ├── descripcion/         # Descripción y análisis de datos
    │   └── descripcion.py
    └── api/                 # Consumo de APIs externas
        └── consumo.py
```

## Instalación

```bash
pip install -r requirements.txt
```

## Uso

```bash
python main.py
```
