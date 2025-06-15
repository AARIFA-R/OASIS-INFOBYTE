import matplotlib.pyplot as plt
import seaborn as sns
def plot_price_distribution(df):
    if 'Selling_Price' in df.columns:
        plt.figure(figsize=(8, 5))
        sns.histplot(df['Selling_Price'], kde=True, bins=30, color='skyblue')
        plt.title("Selling Price Distribution")
        plt.xlabel("Selling Price")
        plt.ylabel("Count")
        plt.grid(True)
        plt.show()
def plot_fuel_type_count(df):
    if 'Fuel_Type' in df.columns:
        plt.figure(figsize=(6, 4))
        sns.countplot(x='Fuel_Type', data=df, palette='pastel')
        plt.title("Fuel Type Count")
        plt.xlabel("Fuel Type")
        plt.ylabel("Count")
        plt.grid(True)
        plt.show()
def plot_transmission_type_count(df):
    if 'Transmission' in df.columns:
        plt.figure(figsize=(6, 4))
        sns.countplot(x='Transmission', data=df, palette='muted')
        plt.title("Transmission Type Count")
        plt.xlabel("Transmission")
        plt.ylabel("Count")
        plt.grid(True)
        plt.show()
def plot_selling_type_count(df):
    if 'Selling_type' in df.columns:
        plt.figure(figsize=(6, 4))
        sns.countplot(x='Selling_type', data=df, palette='Set2')
        plt.title("Selling Type Count")
        plt.xlabel("Selling Type")
        plt.ylabel("Count")
        plt.grid(True)
        plt.show()
def plot_actual_vs_predicted(y_test, y_pred):
    plt.figure(figsize=(8, 5))
    sns.scatterplot(x=y_test, y=y_pred, color='purple')
    plt.plot([y_test.min(), y_test.max()], [y_test.min(), y_test.max()], 'r--') # ideal line
    plt.xlabel("Actual Selling Price")
    plt.ylabel("Predicted Selling Price")
    plt.title("Actual vs Predicted Selling Price")
    plt.grid(True)
    plt.show()