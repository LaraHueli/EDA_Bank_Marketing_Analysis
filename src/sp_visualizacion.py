import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import math

def graficar_categoricas(df):
    """Genera gráficos de barras para todas las columnas categóricas sin limitación de categorías."""
    # Seleccionamos solo columnas categóricas, excluyendo 'id' si existe
    categorical_cols = [col for col in df.select_dtypes(include=['object']).columns if col != 'id']

    for col in categorical_cols:
        plt.figure(figsize=(10, 5))

        # Reemplazar valores nulos para evitar errores
        df[col] = df[col].fillna("desconocido")

        sns.countplot(data=df, x=col, palette="viridis",
                      order=df[col].value_counts().index)  # Mostrar todas las categorías

        plt.title(f"Distribución de {col}")
        plt.xticks(rotation=45)
        plt.show()  # Mostrar cada gráfico antes de pasar al siguiente
        

def graficar_poutcome_vs_y(df):
    """Grafica la relación entre `poutcome` y `y`"""
    tabla_frecuencia = pd.crosstab(df['poutcome'], df['y'], normalize='index')
    
    plt.figure(figsize=(8,5))
    sns.barplot(x=tabla_frecuencia.index, y=tabla_frecuencia['yes'], color='royalblue', label='Sí (y = 1)')
    sns.barplot(x=tabla_frecuencia.index, y=tabla_frecuencia['no'], color='lightgrey', label='No (y = 0)')
    plt.legend()
    plt.title("Relación entre `poutcome` y `y`")
    plt.xlabel("poutcome")
    plt.ylabel("Proporción de `y`")
    plt.xticks(rotation=45)
    plt.show(block=True)
    plt.pause(0.1)  # Pausa breve para procesar cada gráfico
    plt.close()

def graficar_boxplots(df):
    """Genera boxplots para detectar outliers en columnas numéricas, mostrando dos gráficos por fila"""
    
    num_cols = df.select_dtypes(include=['number']).columns
    total_cols = len(num_cols)
    
    filas = math.ceil(total_cols / 2)  # Definir cuántas filas se necesitan
    
    fig, axes = plt.subplots(filas, 2, figsize=(12, filas * 4))  # Dos gráficos por fila
    axes = axes.flatten()  # Convertir a un solo array para iterar

    for i, col in enumerate(num_cols):
        sns.boxplot(data=df, x=df[col], ax=axes[i], color="royalblue",
                    flierprops={'marker': 'o', 'markerfacecolor': 'red', 'markersize': 5})
        axes[i].set_title(f"Boxplot de {col}", fontsize=12)
        axes[i].grid(True, linestyle="--", alpha=0.7)

    # Ocultar gráficos vacíos si hay un número impar de columnas
    for j in range(i + 1, len(axes)):
        fig.delaxes(axes[j])

    plt.tight_layout()
    plt.show()

def graficar_histogramas(df, columnas_numericas):
    """Genera histogramas para visualizar la distribución de variables numéricas"""
    for col in columnas_numericas:
        plt.figure(figsize=(6, 4))
        sns.histplot(df[col], bins=30, kde=True, color="blue");
        plt.title(f"Histograma de {col}")
        plt.show(block=True)
        plt.pause(0.5)  # Pausa breve para procesar cada gráfico
        plt.close()
        
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

def graficar_numericas(df, columna=None):
    
    if columna:
        # Graficar solo una columna en un solo subplot
        fig, ax = plt.subplots(1, 1, figsize=(7, 4))
        sns.histplot(df[columna], kde=True, bins=25, ax=ax, color='royalblue', edgecolor='black', alpha=0.6)
        
        # Líneas de media y mediana
        media = df[columna].mean()
        mediana = df[columna].median()
        ax.axvline(media, color='red', linestyle='--', label=f'Media: {media:.2f}')
        ax.axvline(mediana, color='green', linestyle='-', label=f'Mediana: {mediana:.2f}')
        
        ax.set_title(f'Distribución de {columna}', fontsize=12)
        ax.set_xlabel(columna, fontsize=10)
        ax.set_ylabel('Frecuencia', fontsize=10)
        ax.legend(fontsize=9)
        ax.grid(axis='y', linestyle='--', alpha=0.7)
        
        plt.tight_layout()
        plt.show()
        return
    
    # Si no se especifica columna, graficar todas las columnas numéricas en subplots
    columnas_numericas = df.select_dtypes(include=np.number).columns
    num_columnas = len(columnas_numericas)
    filas = (num_columnas // 2) + (num_columnas % 2)  # 2 gráficos por fila

    fig, axes = plt.subplots(filas, 2, figsize=(12, filas * 3.5))  
    axes = axes.flatten()  

    for i, col in enumerate(columnas_numericas):
        sns.histplot(df[col], kde=True, bins=25, ax=axes[i], color='royalblue', edgecolor='black', alpha=0.6)
        
        # Líneas de media y mediana
        media = df[col].mean()
        mediana = df[col].median()
        axes[i].axvline(media, color='red', linestyle='--', label=f'Media: {media:.2f}')
        axes[i].axvline(mediana, color='green', linestyle='-', label=f'Mediana: {mediana:.2f}')
        
        axes[i].set_title(f'Distribución de {col}', fontsize=10)
        axes[i].set_xlabel(col, fontsize=9)
        axes[i].set_ylabel('Frecuencia', fontsize=9)
        axes[i].legend(fontsize=8)
        axes[i].grid(axis='y', linestyle='--', alpha=0.7)

    # Ocultar ejes vacíos si hay un número impar de columnas
    for j in range(i + 1, len(axes)):
        fig.delaxes(axes[j])

    plt.tight_layout()  
    plt.show()
    
   