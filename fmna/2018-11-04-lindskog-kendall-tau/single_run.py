#!/usr/bin/python

import math
import sys
sys.path.append('../common')

import funcs
import numpy as np
import scipy.stats as stats







means = [0, 0]
S = [[1, 0.5], [0.5, 1]]
df = 3
num_obs = 90

obs = np.transpose(funcs.multivariate_t_rvs(means, S, df, num_obs))

pearson = np.corrcoef(obs)[0, 1]
tau = stats.kendalltau(stats.stats.rankdata(obs[0]), stats.stats.rankdata(obs[1]))[0]
pearson_est = math.sin(math.pi * tau / 2)
sign_corr = sum((obs[0] > 0) == (obs[1] > 0)) * 1.0 / num_obs
sign_corr_no_means = sum(((obs[0] - np.mean(obs[0])) > 0) == ((obs[1] - np.mean(obs[1])) > 0)) * 1.0 / num_obs

pearson_est_sign = math.sin(math.pi * (sign_corr - 0.5))
pearson_est_sign_no_means = math.sin(math.pi * (sign_corr_no_means - 0.5))

# print "%s, %s, %s, %s, %s, %s, %s" % (pearson, tau, pearson_est, sign_corr, sign_corr_no_means, pearson_est_sign, pearson_est_sign_no_means)
