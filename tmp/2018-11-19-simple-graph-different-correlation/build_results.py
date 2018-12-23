#!/usr/bin/python

from numpy import genfromtxt
import sys

import matplotlib.pyplot as plt
from rsa import key
import numpy

###############################
# params
###############################

case = sys.argv[1]
corr = float(sys.argv[2])

###############################

raw = genfromtxt("results/raw_%s.csv" % case, delimiter=',')

num_thresholds = 100
thresholds = [tt * 1.0 / num_thresholds for tt in range(0, num_thresholds + 1)] 

pearson_false_positive = numpy.zeros(num_thresholds + 1)
pearson_false_negative = numpy.zeros(num_thresholds + 1)

sign_false_positive = numpy.zeros(num_thresholds + 1)
sign_false_negative = numpy.zeros(num_thresholds + 1)

sign_no_means_false_positive = numpy.zeros(num_thresholds + 1)
sign_no_means_false_negative = numpy.zeros(num_thresholds + 1)

tau_false_positive = numpy.zeros(num_thresholds + 1)
tau_false_negative = numpy.zeros(num_thresholds + 1)

for r in raw:
    key = int(r[0])

    true_graph = r[1]
    pearson_graph = r[2]
    sign_graph = r[3]
    sign_no_means_graph = r[4]
    tau_graph = r[5]

    pearson_false_positive[key] += pearson_graph > true_graph
    pearson_false_negative[key] += pearson_graph < true_graph

    sign_false_positive[key] += sign_graph > true_graph
    sign_false_negative[key] += sign_graph < true_graph

    sign_no_means_false_positive[key] += sign_no_means_graph > true_graph
    sign_no_means_false_negative[key] += sign_no_means_graph < true_graph

    tau_false_positive[key] += tau_graph > true_graph
    tau_false_negative[key] += tau_graph < true_graph

num_runs = raw[:, 0].size / (num_thresholds + 1)

pearson_false_positive /= num_runs
pearson_false_negative /= num_runs

sign_false_positive /= num_runs
sign_false_negative /= num_runs

sign_no_means_false_positive /= num_runs
sign_no_means_false_negative /= num_runs

tau_false_positive /= num_runs
tau_false_negative /= num_runs

fig = plt.figure("False Positives")
plt.title("False Positives")
plt.scatter(thresholds, pearson_false_positive, label="Standard", color='k')
plt.scatter(thresholds, sign_false_positive, label="Sign", color='r')
plt.scatter(thresholds, sign_no_means_false_positive, label="Sign -m", color='g')
plt.scatter(thresholds, tau_false_positive, label="Kendall", color='b')
plt.xlim([0, 1])
plt.ylim([0, 1])
plt.axvline(corr, color="k", linestyle="--")
plt.legend()
plt.grid()
name = "false-positives"
fig.savefig("results/%s_%s.png" % (name, case), figsize=(8, 6), dpi=300)

fig = plt.figure("False Negatives")
plt.title("False Negatives")
plt.scatter(thresholds, pearson_false_negative, label="Standard", color='k')
plt.scatter(thresholds, sign_false_negative, label="Sign", color='r')
plt.scatter(thresholds, sign_no_means_false_negative, label="Sign -m", color='g')
plt.scatter(thresholds, tau_false_negative, label="Kendall", color='b')
plt.xlim([0, 1])
plt.ylim([0, 1])
plt.axvline(corr, color="k", linestyle="--")
plt.legend()
plt.grid()
name = "false-negatives"
fig.savefig("results/%s_%s.png" % (name, case), figsize=(8, 6), dpi=300)

#plt.show()
