#how to replace existing index without loosing


import numpy as np
import pandas as pd

runs=pd.read_csv(r"C:\Users\Lenovo\Downloads\batsman_runs_ipl (1).csv")
a=runs.reset_index().set_index('batsman_run')
print(a)
