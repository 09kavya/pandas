import numpy as np
import pandas as pd

month1=pd.read_csv(r"C:\Users\Lenovo\Downloads\reg-month1.csv")
month2=pd.read_csv(r"C:\Users\Lenovo\Downloads\reg-month2.csv")
a=pd.concat([month1,month2],ignore_index=True)
print(a)
