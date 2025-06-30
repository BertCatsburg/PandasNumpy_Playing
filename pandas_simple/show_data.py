import pandas as pd


df = pd.DataFrame([
    {'Key': 'AAA', 'Value': 10},
    {'Key': 'BBB', 'Value': 20},
    {'Key': 'CCC', 'Value': 30}
])

print(df.to_dict())