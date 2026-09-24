import numpy as np
import pandas as pd

temp=pd.Series([1,1,2,2,3,2,3,4,4,5])
a=temp.duplicated().sum()

print(a)