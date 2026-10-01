import numpy as np
import pandas as pd


a=pd.MultiIndex.from_product([['cse', 'ece'], [2019, 2020, 2021, 2022]])
b=pd.DataFrame([
    [1,2],
    [3,4],
    [5,6],
    [7,8],
    [9,10],
    [11,12],
    [13,14],
    [15,16],
],index=a,columns=['Avg_package','students'])

print(b)
print(b.loc['cse'])
print(b['Avg_package'])
