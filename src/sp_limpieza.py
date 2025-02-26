 #importaciones       
import pandas as pd
import numpy as np

# Configuración para mostrar todas las columnas
pd.set_option('display.max_columns', None)


def eda_preliminar(df):
    """
    Realiza un análisis exploratorio preliminar del DataFrame.
    
    Parámetros:
    df (pd.DataFrame): DataFrame a analizar.
    
    Retorno:
    None
    """
    print(df.sample(5))  # Muestra una muestra aleatoria de 5 filas
    print('\nINFO')
    print(df.info())
    print('\nNULOS')
    print(round(df.isnull().sum() / df.shape[0] * 100, 2))
    print('\nDUPLICADOS')
    print(df.duplicated().sum())
    print('\nCATEGORÍAS')
    print(df.select_dtypes(include='object').columns)
    print('\nVALUE COUNTS')
    for col in df.select_dtypes(include='object').columns:
        print(df[col].value_counts())
        print('------------------------------------------------------------')
 
  
def valores_minuscula(df):
    """
    Convierte todas las columnas categóricas a minúsculas para evitar inconsistencias.
    
    Parámetros:
    df (pd.DataFrame): DataFrame con columnas categóricas.
    
    Retorno:
    pd.DataFrame: DataFrame con los valores categóricos en minúsculas.
    """
    for col in df.select_dtypes(include='object').columns:
        df[col] = df[col].astype(str).str.lower()
    return df



def reemplazar_nulos(df, columna, valor='sin especificar'):
    """
    Reemplaza los valores nulos en una columna específica.
    
    Parámetros:
    df (pd.DataFrame): DataFrame a modificar.
    columna (str): Nombre de la columna en la que se reemplazarán los valores nulos.
    valor (str): Valor por el que se reemplazarán los nulos (por defecto 'sin especificar').
    
    Retorno:
    pd.DataFrame: DataFrame con los valores nulos reemplazados.
    """
    if df[columna].dtype == 'object':
        df[columna] = df[columna].fillna(valor)
    else:
        print(f"⚠️ Advertencia: La columna '{columna}' no es de tipo 'object', no se reemplazó ningún valor.")
    return df


def unificar_education(df):
    """
    Unifica categorías en la columna 'education'.
    
    Parámetros:
    df (pd.DataFrame): DataFrame con la columna 'education'.
    
    Retorno:
    pd.DataFrame: DataFrame con las categorías unificadas.
    """
    df['education'] = df['education'].replace(['basic.4y', 'basic.6y', 'basic.9y'], 'basic')
    df['education'] = df['education'].replace('nan', np.nan)
    return df



def unificar_categorias(df, columna, categorias_antiguas, nueva_categoria):
    """
    Unifica varias categorías dentro de una columna en una sola.
    
    Parámetros:
    df (pd.DataFrame): DataFrame con la columna a modificar.
    columna (str): Nombre de la columna a modificar.
    categorias_antiguas (list): Lista de categorías a unificar.
    nueva_categoria (str): Nuevo valor para las categorías unificadas.
    
    Retorno:
    pd.DataFrame: DataFrame con las categorías unificadas.
    """
    df[columna] = df[columna].replace(categorias_antiguas, nueva_categoria)
    return df



def eliminar_columnas(df, columnas):
    """
    Elimina columnas no relevantes del DataFrame.
    
    Parámetros:
    df (pd.DataFrame): DataFrame a modificar.
    columnas (list): Lista de columnas a eliminar.
    
    Retorno:
    pd.DataFrame: DataFrame sin las columnas eliminadas.
    """
    df = df.drop(columns=columnas)
    return df




def convertir_float_a_int(df, columnas):
    """
    Convierte columnas numéricas de tipo float a int.
    
    Parámetros:
    df (pd.DataFrame): DataFrame a modificar.
    columnas (list): Lista de columnas a convertir.
    
    Retorno:
    pd.DataFrame: DataFrame con las columnas convertidas a int.
    """
    for col in columnas:
        df[col] = df[col].astype('Int64')  # Mantiene NaN
    return df



def convertir_int_a_float(df, columna):
    """
    Convierte valores numéricos de tipo int a float, asegurando compatibilidad con decimales.
    
    Parámetros:
    df (pd.DataFrame): DataFrame a modificar.
    columna (str): Nombre de la columna a convertir.
    
    Retorno:
    pd.DataFrame: DataFrame con la columna convertida a float.
    """
    df[columna] = df[columna].str.replace(',', '.').astype(float)
    return df


def limpiar_columnas(df):
    """
    Convierte columnas categorizadas erróneamente a float eliminando caracteres extraños.
    
    Parámetros:
    df (pd.DataFrame): DataFrame a modificar.
    
    Retorno:
    pd.DataFrame: DataFrame con columnas corregidas.
    """
    columnas_a_convertir = ['cons_price_idx', 'cons_conf_idx', 'euribor3m', 'nr_employed']
    for columna in columnas_a_convertir:
        df[columna] = df[columna].str.replace(',', '').astype(float)
    return df



def forzar_age_a_int(df):
    """
    Convierte la columna 'age' a tipo 'Int64', permitiendo valores nulos.
    
    Parámetros:
    df (pd.DataFrame): DataFrame a modificar.
    
    Retorno:
    pd.DataFrame: DataFrame con la columna 'age' convertida a Int64.
    """
    df['age'] = df['age'].astype('Int64')  # 'Int64' permite NaN en pandas
    return df



def convertir_fecha(df, columna='date'):
    """
    Convierte la columna de fecha en tipo datetime y extrae los componentes de año, mes y día.
    
    Parámetros:
    df (pd.DataFrame): DataFrame a modificar.
    columna (str): Nombre de la columna con la fecha (por defecto 'date').
    
    Retorno:
    pd.DataFrame: DataFrame con las nuevas columnas 'year', 'month' y 'day'.
    """
    df[columna] = pd.to_datetime(df[columna], errors='coerce', format='%d-%b-%Y')
    df['year'] = df[columna].dt.year.fillna(0).astype(int)
    df['month'] = df[columna].dt.month.fillna(0).astype(int)
    df['day'] = df[columna].dt.day.fillna(0).astype(int)
    return df


def rellenar_nulos_categoricas(df, columnas):
    """
    Rellena los valores nulos en columnas categóricas con 'unknown'.
    
    Parámetros:
    df (pd.DataFrame): DataFrame a modificar.
    columnas (list): Lista de columnas categóricas a rellenar.
    
    Retorno:
    pd.DataFrame: DataFrame con valores nulos reemplazados por 'unknown'.
    """
    df[columnas] = df[columnas].fillna('unknown')
    return df

def rellenar_nulos_numericas(df, columnas):
    """
    Rellena los valores nulos de las columnas numéricas con la mediana.

    Parámetros:
    - df: DataFrame
    - columnas: Lista de columnas numéricas a rellenar

    Retorna:
    - DataFrame con los nulos reemplazados por la mediana
    """
    df = df.copy()  # Aseguramos que trabajamos con una copia y no con una vista
    for col in columnas:
        df.loc[:, col] = df[col].fillna(df[col].median())
    
    return df
        














