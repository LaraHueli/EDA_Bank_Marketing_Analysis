
import pandas as pd


def eda_preliminar(df):
    display(df.sample(5))
    
    print('--------------------------------------------------------------')
    
    print('INFO')   
    
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
    
    print('VALUE COUNTS')
    
    for columns in df.select_dtypes(include='object').columns:
        print(df[columns].value_counts())
        print('--------------------------------------------------------------')
        
        
def valores_minuscula(df):
    """Convierte todas las columnas de tipo objeto a minúsculas."""
    for col in df.select_dtypes(include="object").columns:
        df[col] = df[col].str.lower()
    return df

def reemplazar_nulos(df, columna, valor="sin especificar"):
    """Reemplaza los valores nulos de una columna por un valor específico."""
    df[columna] = df[columna].fillna(valor)
    return df

def unificar_education(df):
    """Unifica las categorías en la columna 'education'."""
    df['education'] = df['education'].replace(['basic.4y', 'basic.6y', 'basic.9y'], 'basic')
    df['education'] = df['education'].fillna('sin especificar')
    return df

def unificar_categorias(df, columna, categorias_antiguas, nueva_categoria):
    """Unifica varias categorías de una columna en una nueva categoría."""
    df[columna] = df[columna].replace(categorias_antiguas, nueva_categoria)
    return df

def eliminar_columnas(df, columnas):
    """Elimina columnas no relevantes del DataFrame."""
    df = df.drop(columns=columnas)
    return df

def convertir_float_a_int(df, columnas):
    """Convierte varias columnas de tipo float a int, reemplazando nulos por 0."""
    for columna in columnas:
        df[columna] = df[columna].fillna(0).astype(int)
    return df
        