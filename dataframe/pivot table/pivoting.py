import seaborn as sns
import pandas as pd
import  numpy as np

df=sns.load_dataset('tips')
a=df.pivot_table(index='sex',columns='smoker',values='total_bill')
print(a)              
