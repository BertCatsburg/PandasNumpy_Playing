import pandas as pd

songs = {
    'Album': ['Thriller', 'Back in Blank'],
    'Released': [1982, 1980],
    'Length': ['00:42:19', '00:42:11'],
}

songs_df = pd.DataFrame(songs)

songs_df.index = ['MJ', 'AC/DC']
print(songs_df.head())

print(songs_df.loc['MJ', 'Album'])  # 'Thriller'
