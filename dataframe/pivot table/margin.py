
import seaborn as sns
import pandas as pd
import  numpy as np

df=sns.load_dataset('tips')
a=df.pivot_table(index=['sex','smoker'],columns=['day','time'],margins=True)
print(a)              
