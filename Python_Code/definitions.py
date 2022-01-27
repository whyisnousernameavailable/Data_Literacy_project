import pandas as pd

dtype_caracteristics = {'Num_Acc': pd.Int64Dtype(), 'jour': pd.Int8Dtype(), 'mois': pd.Int8Dtype(),
                        'an': pd.Int16Dtype(), 'hrmn': pd.Int16Dtype(), 'lum': pd.Int8Dtype(),
                        'dep': pd.Int16Dtype(), 'com': pd.Int16Dtype(), 'col': pd.Int8Dtype(),
                        'adr': str, 'gps': str, 'lat': pd.Float64Dtype(), 'long': pd.Float64Dtype(),
                        'atm': pd.Int8Dtype(), 'agg': pd.Int8Dtype(), 'int': pd.Int8Dtype()}

dtype_places = {'Num_Acc': pd.Int64Dtype(), 'catr': pd.Int8Dtype(), 'voie': pd.Int32Dtype(),
                'v1': pd.Int8Dtype(), 'v2': str, 'circ': pd.Int8Dtype(),
                'nbv': pd.Int8Dtype(), 'vosp': pd.Int8Dtype(), 'prof': pd.Int8Dtype(),
                'pr': pd.Int16Dtype(), 'pr1': pd.Int32Dtype(), 'plan': pd.Int8Dtype(), 'lartpc': pd.Int32Dtype(),
                'larrout': pd.Int32Dtype(), 'surf': pd.Int8Dtype(), 'infra': pd.Int8Dtype(),
                'situ': pd.Int8Dtype(), 'env1': pd.Int32Dtype()}
