import pandas as pd
import numpy as np


df = pd.DataFrame([
    {'Key': 'AA', 'USD': 40},
    {'Key': 'BB', 'USD': 50},
    {'Key': 'CC', 'USD': 60}
])

# print(df.info())
# print(len(df.columns))

df.insert(len(df.columns), "EUR", np.array([42, 52, 62]))
# print(df['USD'])
usd = df['USD'].to_numpy()
eurfunction = lambda x: x * 1.2
eur = eurfunction(usd)
print(eur)
# df.insert(len(df.columns), "EUR", np.array([42, 52, 62]))







