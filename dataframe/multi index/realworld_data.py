import pandas as pd

death=pd.read_csv(r"C:\Users\Lenovo\Downloads\time_series_covid19_deaths_global.csv")
confirm=pd.read_csv(r"C:\Users\Lenovo\Downloads\time_series_covid19_confirmed_global.csv")
# print(death.columns)
a=death.melt(id_vars=['Province/State', 'Country/Region', 'Lat', 'Long'],var_name='date',value_name='num of deaths')
b=confirm.melt(id_vars=['Province/State', 'Country/Region', 'Lat', 'Long'],var_name='date',value_name='num of cases')
temp=b.merge(a,how='inner',on=['Province/State', 'Country/Region', 'Lat', 'Long','date'])[['Country/Region','date','num of cases','num of deaths']]
print(temp)