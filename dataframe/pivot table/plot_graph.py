
import seaborn as sns
import pandas as pd
import  numpy as np
import matplotlib.pyplot as plt

df=pd.read_csv(r"C:\Users\Lenovo\Downloads\expense_data.csv")
df['Date']=pd.to_datetime(df['Date'])
df['Month']=df['Date'].dt.month_name()
a=df.pivot_table(index='Month',columns='Category',values='INR',aggfunc='sum',fill_value=0).plot(kind='line')
plt.show()

# print(a)              
a=df.pivot_table(index='Month',columns='Income/Expense',values='INR',aggfunc='sum',fill_value=0).plot(kind='line')
plt.show()
a=df.pivot_table(index='Month',columns='Account',values='INR',aggfunc='sum',fill_value=0).plot(kind='line')
plt.show()

