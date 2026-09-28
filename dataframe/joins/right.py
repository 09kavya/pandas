import numpy as np
import pandas as pd

students=pd.read_csv(r"C:\Users\Lenovo\Downloads\students.csv")
temp_df = pd.DataFrame({
    'student_id':[26,27,28],
    'name':['Nitish','Ankit','Rahul'],
    'partner':[28,26,17]
})
students=pd.concat([students,temp_df],ignore_index=True)
nov=pd.read_csv(r"C:\Users\Lenovo\Downloads\reg-month1.csv")
dec=pd.read_csv(r"C:\Users\Lenovo\Downloads\reg-month2.csv")
regs = pd.concat([nov,dec],ignore_index=True)
a=students.merge(regs,how='right',on='student_id')
print(a.tail())