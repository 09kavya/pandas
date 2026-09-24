import numpy as np
import pandas as pd

sub=pd.read_csv(r"C:\Users\Lenovo\Downloads\subs.csv")
a=sub.clip(100,200)
print(a)