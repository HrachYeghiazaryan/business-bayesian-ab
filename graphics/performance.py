import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def plot_performance(algorithm):
    """
    Plots the cumulative reward earned over time.

    Parameters
    ----------
    algorithm : EpsilonGreedy

    """
    cumulative_average = np.cumsum(algorithm.df.loc[:,'reward'])/algorithm.df.loc[:,'experiment_number']
    plt.plot(cumulative_average)
    plt.title('Win rate convergence for Epsilon Greedy')
    plt.xlabel('Number of trials')
    plt.ylabel('Estimated reward')
    plt.show()