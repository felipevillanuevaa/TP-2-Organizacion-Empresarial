# TP-2-Organizacion-Empresarial
Repositorio para el TP 2 de OE, Escenario B – Análisis de Ventas de una Pequeña Empresa

ANÁLISIS DE VENTAS DE UNA PEQUEÑA EMPRESA
Trabajo Práctico Integrador — Gestión Colaborativa, Control de Versiones y Organización Empresarial
Cátedra: Organización Empresarial
Institución: Universidad Tecnológica Nacional — Tecnicatura Universitaria en Programación (TUP) — Modalidad a Distancia
Año Lectivo: 2026

INTEGRANTES DEL EQUIPO
Integrante-Rol: Felipe Villanueva P1 – Líder y Organizador (Hugo) - P3 – Revisor y QA (Luis) / Lourdes Valzura P2 – Desarrolladora Técnica (Paco)

ESCENARIO ELEGIDO
Escenario B – Análisis de Ventas de una Pequeña Empresa
El proyecto analiza un conjunto de datos simulados de ventas comerciales con el objetivo de generar indicadores básicos que permitan interpretar el desempeño de la empresa. Se calculan métricas como ventas totales, producto más vendido y evolución de ventas por mes, acompañadas de una visualización gráfica de los resultados.

DATASET UTILIZADO

Fuente: Dataset de ventas simuladas disponible públicamente
URL: https://gist.github.com/khanusama20/ee33c2869dd5cf3cebdf020be1ca43f6
Formato: CSV
Columnas principales: id, sales_date, sales_amount
Descripción: Registros diarios de ventas con fecha y monto correspondiente, diseñados para la práctica de análisis de datos.

El archivo se encuentra almacenado en la carpeta /datos del repositorio.

ESTRUCTURA DEL REPOSITORIO
analisis-ventas-tup/
│
├── datos/
│   └── dataset.csv
│
├── scripts/
│   └── analisis_ventas.py
│
├── resultados/
│   └── grafico_ventas.png
│
├── README.md
│
└── .gitignore

INSTRUCCIONES PARA EJECUTAR EL SCRIPT
Opción 1 — Google Colab (recomendado)

Abrir Google Colab
Clonar el repositorio ejecutando en una celda:

bash   !git clone https://github.com/TU_USUARIO/analisis-ventas-tup.git
   %cd analisis-ventas-tup

Ejecutar el script:

bash   !python scripts/analisis_ventas.py

Los resultados y el gráfico se guardarán automáticamente en la carpeta /resultados.


TRAZABILIDAD CON JIRA
Todos los commits de este proyecto siguen el formato de Conventional Commits vinculados al tablero de Jira del equipo

Tablero Jira: 

