#!/usr/bin/python

from numpy import genfromtxt
import sys

import matplotlib.pyplot as plt
from rsa import key
import numpy

raw = genfromtxt("%s/raw.csv" % sys.argv[1], delimiter=',')

num_thresholds = 100
thresholds = [tt * 1.0 / num_thresholds for tt in range(0, num_thresholds + 1)] 

sign_false_positive = numpy.zeros(num_thresholds + 1)
sign_false_negative = numpy.zeros(num_thresholds + 1)

sign_no_means_false_positive = numpy.zeros(num_thresholds + 1)
sign_no_means_false_negative = numpy.zeros(num_thresholds + 1)

for r in raw:
    key = int(r[0])
    true_graph = r[1]
    sign_graph = r[2]
    sign_no_means_graph = r[3]

    sign_false_positive[key] += sign_graph > true_graph
    sign_false_negative[key] += sign_graph < true_graph

    sign_no_means_false_positive[key] += sign_no_means_graph > true_graph
    sign_no_means_false_negative[key] += sign_no_means_graph < true_graph

num_runs = raw[:, 0].size / (num_thresholds + 1)

sign_false_positive /= num_runs
sign_false_negative /= num_runs

sign_no_means_false_positive /= num_runs
sign_no_means_false_negative /= num_runs

fig = plt.figure("False Positives")
plt.title("False Positives")
plt.scatter(thresholds, sign_false_positive, label="Sign", color='r', marker='x')
plt.scatter(thresholds, sign_no_means_false_positive, label="Sign Means Subtracted", color='g', marker='.')
plt.xlim([0, 1])
plt.ylim([0, 1])
plt.axvline(0.5, color="k", linestyle="--")
plt.legend()
plt.grid()
name = "false-positives"
fig.savefig("%s/%s.png" % (sys.argv[1], name), figsize=(8, 6), dpi=300)

fig = plt.figure("False Negatives")
plt.title("False Negatives")
plt.scatter(thresholds, sign_false_negative, label="Sign", color='r', marker='x')
plt.scatter(thresholds, sign_no_means_false_negative, label="Sign Means Subtracted", color='g', marker='.')
plt.xlim([0, 1])
plt.ylim([0, 1])
plt.axvline(0.5, color="k", linestyle="--")
plt.legend()
plt.grid()
name = "false-negatives"
fig.savefig("%s/%s.png" % (sys.argv[1], name), figsize=(8, 6), dpi=300)

#plt.show()
