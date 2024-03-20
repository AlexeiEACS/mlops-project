# Proyecto DataScience End-to-End

Este proyecto tiene como objetivo proporcionar un aprendizaje profundo sobre cómo llevar a cabo un proyecto de Data Science de principio a fin. Incluye todas las etapas, desde la evaluación de modelos hasta la implementación en un entorno productivo.

## Sobre los Datos

Los datos utilizados en este proyecto se refieren al consumo energético de la industria del acero en Korea. El objetivo es predecir el consumo de energía en kilovatios (KW).

## Estructura del Proyecto

El proyecto sigue una estructura estándar utilizando Cookiecutter. Las dependencias están gestionadas con Pipenv y se utiliza Git como sistema de control de versiones.

### Estructura de Carpetas

- **data**: Contiene los datos en diferentes etapas de procesamiento.
  - **0_raw**: Los datos originales, no modificados.
  - **0_external**: Datos de fuentes externas.
  - **1_interim**: Datos intermedios transformados.
  - **2_final**: Conjuntos de datos finales para modelado.

- **docs**: Documentación del proyecto.
  - **data_dictionaries**: Diccionarios de datos.
  - **references**: Documentación adicional (papers, manuales, etc.).

- **notebooks**: Notebooks de Jupyter para análisis y experimentación.
  - **experimentation.ipynb**: Notebook principal para experimentación.

- **output**: Resultados y salidas del proyecto.
  - **features**: Características generadas.
  - **models**: Modelos entrenados y predicciones.
  - **reports**: Informes generados en diferentes formatos.

- **pipelines**: Pipelines y flujos de trabajo.
  - **mlops_project**: Código de los pasos de los pipelines.
    - **etl.py**: Descarga, generación y procesamiento de datos.
    - **visualize.py**: Visualizaciones exploratorias y orientadas a resultados.
    - **features.py**: Generación de características para modelado.
    - **train.py**: Entrenamiento y evaluación de modelos.
  - **tests**: Pruebas de integración para el API HTTP.

- **serve**: API HTTP para servir predicciones.
  - **app.py**: Punto de entrada del API HTTP.
  - **tests**: Pruebas de integración para el API HTTP.

## Instalación y Uso

Para replicar el entorno de trabajo, sigue estos pasos:

1. Clona el repositorio:
   ```bash
   git clone https://github.com/AlexeiEACS/mlops-project
   cd mlops-project
