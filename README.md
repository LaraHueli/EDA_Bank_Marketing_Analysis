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
  - `bank-additional` contiene **43,000 filas**, mientras que `customer-details` tiene **20,115**.
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

### 5️⃣ El Reemplazo de valores nulos se daje para mas adelante  
Se manejaran los valores nulos en varias columnas importantes:  
- **`education`**, **`job`**, y **`marital`** → reemplazados por `'unknown'`.  
- **`age`** → los valores nulos se dejan como Nan de momento.  
- **`euribor3m`** los valores nulos se dejan como Nan de momento.  
- **`default`** → sigue teniendo un 20.89% de valores nulos, pendiente de tratamiento.

### 6️⃣ Revisión de variables categóricas  
Se verificó que las variables categóricas estuvieran limpias y en formato adecuado.  
- **`poutcome`**, **`job`**, **`marital`**, **`education`** → valores corregidos y en minúsculas para coherencia.
- Aunque la columna poutcome debe ser eliminada en un futuro

### 💾 Guardado del dataset transformado  
- Se guardó el dataset limpio en la carpeta **`data/`** con el nombre:  
  - **`bank_limpio.csv`**

## 🔍 Análisis de Columnas Categóricas

###  Creación del script `sp_eda.py`
Se creó un script en la carpeta **`src/`** llamado **`sp_eda.py`**, donde se almacenan funciones reutilizables para el análisis exploratorio de datos.

#### 📌 **Funciones creadas en `sp_eda.py`**:
1. **`calcular_nulos(df)`** ➝ Calcula el número y porcentaje de valores nulos en cada columna.
   ```python
   def calcular_nulos(df):
       numero_nulos = df.isnull().sum()
       porcentaje_nulos = (df.isnull().sum() / df.shape[0]) * 100
       return numero_nulos, porcentaje_nulos
---

## 🔎 Análisis de Datos

### 🔹 **Gestión de Valores Nulos**
Se identificaron y gestionaron valores nulos en columnas categóricas clave:

| Columna   | Valores Nulos | Método de Imputación |
|-----------|--------------|----------------------|
| `job`     | 1.95%        | Rellenado con `"unknown"` |
| `marital` | 0.20%        | Rellenado con `"unknown"` |
| `education` | 4.20%      | Rellenado con `"unknown"` |

El código implementado para esta transformación se encuentra en `sp_limpieza.py`, con la función `rellenar_nulos_categoricas(df, columnas)`, aplicada en `columnas_categoricas.ipynb` antes de generar las visualizaciones.

---

### 📊 **Visualización de Datos Categóricos**
Se generaron gráficos de barras para cada columna categórica tras la limpieza de datos. Ahora incluyen la categoría `"unknown"` en los casos donde se imputaron valores nulos.

- **`job`** → 12 categorías (se agregó `"unknown"`)
- **`marital`** → 4 categorías (se agregó `"unknown"`)
- **`education`** → 6 categorías (se agregó `"unknown"`)

Los gráficos se encuentran en `columnas_categoricas.ipynb` y fueron generados con la función `graficar_categoricas(df)`, ubicada en `sp_visualizacion.py`.


### 📌 **4️⃣ Análisis Preliminar de Columnas Numéricas**

#### 🔢 **Exploración de las columnas numéricas**
Se realizó un análisis exploratorio sobre las columnas numéricas, examinando su distribución, valores atípicos y diferencias entre medidas de tendencia central.

- Se calcularon estadísticas descriptivas usando:
  ```python
  df.describe().T

- Se identificaron columnas con alta dispersión entre la media y la mediana.
- Se visualizaron histogramas y boxplots para detectar outliers en variables clave.

**Boxplots y distribución de los datos**
- Para identificar valores atípicos en las variables numéricas, se crearon gráficos de caja (boxplots), lo que permitió:

- Detectar columnas con valores extremos, como duration y campaign.

## 🔹 Gestión de valores nulos

Se realizó un análisis de valores nulos en el dataset y se tomaron las siguientes decisiones:

✅ **Sustitución de nulos en columnas numéricas**:
   - `age` → **Sustituido por la mediana** (38.0).
   - `duration` → **Sustituido por la mediana** (179.0).
   - Resto de columnas numéricas **se mantienen con NaN** para futuras decisiones.

✅ **Sustitución de nulos en columnas categóricas**:
   - Se reemplazaron valores nulos en variables categóricas con `'unknown'` para evitar la pérdida de información.

Los cambios fueron implementados en el script `src/sp_limpieza.py` dentro de la función `rellenar_nulos_numericas`.



**Comparación de correlaciones**
Correlaciones entre Variables

✅ Calculamos la matriz de correlaciones entre las variables numéricas.
✅ Identificamos relaciones destacadas como:

emp_var_rate y euribor3m con una correlación de 0.82, lo que indica una fuerte relación entre estas variables.

campaign y previous tienen una correlación muy baja, lo que sugiere que las interacciones previas con clientes no afectan significativamente el número de intentos en la campaña actual.

 **Outliers (Valores Atípicos)**

✅ Identificamos outliers en varias columnas, especialmente en duration, campaign y pdays.
✅ No eliminamos los outliers, ya que podrían representar información valiosa para el análisis.
✅ Mencionamos en el informe que, en futuros análisis, se puede considerar tratarlos dependiendo del enfoque del negocio.

**Observaciones y Próximos Pasos**
Algunas variables presentan alta correlación.
Se encontraron valores atípicos en duration y campaign, lo que requerirá un tratamiento especial.
El análisis de outliers y su impacto en el modelo será evaluado en sesiones posteriores.

** Conclusiones principales:**
✅ La duración de la última campaña (duration) presenta una gran variabilidad y valores extremos.
✅ Algunas variables presentan correlaciones fuertes, lo que puede ayudar a definir estrategias de segmentación de clientes.
✅ La presencia de outliers indica que existen casos excepcionales que podrían analizarse con más detalle.

El dataset actualizado sigue estando disponible como bank_limpio.csv en la carpeta data/.
---



### 💾 **Guardado de Datos**
El dataset limpio y procesado se guardó en la carpeta `data` bajo el nombre `bank_limpio.csv`.  

```python
df_limpio.to_csv("../data/bank_limpio.csv", index=False)
