import numpy as np
import pandas as pd

a=pd.read_csv(r'C:\Users\Lenovo\Downloads\subs.csv')
print(a)

b=a.min()
print(b)
b=a.max()
print(b)