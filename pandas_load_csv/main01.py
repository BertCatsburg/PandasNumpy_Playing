import pandas as pd
import glob


def get_csv_data(file_to_process) -> pd.DataFrame:
    dataframe = pd.read_csv(file_to_process)
    return dataframe


def process_all_csv_files():
    all_data = pd.DataFrame(columns=['Naam', 'Plaats', 'Leeftijd', 'Salaris'])
    for csvfile in glob.glob('*.csv'):
        d = get_csv_data(csvfile)
        all_data = pd.concat([all_data, d], ignore_index=True).sort_values(by=['Leeftijd'])

    return all_data


if __name__ == "__main__":
    df = process_all_csv_files()

    print(df.head())