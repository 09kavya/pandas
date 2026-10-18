import numpy as np
import pandas as pd


df= pd.read_csv(r"C:\Users\Lenovo\Downloads\titanic.csv")
a=df['Name'].str.strip()
print(a)