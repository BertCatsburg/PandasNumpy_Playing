import pandas as pd

data = [1, 3, 5, 7, 9]

df = pd.DataFrame(data)
dfr = df.rolling(2) # Take two numbers from the row, and then the next 2 numbers

print(type(dfr)) # <class 'pandas.core.window.rolling.Rolling'>
print(dfr.sum()) # 1+3, 3+5, 5+7, 7+9
print(dfr.mean())