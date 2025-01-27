# 📊 Análisis de Marketing Bancario

## 📖 Descripción
Este proyecto realiza un análisis exploratorio de datos para entender los patrones de comportamiento de los clientes bancarios. Su objetivo es identificar factores clave que influyen en las campañas de marketing.

## 🗂 Estructura de las carpetas del Proyecto
├── data/                # Datos crudos y procesados
├── notebooks/           # Notebooks de Jupyter con el análisis
├── src/                 # Scripts de procesamiento
├── results/             # Gráficos y conclusiones
├── README.md            # Descripción del proyecto


Este proyecto utiliza Python 3.8 y requiere las siguientes bibliotecas:
- pandas
- numpy
- jupyter

## Progreso del Proyecto
1. **Carga de datos brutos**: Se han incorporado los datos iniciales en la carpeta `data/Data_origen`.
2. **Creación del EDA preliminar**: Se ha creado un notebook en `notebooks/eda_preliminar.ipynb` para comenzar el análisis.
3. **Importación de librerías**: Se han importado las librerías necesarias (`pandas`, `numpy`).
4. **Primera lectura de datos**: Se ha realizado una inspección inicial de los datos (`head`) para entender la estructura y el contenido del conjunto.

### 1ª Descripción de las columnas - EDA PRELIMINAR

Este dataset contiene información bancaria y variables macroeconómicas relacionadas con clientes y campañas de marketing. A continuación, se detalla cada columna:

| **Columna**          | **Descripción**                                                                |
|-----------------------|-------------------------------------------------------------------------------|
| `Unnamed: 0`         | Índice sin nombre.                                                             |
| `age`                | Edad del cliente.                                                              |
| `job`                | Profesión del cliente.                                                         |
| `marital`            | Estado civil del cliente (ej. "MARRIED", "SINGLE").                            |
| `education`          | Nivel educativo del cliente (ej. "high.school", "basic.4y").                   |
| `default`            | Indica si el cliente tiene un crédito en mora (0 = no, 1 = sí).                |
| `housing`            | Indica si el cliente tiene un préstamo hipotecario (0 = no, 1 = sí).           |
| `loan`               | Indica si el cliente tiene un préstamo personal (0 = no, 1 = sí).              |
| `contact`            | Tipo de contacto utilizado (ej. "telephone", "cellular").                      |
| `duration`           | Duración de la última llamada en segundos.                                     |
| `campaign`           | Número de contactos realizados durante esta campaña.                           |
| `pdays`              | Número de días desde el último contacto con el cliente.                        |
| `previous`           | Número de contactos realizados antes de esta campaña.                          |
| `poutcome`           | Resultado de la campaña de marketing anterior.                                 |
| `emp.var.rate`       | Tasa de variación del empleo (variable macroeconómica).                        |
| `cons.price.idx`     | Índice de precios al consumidor.                                               |
| `cons.conf.idx`      | Índice de confianza del consumidor.                                            |
| `euribor3m`          | Tasa de interés del Euribor a 3 meses.                                         |
| `nr.employed`        | Número total de empleados (indicador macroeconómico).                          |
| `y`                  | Variable objetivo:  si el cliente aceptó una oferta o producto ("yes"/"no").   |
| `date`               | Fecha asociada al contacto o registro.                                         |
| `latitude`           | Latitud del cliente, posiblemente vinculada a su ubicación geográfica.         |
| `longitude`          | Longitud del cliente, posiblemente vinculada a su ubicación geográfica.        |
| `id`                 | Identificador único del cliente.                                               |

---

Este resumen combina la descripción y los nombres de las columnas en una única tabla para mayor claridad. También destaca que estas columnas serán utilizadas en el análisis exploratorio de datos.


### Dimensiones e informacion general del dataset

El dataset contiene **43,000 filas** y **24 columnas**. A continuación, se detalla la información clave sobre los tipos de datos y los valores no nulos de cada columna:

| **Columna**       | **Tipo de dato** | **Valores no nulos** | **Descripción**                                                        |
|--------------------|------------------|-----------------------|--------------------------------------------------------------------- |
| `Unnamed: 0`      | int64            | 43,000               | Índice sin nombre, posiblemente un residuo de exportaciones previas.   |
| `age`             | float64          | 37,880               | Edad del cliente (valores nulos = 5,120).                              |
| `job`             | object           | 42,655               | Profesión del cliente (valores nulos = 345).                           |
| `marital`         | object           | 42,915               | Estado civil del cliente (valores nulos = 85).                         |
| `education`       | object           | 41,193               | Nivel educativo del cliente (valores nulos = 1,807).                   |
| `default`         | float64          | 34,019               | Indica si el cliente tiene un crédito en mora (valores nulos = 8,981). |
| `housing`         | float64          | 41,974               | Indica si el cliente tiene un préstamo hipotecario.                    |
| `loan`            | float64          | 41,974               | Indica si el cliente tiene un préstamo personal.                       |
| `contact`         | object           | 43,000               | Tipo de contacto utilizado (sin valores nulos).                        |
| `duration`        | int64            | 43,000               | Duración de la última llamada en segundos (sin valores nulos).         |
| `campaign`        | int64            | 43,000               | Número de contactos realizados durante esta campaña (sin valores nulos)|
| `pdays`           | int64            | 43,000               | Número de días desde el último contacto con el cliente.                |
| `previous`        | int64            | 43,000               | Número de contactos realizados antes de esta campaña.                  |
| `poutcome`        | object           | 43,000               | Resultado de la campaña de marketing anterior.                         |
| `emp.var.rate`    | float64          | 43,000               | Tasa de variación del empleo.                                          |
| `cons.price.idx`  | float64          | 42,529               | Índice de precios al consumidor (valores nulos = 471).                 |
| `cons.conf.idx`   | object           | 43,000               | Índice de confianza del consumidor.                                    |
| `euribor3m`       | float64          | 33,744               | Tasa de interés del Euribor a 3 meses (valores nulos = 9,256).         |
| `nr.employed`     | object           | 43,000               | Número total de empleados (indicador macroeconómico).                  |
| `y`               | object           | 43,000               | Variable objetivo: indica si el cliente aceptó una oferta o producto.  |
| `date`            | object           | 43,000               | Fecha asociada al contacto o registro.                                 |
| `latitude`        | float64          | 43,000               | Latitud del cliente (sin valores nulos).                               |
| `longitude`       | float64          | 43,000               | Longitud del cliente (sin valores nulos).                              |
| `id`              | object           | 43,000               | Identificador único del cliente.                                       |

