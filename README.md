# NT_2026NuevasTecnologias_AsparagusApp

Repositorio para la materia de Nuevas Tecnologias.

## Integrantes

- Alejandro Arroyave – Experto FullStack
- Alejandro Gallego – Experto en JS
- Ricardo Jimenez – Experto Analisis de Datos

## Estructura del proyecto

```
.
├── main.py                  # Punto de entrada principal
├── requirements.txt         # Dependencias
├── README.md                # Este archivo
├── graficas/                # Imagenes PNG generadas
├── config/                  # Configuracion global
└── src/                     # Codigo fuente
    ├── api/                 # Consumo de APIs y BD del backend
    │   └── consumo_datos.py
    └── visualizacion/       # Graficas y reportes visuales
        └── graficas.py
```

## Dependencias

```bash
pip install -r requirements.txt
```

## Requisitos previos

- Backend Java (`pos-restaurante`) corriendo en `localhost:8080`
- SQL Server corriendo en `localhost:1433`

## Uso

```bash
python main.py
```

Esto carga los datos reales de las 4 tablas principales (Clientes, Productos, Usuarios, Ventas) y genera 2 graficas por cada una, guardandolas en la carpeta `graficas/`.
