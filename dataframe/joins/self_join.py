import numpy as np
import pandas as pd


students=pd.read_csv(r"C:\Users\Lenovo\Downloads\students.csv")



temp=students.merge(students,how='inner',left_on='partner',right_on='student_id')
print(temp)