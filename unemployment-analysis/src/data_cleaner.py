import pandas as pd
def clean_data(df):
    df.columns = df.columns.str.strip()
    df.dropna(inplace=True)
    df['Date'] = pd.to_datetime(df['Date'])
    df['Month'] = df['Date'].dt.strftime('%b')  # Add Month column like 'Jan', 'Feb'
    return df