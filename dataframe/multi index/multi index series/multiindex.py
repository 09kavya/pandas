import numpy as np
import pandas as pd


index_val=[('cse',2019),('cse',2020),('cse',2021),('cse',2022),('cse',2023),('cse',2024),('ece',2019),('ece',2020),('ece',2021)]
a=pd.Series([1,2,3,4,5,6,7,8,9],index=index_val)
print(a)