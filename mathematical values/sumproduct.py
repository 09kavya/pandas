import numpy as np
import pandas as pd

a=pd.read_csv(r'C:\Users\Lenovo\Downloads\subs.csv')
print(a)
b=a.sum()
print(b)
b=a.product()
print(b)