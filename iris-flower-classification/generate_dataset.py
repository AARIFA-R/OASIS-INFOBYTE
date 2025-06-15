from sklearn.datasets import load_iris
import pandas as pd
import os
def generate_csv():
    iris = load_iris()
    df = pd.DataFrame(iris.data, columns=["sepal_length", "sepal_width", "petal_length", "petal_width"])
    df["species"] = pd.Categorical.from_codes(iris.target, iris.target_names)
    os.makedirs("dataset", exist_ok=True)
    df.to_csv("dataset/iris.csv", index=False)
    print("✅ dataset/iris.csv created.")
if __name__ == "__main__":
    generate_csv()