def predict_species(model):
    print("🔍 Enter flower features to predict species:")
    sepal_length = float(input("Sepal Length: "))
    sepal_width = float(input("Sepal Width: "))
    petal_length = float(input("Petal Length: "))
    petal_width = float(input("Petal Width: "))
    sample = [[sepal_length, sepal_width, petal_length, petal_width]]
    pred = model.predict(sample)
    print(f"🌸 Predicted Species: {pred[0]}")