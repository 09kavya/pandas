# 10. find top 3 students who spent most amount of money on courses

import pandas as pd

courses=pd.read_csv(r"C:\Users\Lenovo\Downloads\courses.csv")
regs=pd.read_csv(r"C:\Users\Lenovo\Downloads\reg-month1.csv")
reg=pd.read_csv(r"C:\Users\Lenovo\Downloads\reg-month2.csv")
students=pd.read_csv(r"C:\Users\Lenovo\Downloads\students.csv")

a=pd.concat([regs,reg],ignore_index=True)

temp=a.merge(students,on='student_id').merge(courses,on='course_id').groupby(['student_id','name'])['price'].sum().sort_values(ascending=False).head(3)
print(temp)