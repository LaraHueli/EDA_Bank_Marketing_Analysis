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
        plt.show()
        plt.pause(0.1)  # Pausa breve para procesar cada gráfico
        plt.close('all')

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
    plt.show()
    plt.pause(0.1)  # Pausa breve para procesar cada gráfico
    plt.close()

def graficar_boxplots(df, columnas_numericas):
    """Genera boxplots para detectar outliers en columnas numéricas"""
    for col in columnas_numericas:
        plt.figure(figsize=(6, 4))
        sns.boxplot(data=df, x=col, palette="coolwarm");
        plt.title(f"Boxplot de {col}")
        plt.show()
        plt.pause(0.5)  # Pausa breve para procesar cada gráfico
        plt.close()

def graficar_histogramas(df, columnas_numericas):
    """Genera histogramas para visualizar la distribución de variables numéricas"""
    for col in columnas_numericas:
        plt.figure(figsize=(6, 4))
        sns.histplot(df[col], bins=30, kde=True, color="blue");
        plt.title(f"Histograma de {col}")
        plt.show()
        plt.pause(0.5)  # Pausa breve para procesar cada gráfico
        plt.close()