import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

a=pd.read_csv(r"C:\Users\Lenovo\Downloads\bollywood.csv",index_col="movie")
b=a.value_counts().head(20).plot(kind='bar')
plt.show()
