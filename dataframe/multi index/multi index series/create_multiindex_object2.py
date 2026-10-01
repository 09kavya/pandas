import numpy as np
import pandas as pd


a=pd.MultiIndex.from_product([['cse', 'ece'], [2019, 2020, 2021, 2022, 2023, 2024]])
b=a.levels
print(a)