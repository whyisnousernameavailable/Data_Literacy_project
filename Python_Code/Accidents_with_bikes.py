import pandas as pd
import matplotlib.pyplot as plt
from tueplots import bundles

from Python_Code.definitions import load_users_csv, load_caracteristics_csv, load_vehicles_csv, load_places_csv

plt.rcParams.update(bundles.neurips2021(usetex=False))

data_users = load_users_csv()
data_caracteristics = load_caracteristics_csv()
data_vehicles = load_vehicles_csv()
data_places = load_places_csv()

user_acc_data = pd.merge(data_users[['Num_Acc', 'grav', 'catu']],
                            data_caracteristics[['Num_Acc', 'an']],
                            how="left",
                            on=['Num_Acc', 'Num_Acc'])

user_acc_catv_data = pd.merge(user_acc_data,
                              data_vehicles[['Num_Acc', 'catv']],
                              how="left",
                              on=['Num_Acc', 'Num_Acc'])
user_acc_catv_places_data = pd.merge(user_acc_catv_data,
                                     data_places[['Num_Acc', 'vosp', 'prof']],
                                     how="left",
                                     on=['Num_Acc', 'Num_Acc'])


if isinstance(user_acc_catv_places_data, pd.DataFrame):
    print('I am a dataframe')

data_bike_accidents = user_acc_catv_places_data.loc[user_acc_catv_places_data['catv'] == 1]
data_bike_accidents_unscathed = data_bike_accidents.loc[user_acc_catv_places_data['grav'] == 1]
data_bike_accidents_dead = data_bike_accidents.loc[user_acc_catv_places_data['grav'] == 2]
data_bike_accidents_hosp = data_bike_accidents.loc[user_acc_catv_places_data['grav'] == 3]
data_bike_accidents_li = data_bike_accidents.loc[user_acc_catv_places_data['grav'] == 4]

print('Unscathed:')
print(data_bike_accidents_unscathed[['vosp']].value_counts(normalize=True))
print('Killed:')
print(data_bike_accidents_dead[['vosp']].value_counts(normalize=True))
print('hospitalized:')
print(data_bike_accidents_hosp[['vosp']].value_counts(normalize=True))
print('LI:')
print(data_bike_accidents_li[['vosp']].value_counts(normalize=True))
