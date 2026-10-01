import numpy as np
import pandas as pd


index_val=[('cse',2019),('cse',2020),('cse',2021),('cse',2022),('cse',2023),('cse',2024),('ece',2019),('ece',2020),('ece',2021)]
a=pd.MultiIndex.from_tuples(index_val)
b=a.levels
print(b)