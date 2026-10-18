import numpy as np
import pandas as pd

df= pd.read_csv(r"C:\Users\Lenovo\Downloads\titanic.csv")
# a=df['Name'].str.split(',').str.get(0)
# print(a)


a=df['Name'].str.split(',').str.get(1).str.strip().str.split(' ',n=1,expand=True)
print(a.head())