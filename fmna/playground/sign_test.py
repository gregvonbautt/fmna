#!/usr/bin/python

import matplotlib.pyplot as plt
import numpy as np

import fmna as funcs

means = [0, 0]
S = [[1, 0.5], [0.5, 1]]
df = 3
num_obs = 50

x = []

for i in range(0, 100000):
    # NORMAL DISTRIBUTION !!!
    # obs = np.transpose(np.random.multivariate_normal(means, S, num_obs))
    obs = np.transpose(funcs.multivariate_t_rvs(means, S, df, num_obs))
    sign_corr = sum((obs[0] > 0) == (obs[1] > 0)) * 1.0 / num_obs
    x.append(sign_corr)

# print x
bins = [b * 1.0 / 1000 for b in range(0, 1001)] 

f = plt.hist(x, bins)
plt.xlim([0, 1])
plt.show()
