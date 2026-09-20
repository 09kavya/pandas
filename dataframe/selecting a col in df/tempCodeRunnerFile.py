import numpy as np
import pandas as pd

a=pd.read_csv(r"C:\Users\Lenovo\Downloads\movies.csv")
print(a)
print(a['title_x','year_of_release','actors'])