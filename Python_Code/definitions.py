import pandas as pd

dtype_caracteristics = {'Num_Acc': pd.Int64Dtype(), 'jour': pd.Int8Dtype(), 'mois': pd.Int8Dtype(),
                        'an': pd.Int16Dtype(), 'hrmn': pd.Int16Dtype(), 'lum': pd.Int8Dtype(),
                        'dep': pd.Int16Dtype(), 'com': pd.Int16Dtype(), 'col': pd.Int8Dtype(),
                        'adr': str, 'gps': str, 'lat': pd.Float64Dtype(), 'long': pd.Float64Dtype(),
                        'atm': pd.Int8Dtype(), 'agg': pd.Int8Dtype(), 'int': pd.Int8Dtype()}



