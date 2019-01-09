import matplotlib.pyplot as plt
import numpy as np

import fmna.experiment as exp


def fname(title):
    fname = "%s/output/%s.png" % (exp.dir(), title.lower().replace(" ", "_").replace(",", ""))
    print(fname)
    return fname

def simple_scatter(title, arr, ylim):
    fig = plt.figure(title)
    plt.title(title)
    plt.scatter(range(0, len(arr)), arr, marker='.')
    plt.xlim([0, len(arr)])
    plt.ylim(ylim)
    plt.axhline(0, color='k')
    plt.grid()
    plt.gcf().text(0.02, 0.02, "m=%s, std=%s" % ("{0:.5f}".format(np.mean(arr)), "{0:.5f}".format(np.std(arr))))
    fig.savefig(fname(title), figsize=(8, 6), dpi=300)


def simple_graph(title, values, xlim=[0, 1], ylim=[0, 1]):
    fig = plt.figure(title)
    plt.title(title)
    for v in values:
        x = v[0]
        y = v[1]
        label = v[2]
        plt.plot(x, y, label=label)
    plt.xlim(xlim)
    plt.ylim(ylim)
    plt.legend()
    plt.grid()
    fig.savefig(fname(title), figsize=(8, 6), dpi=300)
