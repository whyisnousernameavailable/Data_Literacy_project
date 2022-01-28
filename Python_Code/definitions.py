import pandas as pd

dtype_caracteristics = {'Num_Acc': pd.Int64Dtype(), 'jour': pd.Int8Dtype(), 'mois': pd.Int8Dtype(),
                        'an': pd.Int16Dtype(), 'hrmn': pd.Int16Dtype(), 'lum': pd.Int8Dtype(),
                        'dep': pd.Int16Dtype(), 'com': pd.Int16Dtype(), 'col': pd.Int8Dtype(),
                        'adr': str, 'gps': str, 'lat': pd.Float64Dtype(), 'long': pd.Float64Dtype(),
                        'atm': pd.Int8Dtype(), 'agg': pd.Int8Dtype(), 'int': pd.Int8Dtype()}

dtype_places = {'Num_Acc': pd.Int64Dtype(), 'catr': pd.Int8Dtype(), 'voie': str,
                'v1': pd.Int8Dtype(), 'v2': str, 'circ': pd.Int8Dtype(),
                'nbv': pd.Int8Dtype(), 'vosp': pd.Int8Dtype(), 'prof': pd.Int8Dtype(),
                'pr': str, 'pr1': str, 'plan': pd.Int8Dtype(), 'lartpc': pd.Int32Dtype(),
                'larrout': pd.Int32Dtype(), 'surf': pd.Int8Dtype(), 'infra': pd.Int8Dtype(),
                'situ': pd.Int8Dtype(), 'env1': pd.Int32Dtype()}

dtype_users = {'Num_Acc': pd.Int64Dtype(), 'place': pd.Int8Dtype(), 'catu': pd.Int8Dtype(),
               'grav': pd.Int8Dtype(), 'sexe': pd.Int8Dtype(), 'trajet': pd.Int8Dtype(),
               'secu': pd.Int8Dtype(), 'locp': pd.Int8Dtype(), 'actp': pd.Int8Dtype(),
               'etatp': pd.Int8Dtype(), 'an_nais': pd.Int16Dtype(), 'num_veh': str}

dtype_vehicles = {'Num_Acc': pd.Int64Dtype(), 'catv': pd.Int8Dtype(), 'num_veh': str}

dtype_holidays = {'ds': str, 'holiday': str}


def load_caracteristics_csv():
    return pd.read_csv('..//archive//caracteristics.csv',
                       encoding="ISO-8859-1", dtype=dtype_caracteristics,
                       on_bad_lines='warn', na_values=['-'])


def load_places_csv():
    return pd.read_csv('..//archive//places.csv',
                       encoding="ISO-8859-1", dtype=dtype_places,
                       on_bad_lines='warn', na_values=['-'])


def load_user_csv():
    return pd.read_csv('..//archive//users.csv',
                       encoding="ISO-8859-1", dtype=dtype_users,
                       on_bad_lines='warn', na_values=['-'])


def load_vehicles_csv():
    return pd.read_csv('..//archive//vehicles.csv',
                       encoding="ISO-8859-1", dtype=dtype_vehicles,
                       on_bad_lines='warn', na_values=['-'])


def load_holidays_csv():
    return pd.read_csv('..//archive//holidays.csv',
                       encoding="ISO-8859-1", dtype=dtype_holidays,
                       on_bad_lines='warn', na_values=['-'], parse_dates=['ds'])
