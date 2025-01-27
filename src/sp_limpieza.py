
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

def convertir_int_a_float(df, columna):
    # Reemplaza comas por puntos y convierte de int a float.
    df[columna] = df[columna].str.replace(',', '.').astype(float)
    return df

def limpiar_columnas(df):
    # Limpiar las columnas 'cons.price.idx' 'euribor3m'  'nr.employed' y 'cons.conf.idx', y convertirlas a float
    df['cons.price.idx'] = df['cons.price.idx'].str.replace(',', '').astype(float)
    df['cons.conf.idx'] = df['cons.conf.idx'].str.replace(',', '').astype(float)
    df['euribor3m'] = df['euribor3m'].str.replace(',', '').astype(float)
    df['nr.employed'] = df['nr.employed'].str.replace(',', '').astype(float)
    return df


def convertir_fecha(df, columna='date'):
   #Convierte una columna de fechas a tipo datetime y extrae los componentes: año, mes, día.
    df[columna] = pd.to_datetime(df[columna], errors='coerce', format='%d-%B-%Y')
        # Crear nuevas columnas de 'year', 'month' y 'day' a partir de 'date'
    df['year'] = df[columna].dt.year.fillna(0).astype(int)
    df['month'] = df[columna].dt.month.fillna(0).astype(int)
    df['day'] = df[columna].dt.day.fillna(0).astype(int)
    return df

        