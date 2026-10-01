import numpy as np
import pandas as pd


a=pd.MultiIndex.from_product([['cse', 'ece'], [2019, 2020, 2021, 2022]])
b=pd.DataFrame([
    [1, 2, 0, 0],
    [3, 4, 4, 0],
    [5, 6, 3, 5],
    [7, 8, 5, 1],
    [2, 3, 1, 0],
    [4, 5, 3, 2],
    [6, 7, 4, 3],
    [8, 9, 6, 4]
],index=a,columns=pd.MultiIndex.from_product([['delhi','mumbai'],['Avg_package','students']]))

print(b.unstack().unstack())
