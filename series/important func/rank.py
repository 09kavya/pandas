import numpy as np
import pandas as pd

runs=pd.read_csv(r"C:\Users\Lenovo\Downloads\batsman_runs_ipl.csv")
runs['rank']=runs["batsman_run"].rank(ascending=False)
print(runs)