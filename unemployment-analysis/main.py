from src.data_loader import load_data
from src.data_cleaner import clean_data
from src.data_visualizer import plot_unemployment_trend, plot_regionwise_unemployment, plot_heatmap

df = load_data('data/unemployment_data.csv')
df = clean_data(df)
plot_unemployment_trend(df)
plot_regionwise_unemployment(df)
plot_heatmap(df)