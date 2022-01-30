import pandas as pd
import matplotlib.pyplot as plt

from Python_Code.definitions import load_users_csv, load_caracteristics_csv

data_users = load_users_csv()
data_caracteristics = load_caracteristics_csv()

print(data_users.head())
print(data_users[['Num_Acc', 'grav']].head())


severity_by_year = pd.merge(data_users[['Num_Acc', 'grav']],
                            data_caracteristics[['Num_Acc', 'an']],
                            how="left",
                            on=['Num_Acc', 'Num_Acc'])

print(severity_by_year.head())

res = severity_by_year[['grav', 'an']].groupby(['an']).value_counts()
print(res)
print(res.shape)
#res.loc[(['grav'] == 2)].plot()
#plt.show()

