import matplotlib.pyplot as plt

def plot_histogram(df, column):
    """Plot a histogram of a given column"""
    plt.hist(df[column], bins=50, color='blue', alpha=0.7)
    plt.xlabel(column)
    plt.ylabel('Frequency')
    plt.title(f'Histogram of {column}')
    plt.savefig("output/histogram.png")
    plt.show()

