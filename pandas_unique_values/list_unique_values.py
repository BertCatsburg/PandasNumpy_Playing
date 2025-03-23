import pandas as pd


csv_path = '../data/data.csv'

df = pd.read_csv(csv_path)
d2 = df['Getal'].unique()
print(d2)
print(len(d2))