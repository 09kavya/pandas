# 8. Print student name -> partner name for all enrolled students

import numpy as np
import pandas as pd

courses=pd.read_csv(r"C:\Users\Lenovo\Downloads\courses.csv")
regs=pd.read_csv(r"C:\Users\Lenovo\Downloads\reg-month1.csv")
reg=pd.read_csv(r"C:\Users\Lenovo\Downloads\reg-month2.csv")
students=pd.read_csv(r"C:\Users\Lenovo\Downloads\students.csv")

a=pd.concat([regs,reg],ignore_index=True)

temp=students.merge(students,how="inner",left_on='partner',right_on='student_id')[['name_x','name_y']]
print(temp)