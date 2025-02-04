
import pandas as pd
import numpy as np
# Configuración para mostrar todas las columnas
pd.set_option('display.max_columns', None)

def eda_preliminar(df):
    display(df.sample(5)) #Muestra una muestra aleatoria de 5 filas del DataFrame.
    
    print('--------------------------------------------------------------')
    
    print('INFO') # Muestra un resumen general del DataFrame, incluyendo:  filas y columnas, Tipos de datos y valores no nulos.
    
    display(df.info())
    
    print('--------------------------------------------------------------') 
       
    print('NULOS')  
    
    display(round(df.isnull().sum()/df.shape[0]*100,2))
            
    print('--------------------------------------------------------------')
    
    print('DUPLICADOS')  
    
    display(df.duplicated().sum())
    
    print('--------------------------------------------------------------')
    
    print('CATEGORIAS') 
    
    display(df.select_dtypes(include='object').columns)
    
    print('--------------------------------------------------------------')
    
    print('VALUE COUNTS') # Muestra la distribución de valores en cada columna categórica.
    
    for columns in df.select_dtypes(include='object').columns:
        print(df[columns].value_counts())
        print('--------------------------------------------------------------')
        
        
def valores_minuscula(df):
    """Convierte todas las columnas de tipo objeto a minúsculas, manejando valores nulos."""
    for col in df.select_dtypes(include="object").columns:
        df[col] = df[col].astype(str).str.lower()
    return df


def reemplazar_nulos(df, columna, valor='sin especificar'):
    """Reemplaza los valores nulos de una columna SOLO si es de tipo object."""
    if df[columna].dtype == 'object':  # Solo aplica a columnas categóricas
        df[columna] = df[columna].fillna(valor)
    else:
        print(f"⚠️ Advertencia: La columna '{columna}' no es de tipo 'object', no se reemplazó ningún valor.")
    return df


def unificar_education(df):
    """Unifica las categorías en la columna `education`."""
    df['education'] = df['education'].replace(['basic.4y', 'basic.6y', 'basic.9y'], 'basic')
    df['education'] = df['education'].fillna('sin especificar')  # Ya estaba esta línea
    df['education'] = df['education'].replace('nan', np.nan)  # 🚀 Nueva línea para corregir valores string 'nan'
    return df


def unificar_categorias(df, columna, categorias_antiguas, nueva_categoria): # Unifica varias categorías de una columna en una nueva categoría.
    """Unifica varias categorías de una columna en una nueva categoría."""
    df[columna] = df[columna].replace(categorias_antiguas, nueva_categoria)
    return df

def eliminar_columnas(df, columnas): # Elimina columnas no relevantes en el DataFrame
    """Elimina columnas no relevantes del DataFrame."""
    df = df.drop(columns=columnas)
    return df

def convertir_float_a_int(df, columnas):
    """Convierte varias columnas de tipo float a int, permitiendo valores nulos."""
    for columna in columnas:
        df[columna] = df[columna].astype('Int64')  # Usa 'Int64' para mantener nulos
    return df

def convertir_int_a_float(df, columna):  # Reemplaza comas por puntos y convierte de int a float.
    df[columna] = df[columna].str.replace(',', '.').astype(float)
    return df

def limpiar_columnas(df):
    """Convierte columnas categorizadas erróneamente a float eliminando caracteres extraños."""
    columnas_a_convertir = ['cons_price_idx', 'cons_conf_idx', 'euribor3m', 'nr_employed']
    for columna in columnas_a_convertir:
        df[columna] = df[columna].str.replace(',', '').astype(float)
    return df


def convertir_fecha(df, columna='date'):
   #Convierte una columna de fechas a tipo datetime y extrae los componentes: año, mes, día.
    df[columna] = pd.to_datetime(df[columna], errors='coerce', format='%d-%B-%Y')
        # Crear nuevas columnas de 'year', 'month' y 'day' a partir de 'date'
    df['year'] = df[columna].dt.year.fillna(0).astype(int)
    df['month'] = df[columna].dt.month.fillna(0).astype(int)
    df['day'] = df[columna].dt.day.fillna(0).astype(int)
    return df

        