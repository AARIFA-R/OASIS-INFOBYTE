from sklearn.linear_model import LinearRegression

def predict_unemployment(df):
    df['timestamp'] = df['Date'].map(pd.Timestamp.toordinal)
    model = LinearRegression()
    model.fit(df[['timestamp']], df['Unemployment Rate'])
    df['Prediction'] = model.predict(df[['timestamp']])
    return df