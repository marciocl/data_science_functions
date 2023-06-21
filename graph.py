##### Calculate and plot confidence Interval

import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import t, sem


def mean_confidence_interval(data: list, confidence_level:float = 0.95, label=None):
    mean = np.mean(data)
    print(mean)
    std_err = np.std(data)
    critical_value = t.ppf((1 + confidence_level) / 2, len(data) - 1)
    margin_of_error = critical_value * std_err
    confidence_interval = (mean - margin_of_error, mean + margin_of_error)
    return confidence_interval


def plot_confidence_intervals(dados: list, labels= []):
    confidence_intervals = [mean_confidence_interval(i) for i in dados]
    means = [np.mean(i) for i in dados]

    fig, ax = plt.subplots(figsize=(20, 10))

    # Plot the confidence intervals
    for i, (lower, upper) in enumerate(confidence_intervals):
        plt.plot([i, i], [lower, upper], color='blue', linewidth=2)

    # Plot the means
    plt.scatter(range(len(means)), means, color='red', zorder=10)

    # Customize the plot
    if len(labels) == 0:
        plt.xticks(range(len(means)),[i for i in range(len(dados))])
    else:
        plt.xticks(range(len(means)),labels)
    plt.xlabel('Datasets')
    plt.ylabel('Values')
    plt.title('Confidence Intervals and Means')
    ax.spines[['top', 'right']].set_visible(False)

    # Show the plot
    plt.show()
