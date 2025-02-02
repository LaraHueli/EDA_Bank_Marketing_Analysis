# 📊 Análisis de Marketing Bancario

## 📌 Descripción
Este proyecto realiza un análisis exploratorio de datos para entender los patrones de comportamiento de los clientes bancarios. Su objetivo es identificar factores clave que influyen en las campañas de marketing.

### 📌 **1️⃣ Primera sesión: Configuración inicial**

1. **Creación del repositorio en GitHub** y organización del entorno de trabajo.
2. **Estructura de carpetas y archivos** (`.gitignore`, `venv`, `requirements.txt`).
3. **Carga de datos brutos** en la carpeta `data/`.
4. **Importación de librerías** necesarias para el análisis (`pandas`, `numpy`).

## 📂 Estructura de las carpetas del Proyecto
```
📁 data/         # Datos crudos y procesados
📁 notebooks/    # Notebooks de Jupyter con el análisis
📁 src/          # Scripts de procesamiento
📁 results/      # Gráficos y conclusiones
📄 README.md     # Descripción del proyecto
```

## 🛠 Requerimientos
Este proyecto utiliza **Python 3.8** y requiere las siguientes bibliotecas:
- `pandas`
- `numpy`
- `jupyter`


---  


### 📌 **2️⃣ Segunda sesión: Exploración Preliminar de Datos (EDA Preliminar)**

#### 🔍 **Estudio previo de combinación de tablas**
Antes de comenzar el análisis de `bank-additional` y `customer-details`, evaluamos la posible fusión de las tablas mediante la columna `id_`.

- **Análisis de los resultados**:
  - `bank-additional` contiene **20,108 ID únicos**, mientras que `customer-details` tiene **20,115 ID**.
  - Existen **7 ID en `customer-details`** que no están en `bank-additional`.
  - Los datos de `customer-details` contienen información adicional como `income`, `teenhome`, `dt_customer`, etc.
  
- **Conclusión**: Dado que la fusión genera **demasiados valores nulos (`NaN`)**, decidimos **trabajar con los datasets por separado**.


#### 🔍 **Descripción de las columnas**
Este dataset contiene información bancaria y variables macroeconómicas relacionadas con clientes y campañas de marketing. A continuación, se detalla cada columna:

| **Columna**          | **Descripción**                                                                |
|----------------------|--------------------------------------------------------------------------------|
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

#### 📊 **Dimensiones e información del dataset**
El dataset contiene **43,000 filas** y **24 columnas**. A continuación, se detalla la información clave sobre los tipos de datos y los valores no nulos de cada columna:

| **Columna**       | **Tipo de dato** | **Valores no nulos** | **Descripción**                                                        |
|-------------------|------------------|----------------------|----------------------------------------------------------------------- |
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
- **Número de filas**: 43,000
- **Número de columnas**: 24
 
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
 
 
 ### Transformación del Dataset
 **Copia del dataset**  
   Para proteger el dataset original, se creó una copia utilizando el método `.copy()` de pandas.
**Eliminación de columnas innecesarias**  
   Se eliminó la columna `Unnamed: 0` que no aportaba valor al análisis.


### 📌 **3️⃣ Tercera sesión: Transformación del Dataset**

### 🔍 Creación de la función `eda_preliminar`
Como primer paso en la limpieza de datos, hemos desarrollado la función `eda_preliminar`, la cual nos permite obtener una visión general del dataset. Esta función realiza las siguientes tareas:

- Muestra una muestra aleatoria (`sample(5)`) para observar algunos registros.
- Presenta información detallada sobre las columnas (`info()`), incluyendo tipos de datos y valores no nulos.
- Calcula el porcentaje de valores nulos (`isnull()`).
- Verifica si hay filas duplicadas (`duplicated()`).
- Identifica las columnas categóricas (`select_dtypes(include='object')`).
- Muestra la distribución de valores (`value_counts()`) en las variables categóricas.

## 📊 Resultados del `eda_preliminar`

### 1️⃣ Tipos de datos inconsistentes
- Algunas columnas que deberían ser **numéricas** (`float64` o `int64`) están siendo interpretadas como **object** (string en Pandas).
- **Ejemplos**: `cons_price_idx`, `cons_conf_idx` y `nr_employed` deberían ser `float64`, pero Pandas las considera `object`.
- 🔹 **Acción a tomar**: Revisar y corregir el formato, eliminando posibles caracteres extraños (como comas en los números).

### 2️⃣ Valores nulos (`isnull()`)
#### Las columnas con más valores nulos:
- `default`: **20.89%** de valores nulos.
- `euribor3m`: **21.53%** de valores nulos.
- 🔹 **Acción a tomar**: Decidir cómo tratarlos (imputación con media, mediana o eliminación de filas).

### 3️⃣ Filas duplicadas (`duplicated()`)
- **No hay filas duplicadas** en el dataset, lo cual es positivo. ✅

### 4️⃣ Distribución de valores (`value_counts()`)
#### **Columna `job`**:
- **Categoría más común**: `admin.` con **10,873 registros**.
- **Categoría menos común**: `student` con **903 registros**.

#### **Columna `marital`**:
- **Mayoría de clientes casados (`MARRIED`)**.
- **Menos frecuentes**: `SINGLE` y `DIVORCED`.

#### **Columna `education`**:
- **Mayoría de clientes con título universitario (`university.degree`)**.
- **Las categorías `basic.4y`, `basic.6y`, `basic.9y` son similares y podrían unificarse en una sola (`basic`).**

---

## 🔄 Limpieza y Preprocesamiento de Datos

### 1️⃣ Conversión de valores a minúsculas  
Se estandarizaron los valores de las siguientes columnas para evitar inconsistencias en las categorías:  
- **`job`**, **`marital`**, **`contact`**, **`education`**.

### 2️⃣ Unificación de categorías  
- En **`education`**, las categorías **`basic.4y`**, **`basic.6y`**, y **`basic.9y`** fueron unificadas en **`basic`** para simplificación.  
- Se corrigieron inconsistencias en **`poutcome`** para garantizar uniformidad.  

### 3️⃣ Eliminación de columnas irrelevantes  
- Se eliminaron **`latitude`** y **`longitude`** por no aportar valor relevante al análisis.  
- Se eliminó **`date`** tras extraer **`year`**, **`month`** y **`day`** como variables separadas.

### 4️⃣ Transformación de tipos de datos  
Se realizaron las siguientes conversiones para asegurar consistencia en los datos:  
- **`age`**, **`housing`**, **`loan`** fueron convertidos de `float` a `int`.  
- **`cons_price_idx`**, **`cons_conf_idx`**, **`euribor3m`**, **`nr_employed`** fueron convertidos de `object` a `float`.

### 5️⃣ Reemplazo de valores nulos  
Se manejaron los valores nulos en varias columnas importantes:  
- **`education`**, **`job`**, y **`marital`** → reemplazados por `'sin especificar'`.  
- **`age`** → valores nulos reemplazados con la **mediana**.  
- **`euribor3m`** → valores nulos imputados con la **media**.  
- **`default`** → sigue teniendo un 20.89% de valores nulos, pendiente de tratamiento.

### 6️⃣ Revisión de variables categóricas  
Se verificó que las variables categóricas estuvieran limpias y en formato adecuado.  
- **`poutcome`**, **`job`**, **`marital`**, **`education`** → valores corregidos y en minúsculas para coherencia.

### 💾 Guardado del dataset transformado  
- Se guardó el dataset limpio en la carpeta **`data/`** con el nombre:  
  - **`bank_limpio.csv`**