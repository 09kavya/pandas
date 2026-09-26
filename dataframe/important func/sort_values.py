#work in series and df

import numpy as np
import pandas as pd

x=pd.DataFrame([10,72,12,39,2,68,99])
movie=pd.read_csv(r"C:\Users\Lenovo\Downloads\movies.csv")
y=x.sort_values(by=0)
print(y)
sort=movie.sort_values('title_x',ascending=False)
print(sort)