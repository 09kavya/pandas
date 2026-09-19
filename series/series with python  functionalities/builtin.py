import numpy as np
import pandas as pd

a=pd.read_csv(r'C:\Users\Lenovo\Downloads\subs.csv')
b = a['Subscribers gained']
print(len(b))
print(type(b))
print(dir(b))
print(sorted(b))
print(min(b))
print(max(b))