#### Observaciones:
- **Valores nulos**: Hay columnas con valores nulos, como `age` (5,120 nulos) y `education` (1,807 nulos), que deben ser tratados antes del análisis.
- **Tipos de datos**: Hay una mezcla de datos numéricos (`int64`, `float64`) y categóricos (`object`), lo que requiere diferentes estrategias de procesamiento según el análisis que se desee realizar.
### Valores nulos en el dataset

Al analizar las columnas, se detectó que algunas contienen valores nulos. Esto se determinó comparando el número de valores no nulos en cada columna con el total de filas del dataset (**43,000 filas**). Las columnas con menos de 43,000 valores no nulos contienen valores nulos que deberán ser tratados antes del análisis.

#### Ejemplo:
Algunas de las columnas con valores nulos identificadas son:
- `age`: 37,880 valores no nulos (**5,120 nulos**).
- `education`: 41,193 valores no nulos (**1,807 nulos**).
- `default`: 34,019 valores no nulos (**8,981 nulos**).


## Progreso del Proyecto

### Transformación del Dataset

1. **Copia del dataset**  
   Para proteger el dataset original, se creó una copia utilizando el método `.copy()` de pandas.

2. **Renombrar columnas**  
   Se renombraron columnas clave para mejorar la legibilidad utilizando el método `.rename()` de pandas.

3. **Eliminación de columna innecesaria**  
   Se eliminó la columna `Unnamed: 0` utilizando el método `.drop()` para mantener el dataset limpio y organizado.

4. **Guardado del dataset transformado**  
   La copia transformada fue guardada en formato `.csv` en la carpeta correspondiente `data/transformation/` bajo el nombre `bank-transformed.csv`, manteniendo la organización del proyecto.

### Creación de la función `eda_preliminar`

Se creó una función llamada `eda_preliminar` que automatiza el análisis exploratorio inicial del dataset. Esta función realiza las siguientes tareas:

- Muestra una muestra aleatoria de los datos utilizando `.sample()`.
- Proporciona información general sobre el dataset mediante `.info()`.
- Calcula y muestra el porcentaje de valores nulos por columna.
- Identifica la presencia de filas duplicadas.
- Lista las columnas categóricas (tipo `object`).
- Cuenta los valores únicos en cada columna categórica utilizando `.value_counts()`.

La función fue probada inicialmente en el archivo `notebooks/eda_preliminar.ipynb` y luego trasladada al script `src/sp_limpieza.py` para facilitar su reutilización en otros análisis.

### Información obtenida con la función `eda_preliminar`

El análisis preliminar reveló las siguientes características del dataset:

- **Valores nulos**  
  Se identificaron las siguientes columnas con valores nulos significativos:
  - `age`: **11.91%** (5,120 nulos).
  - `education`: **4.20%** (1,807 nulos).
  - `default`: **20.89%** (8,981 nulos).
  - `euribor3m`: **21.53%** (9,256 nulos).
  
  Otras columnas tienen un porcentaje menor de nulos o están completas.

- **Tipo de datos**  
  El dataset contiene una mezcla de datos numéricos (`int64`, `float64`) y categóricos (`object`), lo que requiere un tratamiento diferenciado en análisis posteriores.

- **Datos categóricos**  
  Las columnas `job`, `marital` y `education` tienen categorías bien definidas.  
  Algunas columnas como `cons.price.idx` y `cons.conf.idx` contienen valores que deberían ser numéricos pero están almacenados como `object`.

### Creación de funciones para limpieza de datos

Se creó un script `sp_limpieza.py` dentro de la carpeta `src` que automatiza la limpieza de las siguientes columnas:

- **Columna `age`**:
  - Los valores nulos (5,120) fueron reemplazados por la **media** de la columna.
  - La columna fue convertida de `float` a `int` para el análisis.

- **Columna `education`**:
  - Se unificaron las categorías `basic.4y`, `basic.6y`, y `basic.9y` en una sola categoría llamada `basic`.
  - Se sustituyeron los valores nulos por `'sin especificar'`.

- **Columna `marital`**:
  - Se verificó que todos los valores en la columna estuvieran en minúsculas para mantener la consistencia.

- **Otras transformaciones**:
  - Se limpiaron las columnas `cons.price.idx` y `cons.conf.idx` eliminando las comas, para asegurar que se almacenen como valores numéricos.