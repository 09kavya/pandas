#count no. of day when I had more than 200 subs a day

import numpy as np
import pandas as pd

a=pd.read_csv(r'C:\Users\Lenovo\Downloads\subs.csv')
b=a[a>=200].count()
print(b)