import numpy as np
import matplotlib.pyplot as plt
from matplotlib import gridspec
from matplotlib.ticker import MultipleLocator


data = np.loadtxt('stats.csv', delimiter=',')
years = data[:,0]
sums = data[:,1]/1000
diffs = data[:,2]/1000

plt.style.use('ggplot')

def plot_account_balance(years, sums, diffs):
    fig, (ax1, ax2) = plt.subplots(2, 1, sharex=True)

    ax1.fill_between(years, sums, color='olive')
    ax1.grid(True)
    ax1.xaxis.set_major_locator(MultipleLocator(1))
    ax1.tick_params(axis='x', top=True, labeltop=True)
    ax1.tick_params(axis='y', right=True, labelright=True)

    ax2.fill_between(years, diffs, color='darkkhaki')
    ax2.tick_params(axis='y', right=True, labelright=True)

    fig.subplots_adjust(hspace=.01)
    return fig

fig = plot_account_balance(years, sums, diffs)

plt.show()
