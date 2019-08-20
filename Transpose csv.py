import pandas as pd
pd.read_csv('input.csv', header=None).T.to_csv('output.csv', header=False, index=False)
