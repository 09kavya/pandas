import numpy as np
import pandas as pd

a=pd.read_csv(r'C:\Users\Lenovo\Downloads\subs.csv')
b=a['Subscribers gained']
for i in b:
    print(i)