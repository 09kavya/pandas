#work in only  dataframe
import numpy as np
import pandas as pd

runs=pd.read_csv(r"C:\Users\Lenovo\Downloads\batsman_runs_ipl (1).csv")
a=runs.set_index('batter')
print(a)