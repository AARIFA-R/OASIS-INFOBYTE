import pandas as pd
from sklearn.preprocessing import LabelEncoder
def load_data(file_path):
    try:
        return pd.read_csv(file_path)
    except Exception as e:
        print("Error loading file:", e)
        return None
def preprocess_data(df):
    df = df.copy()
    df.dropna(inplace=True)
    le = LabelEncoder()
    if 'Fuel_Type' in df.columns:
        df['Fuel_Type'] = le.fit_transform(df['Fuel_Type'])
    if 'Selling_type' in df.columns:
        df['Selling_type'] = le.fit_transform(df['Selling_type'])
    if 'Transmission' in df.columns:
        df['Transmission'] = le.fit_transform(df['Transmission'])
    if 'Year' in df.columns:
        df['Car_Age'] = 2025 - df['Year']
        df.drop(['Year'], axis=1, inplace=True)
    if 'Car_Name' in df.columns:
        df.drop(['Car_Name'], axis=1, inplace=True)
    X = df.drop('Selling_Price', axis=1)
    y = df['Selling_Price']
    return X, y