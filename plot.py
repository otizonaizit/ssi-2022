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
    fig = plt.figure()
    gs = gridspec.GridSpec(2, 1)

    ax1 = plt.subplot(gs[0])
    #ax1.plot(years, sums, '*')
    ax1.fill_between(years, sums, color='olive')
    ax1.grid(True)
    ax1.xaxis.set_major_locator(MultipleLocator(1))
    ax1.xaxis.tick_top()
    ax1.xaxis.set_label_position('top')
    #plt.setp(ax1.get_xticklabels(), visible=False)
    #ax2.plot(years, diffs, '*')


    ax2 = plt.subplot(gs[1], sharex = ax1)
    ax2.fill_between(years, diffs, color='darkkhaki')
    #ax2.grid(True)
    #ax2.xaxis.set_major_locator(MultipleLocator(1))
    plt.subplots_adjust(hspace=.01)
    plt.show()

plot_stuff(years, sums, diffs)

