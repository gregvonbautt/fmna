#!/usr/bin/python

from numpy import genfromtxt
import sys

import matplotlib.pyplot as plt

def simple_scatter(name, arr, ylim):
    fig = plt.figure(name)
    plt.title(name)
    plt.scatter(range(0, arr.size), arr)
    plt.xlim([0, arr.size])
    plt.ylim(ylim)
    plt.axhline(0, color='k')
    plt.grid()
    fig.savefig("%s/%s.png" % (sys.argv[1], name), figsize=(8, 6), dpi=300)

raw = genfromtxt("%s/raw.csv" % sys.argv[1], delimiter=',')


simple_scatter("Standard Estimator", raw[:, 0], [-1, 1])
simple_scatter("Kendall's tau Transform", raw[:, 2], [-1, 1])
simple_scatter("Sign Transform", raw[:, 5], [-1, 1])
