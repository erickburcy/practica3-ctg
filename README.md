# Práctica 3 – Análisis Exploratorio y Librería de Visualización (CTG)

Este repositorio contiene el desarrollo de la Práctica 3 del diplomado, que consiste en:

- Preprocesar el conjunto de datos **Cardiotocography (CTG)**.
- Evaluar la completitud de las variables.
- Desarrollar una librería de visualización personalizada.
- Documentar el análisis en un notebook y un reporte en PDF.

## Estructura del repositorio

```text
practica3-ctg/
├─ README.md
├─ requirements.txt
├─ data/
│   └─ CTG.csv
├─ notebooks/
│   └─ Practica3_CTG.ipynb
├─ src/
│   └─ ctg_viz/
│       ├─ __init__.py
│       ├─ preprocessing.py
│       ├─ categorization.py
│       ├─ utils.py
│       └─ plots/
│           ├─ __init__.py
│           ├─ histograms.py
│           ├─ boxplots.py
│           ├─ barplots.py
│           ├─ density.py
│           └─ heatmap.py
├─ tests/
│   ├─ test_preprocessing.py
│   ├─ test_categorization.py
│   └─ test_utils.py
└─ report/
    └─ Reporte_Practica3_CTG.pdf
