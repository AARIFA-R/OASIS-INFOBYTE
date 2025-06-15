import matplotlib.pyplot as plt
import seaborn as sns

def plot_unemployment_trend(df):
    plt.figure(figsize=(12, 6))
    sns.lineplot(x='Date', y='Unemployment Rate', data=df, marker='o')
    plt.title('Unemployment Rate Over Time')
    plt.xlabel('Date')
    plt.ylabel('Unemployment Rate (%)')
    plt.xticks(rotation=45)
    plt.grid(True)
    plt.tight_layout()
    plt.show()

def plot_regionwise_unemployment(df):
    plt.figure(figsize=(10, 6))
    region_avg = df.groupby('Region')['Unemployment Rate'].mean().sort_values()
    region_avg.plot(kind='barh', color='skyblue')
    plt.title('Average Unemployment Rate by Region')
    plt.xlabel('Unemployment Rate (%)')
    plt.ylabel('Region')
    plt.tight_layout()
    plt.show()

def plot_heatmap(df):
    if 'Month' not in df.columns:
        print("Error: 'Month' column is missing in the DataFrame.")
        return
    heatmap_data = df.pivot_table(
        index='State',
        columns='Month',
        values='Unemployment Rate',
        aggfunc='mean'
    )
    month_order = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun',
                   'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
    heatmap_data = heatmap_data.reindex(columns=month_order, fill_value=None)
    plt.figure(figsize=(12, 8))
    sns.heatmap(heatmap_data, cmap='coolwarm', annot=True, fmt=".1f", linewidths=0.5, linecolor='gray')
    plt.title('State vs Month - Unemployment Heatmap')
    plt.xlabel('Month')
    plt.ylabel('State')
    plt.tight_layout()
    plt.show()