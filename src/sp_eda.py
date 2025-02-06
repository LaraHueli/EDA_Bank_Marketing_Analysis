import pandas as pd
import numpy as np

def calcular_nulos(df):
    numero_nulos = df.isnull().sum()
    porcentaje_nulos = (numero_nulos / df.shape[0]) * 100
    return numero_nulos, porcentaje_nulos



def calcular_porcentaje_nulos(df):
    porcentaje_nulos = df.isnull().sum() / df.shape[0] * 100
    return porcentaje_nulos  # Devuelve el resultado

def analisis_general_cat(df):
    col_catg = df.select_dtypes(include="object").columns  # Selecciona columnas categóricas

    if len(col_catg) == 0:
        print("No hay columnas categóricas en el DataFrame.")
    else:
        for col in col_catg:
            print(f"\n--- Análisis de la columna: {col.upper()} ---")
            print(f"Esta columna tiene {len(df[col].unique())} valores únicos.\n")
            display(df[col].value_counts(normalize=True))  # Muestra distribución de valores
            display(df[col].describe())  # Resumen descriptivo de la columna categórica
            print("\n--------------------------------------")
    print("\n📊 **Resumen Estadístico General:**")
    display(df.describe(include="all").T)  # 🔥 Agrega esta línea para ver todas las columnas

