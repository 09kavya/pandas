# 2. find month by month revenue
import numpy as np
import pandas as pd
courses=pd.read_csv(r"C:\Users\Lenovo\Downloads\courses.csv")
regs=pd.read_csv(r"C:\Users\Lenovo\Downloads\reg-month1.csv")
reg=pd.read_csv(r"C:\Users\Lenovo\Downloads\reg-month2.csv")

a=pd.concat([regs,reg],keys=['nov','dec']).reset_index()

revenue=a.merge(courses,on='course_id').groupby('level_0')['price'].sum()
print(revenue)