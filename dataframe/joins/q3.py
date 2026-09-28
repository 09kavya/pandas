# 3. Print the registration table
# cols -> name -> course -> price
import numpy as np
import pandas as pd
courses=pd.read_csv(r"C:\Users\Lenovo\Downloads\courses.csv")
regs=pd.read_csv(r"C:\Users\Lenovo\Downloads\reg-month1.csv")
reg=pd.read_csv(r"C:\Users\Lenovo\Downloads\reg-month2.csv")
students=pd.read_csv(r"C:\Users\Lenovo\Downloads\students.csv")

a=pd.concat([regs,reg],ignore_index=True)
 
registration=a.merge(students,on='student_id').merge(courses,on='course_id')[['name','course_name','price']]
print(registration)