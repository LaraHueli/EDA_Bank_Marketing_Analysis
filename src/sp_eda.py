import pandas as pd
import numpy as np

def calcular_nulos(df):
    """
    Calcula el número total de valores nulos y su porcentaje en cada columna del DataFrame.

    Parámetros:
    df (pd.DataFrame): DataFrame de entrada.

    Retorna:
    tuple: DataFrame con el conteo de valores nulos por columna y su porcentaje.
    """
    numero_nulos = df.isnull().sum()
    porcentaje_nulos = (numero_nulos / df.shape[0]) * 100
    return numero_nulos, porcentaje_nulos


def calcular_porcentaje_nulos(df):
    """
    Calcula el porcentaje de valores nulos en cada columna del DataFrame.

    Parámetros:
    df (pd.DataFrame): DataFrame de entrada.

    Retorna:
    pd.Series: Serie con el porcentaje de valores nulos por columna.
    """
    porcentaje_nulos = df.isnull().sum() / df.shape[0] * 100
    return porcentaje_nulos


def analisis_general_cat(df):
    """
    Realiza un análisis exploratorio de las columnas categóricas del DataFrame.

    - Muestra la cantidad de valores únicos por cada columna categórica.
    - Presenta la distribución de valores mediante `value_counts()`.
    - Proporciona una descripción de las columnas categóricas.

    Parámetros:
    df (pd.DataFrame): DataFrame de entrada.

    Retorna:
    None
    """
    col_catg = df.select_dtypes(include="object").columns  # Selecciona columnas categóricas

    if len(col_catg) == 0:
        print("⚠ No hay columnas categóricas en el DataFrame.")
    else:
        for col in col_catg:
            print(f"\n--- Análisis de la columna: {col.upper()} ---")
            print(f"📌 La columna tiene {len(df[col].unique())} valores únicos.\n")
            display(df[col].value_counts(normalize=True))  # Muestra distribución de valores
            display(df[col].describe())  # Resumen descriptivo de la columna categórica
            print("\n------------------------------------")

    print("\n📊 **Resumen Estadístico General:**")
    display(df.describe(include="all").T)  # Resumen estadístico para todas las columnas
