from data_loader import load_data
from model import train_model
from visualizer import plot_pairplot, plot_corr
df = load_data("dataset/iris.csv")
plot_pairplot(df)
plot_corr(df)
X = df.drop("species", axis=1)
y = df["species"]
model, accuracy = train_model(X, y)
print(f"Model trained with accuracy: {accuracy:.2f}")