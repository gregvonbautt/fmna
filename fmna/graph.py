import matplotlib.pyplot as plt

import fmna.experiment as exp


def simple_scatter(name, arr, ylim):
    fig = plt.figure(name)
    plt.title(name)
    plt.scatter(range(0, len(arr)), arr)
    plt.xlim([0, len(arr)])
    plt.ylim(ylim)
    plt.axhline(0, color='k')
    plt.grid()
    fname = "%s/output/%s.png" % (exp.dir(), name)
    print(fname)
    fig.savefig(fname, figsize=(8, 6), dpi=300)
