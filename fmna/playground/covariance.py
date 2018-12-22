#!/usr/bin/python

import math

import numpy as np

import fmna as funcs

corr = 0.5
means = [0, 0]
S = [[1, corr], [corr, 1]]
df = 3
num_obs = 10000000

obs_t = np.transpose(funcs.multivariate_t_rvs(means, S, df, num_obs))
obs_t /= math.sqrt(3)
obs_norm = np.transpose(np.random.multivariate_normal(means, S, num_obs))

print("Student")
print(np.cov(obs_t))
print(np.corrcoef(obs_t))

print("Normal")
print(np.cov(obs_norm))
print(np.corrcoef(obs_norm))