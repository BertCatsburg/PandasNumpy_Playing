import pandas

csv_path = '../data/real_usa_cities.csv'

df = pandas.read_csv(csv_path)
print(df.head())
print("Finished")