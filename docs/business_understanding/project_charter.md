# Project Charter - Entendimiento del Negocio

## Nombre del Proyecto

Predicción del precio de venta de viviendas residenciales en Ames, Iowa, con modelos de regresión de Machine Learning

## Objetivo del Proyecto

Desarrollar un modelo de Machine Learning supervisado (regresión) que estime el precio de venta (SalePrice) de una vivienda residencial a partir de sus características físicas, de ubicación, de calidad y de las condiciones de la venta.

## Alcance del Proyecto

### Incluye:

- Datos disponibles: el conjunto de datos público House Prices – Advanced Regression Techniques de Kaggle (https://www.kaggle.com/c/house-prices-advanced-regression-techniques), compilado por Dean De Cock con fines educativos. Contiene ventas de viviendas residenciales en Ames, Iowa (EE. UU.) entre 2006 y 2010:

* train.csv: 1.460 viviendas con 79 variables explicativas más el precio de venta (SalePrice, en dólares), que es la variable objetivo.

* test.csv: 1.459 viviendas con las mismas 79 variables, sin precio, para generar predicciones.
data_description.txt: descripción oficial de cada variable y de sus categorías.

* Las variables son tanto numéricas (áreas en pies cuadrados, años de construcción y remodelación, número de baños y habitaciones, garajes) como categóricas (barrio, tipo de zona, calidad y condición de materiales, tipo de venta). Varias tienen valores faltantes que en realidad significan "no tiene" (por ejemplo, sin piscina o sin sótano).

- Resultados esperados:
    * Código reproducible de carga de datos y un diccionario de datos.
    * Análisis exploratorio con hallazgos sobre la distribución del precio y su relación con las variables.
    * Un pipeline de preprocesamiento (imputación, codificación de variables categóricas, transformación de la variable objetivo) y de ingeniería de características.
    * Un modelo de regresión entrenado, evaluado y documentado, con la importancia de las variables.
    * Un despliegue básico del modelo (por ejemplo, una API o una aplicación sencilla) que reciba las características de una vivienda y devuelva el precio estimado.
    * Un informe final con resultados, conclusiones y limitaciones.

- Criterios de éxito del proyecto:
    * El modelo final mejora de forma clara a una línea base simple (predecir la mediana del precio y una regresión lineal sin regularizar).

### Excluye:

- Datos de otras ciudades o de periodos posteriores a 2010. El modelo solo es válido para el mercado de Ames entre 2006 y 2010, y no se espera que generalice a otros mercados (por ejemplo, Colombia) sin reentrenarlo con datos locales.

- Variables macroeconómicas externas (tasas de interés, inflación, índices de precios de vivienda) y fuentes de datos adicionales como imágenes de las viviendas, textos de anuncios o datos geográficos detallados.

## Metodología

El proyecto sigue la metodología TDSP (Team Data Science Process) de Microsoft, que organiza el ciclo de vida de un proyecto de ciencia de datos en etapas iterativas:

a. Entendimiento del negocio: definir el problema, los objetivos, el alcance y los criterios de éxito (este documento).

b. Adquisición y entendimiento de los datos: descargar los datos de Kaggle mediante su API con un script reproducible, construir el diccionario de datos, realizar el análisis exploratorio y evaluar la calidad de los datos.

c. Modelamiento: limpieza e imputación de faltantes, codificación de variables categóricas, transformación logarítmica de SalePrice, ingeniería de características (por ejemplo, área total y antigüedad de la vivienda) y entrenamiento de modelos con scikit-learn y librerías de boosting: regresión lineal, Ridge, Lasso, ElasticNet, Random Forest, Gradient Boosting y XGBoost o LightGBM. Los hiperparámetros se ajustan con validación cruzada de 5 particiones, sin usar los datos de evaluación.

d. Despliegue: empaquetar el pipeline final (preprocesamiento y modelo) y exponerlo mediante una API o una aplicación sencilla para obtener predicciones.

e. Aceptación por el cliente: evaluar los resultados frente a los criterios de éxito y entregar el informe final.

El código se versiona en GitHub siguiendo la estructura de carpetas de la plantilla TDSP del curso.

## Cronograma

a. Entendimiento del negocio y carga de datos: 1 semana
b. Preprocesamiento, análisis exploratorio: 1 semana
c. Modelamiento y extracción de características: 1 semana
d. Despliegue y entrega: 1 semana

## Equipo del Proyecto

- Melba Esperanza Corredor Suesca

## Presupuesto

El proyecto es de carácter académico y no requiere presupuesto monetario:

a. Datos: públicos y gratuitos (Kaggle).

b. Infraestructura de cómputo: Google Colab en su versión gratuita o un equipo personal. El conjunto de datos es pequeño (menos de 1 MB) y no requiere GPU.

c. Software: herramientas de código abierto (Python, pandas, scikit-learn, XGBoost/LightGBM, Git y GitHub).

d. Recurso humano: alrededor de 4 a 6 horas semanales de dedicación durante las 4 semanas del proyecto.

## Stakeholders

1. Docente del módulo de Metodologías para el desarrollo de proyectos de ML – Evaluador académico. Revisa las entregas en cada etapa. 

2. Agentes y agencias inmobiliarias (usuarios potenciales) – Usan el modelo para sugerir un precio de publicación a sus clientes. 

3. Vendedores y compradores de vivienda (beneficiarios finales) – Reciben una referencia objetiva del valor de una vivienda para negociar. 


## Aprobaciones

- [Nombre y cargo del aprobador del proyecto]
- [Firma del aprobador]
- [Fecha de aprobación]
