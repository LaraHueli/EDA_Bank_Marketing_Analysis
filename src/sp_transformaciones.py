import pandas as pd
from sklearn.preprocessing import OneHotEncoder, LabelEncoder

def aplicar_one_hot_encoding(df, columnas):
    """
    Aplica One-Hot Encoding a las columnas especificadas y devuelve un nuevo DataFrame con las transformaciones aplicadas.
    """
    encoder = OneHotEncoder(sparse=False, drop='first')  # Elimina la primera categoría para evitar colinealidad
    encoded = encoder.fit_transform(df[columnas])
    col_names = encoder.get_feature_names_out(columnas)
    df_encoded = pd.DataFrame(encoded, columns=col_names)
    df = df.drop(columns, axis=1).reset_index(drop=True)
    df = pd.concat([df, df_encoded], axis=1)
    return df

def aplicar_label_encoding(df, columna):
    """
    Aplica Label Encoding a una columna específica y devuelve el DataFrame modificado.
    """
    encoder = LabelEncoder()
    df[columna] = encoder.fit_transform(df[columna])
    return df

if __name__ == "__main__":
    # Cargar datos limpios
    df = pd.read_csv("../data/bank_limpio.csv")
    
    # Aplicar One-Hot Encoding a variables categóricas
    columnas_categoricas = ['job', 'marital', 'education']
    df = aplicar_one_hot_encoding(df, columnas_categoricas)
    
    # Aplicar Label Encoding a la variable objetivo 'y'
    df = aplicar_label_encoding(df, 'y')
    
    # Guardar el dataset transformado
    df.to_csv("../data/bank_transformed.csv", index=False)
    print("Transformaciones aplicadas y guardadas en bank_transformed.csv")
