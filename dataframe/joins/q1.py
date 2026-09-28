# 1. find total revenue generated
import numpy as np
import pandas as pd
courses=pd.read_csv(r"C:\Users\Lenovo\Downloads\courses.csv")
regs=pd.read_csv(r"C:\Users\Lenovo\Downloads\reg-month1.csv")
a=courses.merge(regs,how='inner',on='course_id')['price'].sum()
print(a)