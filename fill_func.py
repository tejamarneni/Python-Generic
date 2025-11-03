import pandas as pd 
import numpy as np

def fill_func(file_name):
    df = pd.read_csv(file_name)
    cols = [col for col in df.columns if df[col].isnull().sum()>0]
    
    for col in cols:
        if df[col].dtype == 'object':
            df[col].fillna(df[col].mode()[0],inplace=True)
        else:
            df[col].fillna(int(df[col].mean()),inplace=True)

    f_name = input("The function is about to generate a new file.Enter the name of the new file:\n")        
    df.to_csv('C:/Users/tejam/Desktop/' + f_name + '.csv',index = False) 
        

fill_func('C:/Users/dummypth/train.csv')    

   
