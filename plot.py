import numpy as np
import matplotlib.pyplot as plt
from matplotlib import gridspec
from matplotlib.ticker import MultipleLocator

plt.style.use('ggplot')

def load_data(filename):
    data = np.loadtxt(filename, delimiter=',')
    years = data[:,0]
    sums = data[:,1]/1000
    diffs = data[:,2]/1000
    return years, sums, diffs

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

def save_plot_to(fig, filename):
    fig.savefig(filename)


if __name__ == '__main__':
    years, sums, diffs = load_data('stats.csv')
    fig = plot_account_balance(years, sums, diffs)
    save_plot_to(fig, 'plot.png')
    plt.show()
