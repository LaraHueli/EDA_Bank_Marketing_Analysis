import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def graficar_categoricas(df):
    """Genera gráficos de barras para cada columna categórica"""
    categorical_cols = df.select_dtypes(include=['object']).columns

    for col in categorical_cols:
        plt.figure(figsize=(8, 4))
        sns.countplot(data=df, x=col, hue=col, palette="viridis", order=df[col].value_counts().index, legend=False);
        plt.title(f"Distribución de {col}")
        plt.xticks(rotation=45)
        plt.show(block=True)
        plt.pause(0.1)  # Pausa breve para procesar cada gráfico
        plt.close()

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

def graficar_boxplots(df, columnas_numericas):
    """Genera boxplots para detectar outliers en columnas numéricas"""
    for col in columnas_numericas:
        plt.figure(figsize=(6, 4))
        sns.boxplot(data=df, x=col, palette="coolwarm");
        plt.title(f"Boxplot de {col}")
        plt.show(block=True)
        plt.pause(0.5)  # Pausa breve para procesar cada gráfico
        plt.close()

def graficar_histogramas(df, columnas_numericas):
    """Genera histogramas para visualizar la distribución de variables numéricas"""
    for col in columnas_numericas:
        plt.figure(figsize=(6, 4))
        sns.histplot(df[col], bins=30, kde=True, color="blue");
        plt.title(f"Histograma de {col}")
        plt.show(block=True)
        plt.pause(0.5)  # Pausa breve para procesar cada gráfico
        plt.close()
        
def graficar_numericas(df, columna):
    """
    Crea un histograma + KDE para visualizar la distribución de una columna numérica.
    También añade líneas para la media y la mediana.

    Parámetros:
    - df: DataFrame que contiene la columna.
    - columna: str, nombre de la columna a visualizar.

    Retorna:
    - Gráfico de distribución.
    """
    plt.figure(figsize=(10, 5))
    
    # Histograma con KDE
    sns.histplot(df[columna], kde=True, bins=30, color='royalblue', edgecolor='black', alpha=0.6)
    
    # Líneas de media y mediana
    media = df[columna].mean()
    mediana = df[columna].median()
    
    plt.axvline(media, color='red', linestyle='--', label=f'Media: {media:.2f}')
    plt.axvline(mediana, color='green', linestyle='-', label=f'Mediana: {mediana:.2f}')
    
    # Títulos y leyenda
    plt.title(f'Distribución de {columna}', fontsize=14)
    plt.xlabel(columna)
    plt.ylabel('Frecuencia')
    plt.legend()
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    
    plt.show()