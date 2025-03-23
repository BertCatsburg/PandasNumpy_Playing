import pandas as pd

csv_path = '../data/real_usa_cities.csv'

df = pd.read_csv(csv_path)

df2 = df[df['Population']<100000]
print(df2.head())