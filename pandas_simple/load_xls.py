import pandas as pd

xlsx_path = "../data/real_usa_cities.xlsx"

df = pd.read_excel(xlsx_path)
print(df.head())