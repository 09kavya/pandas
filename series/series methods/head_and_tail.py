import numpy as np
import pandas as pd

a=pd.read_csv(r'C:\Users\Lenovo\Downloads\subs.csv')
print(a)
b=a.head(3)
print(b)
b=a.tail(10)
print(b)