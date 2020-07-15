import pandas as pd

dict_data = {'a': 1, 'b': 2, 'c': 3}

series = pd.Series(dict_data)

print(type(series))
print('\n')
print(series)
