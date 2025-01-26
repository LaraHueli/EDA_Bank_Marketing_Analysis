
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