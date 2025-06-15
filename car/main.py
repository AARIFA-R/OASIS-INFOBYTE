from data_preprocessor import preprocess_data, load_data
from model import train_model
from visualizer import (
    plot_price_distribution,
    plot_fuel_type_count,
    plot_transmission_type_count,
    plot_selling_type_count,
    plot_actual_vs_predicted,
)
if __name__ == "__main__":
    file_path = "car data.csv" # Make sure this path is valid
    data = load_data(file_path)
    if data is not None:
        # Visualize raw data
        plot_price_distribution(data)
        plot_fuel_type_count(data)
        plot_transmission_type_count(data)
        plot_selling_type_count(data)
        X, y = preprocess_data(data)
        model, accuracy, y_test, y_pred = train_model(X, y)
        print(f"Model R^2 Accuracy: {accuracy:.2f}")
        plot_actual_vs_predicted(y_test, y_pred)