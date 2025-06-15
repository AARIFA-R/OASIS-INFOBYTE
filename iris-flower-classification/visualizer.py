import matplotlib.pyplot as plt
import seaborn as sns
def plot_pairplot(df):
    sns.pairplot(df, hue="species")
    plt.show()
def plot_corr(df):
    corr = df.drop(columns=["species"]).corr()
    sns.heatmap(corr, annot=True, cmap="coolwarm")
    plt.show()