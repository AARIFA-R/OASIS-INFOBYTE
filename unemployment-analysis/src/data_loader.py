import pandas as pd

def load_data(path):
    df = pd.read_csv(path, header=None, sep=r'\s+', engine='python')
    print("Shape of raw data:", df.shape)
    df.columns = [
        'State', 'Date', 'Gender', 'Unemployment Rate',
        'Population', 'Literacy Rate', 'Region', 'Latitude', 'Longitude'
    ]
    print(df.info())
    return df