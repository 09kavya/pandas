import numpy as np
import pandas as pd


a=pd.MultiIndex.from_product([['cse', 'ece'], [2019, 2020, 2021, 2022, 2023, 2024]])
b=pd.Series([1,2,3,4,5,6,7,8,9,10,11,12],index=a )

print(b.unstack())
