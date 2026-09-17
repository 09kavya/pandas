import numpy as np
import pandas as pd

a=pd.read_csv(r'C:\Users\Lenovo\Downloads\subs.csv')
print(a)
b=a.mean()
print(b)
b=a.median()
print(b)
b=a.std()
print(b)
b=a.mode()
print(b)
b=a.var()
print(b)