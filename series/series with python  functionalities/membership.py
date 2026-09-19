import numpy as np
import pandas as pd

a=pd.read_csv(r"C:\Users\Lenovo\Downloads\bollywood.csv",index_col="movie")

print('Uri: The Surgical Strike  ' in a.index)
b='Shah Rukh Khan' in a.values
print(b)