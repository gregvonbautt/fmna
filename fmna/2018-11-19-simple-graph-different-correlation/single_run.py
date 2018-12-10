#!/usr/bin/python

import math
import sys
sys.path.append('../common')

import funcs
import numpy as np
import scipy.stats as stats

###############################
# params
###############################
num_obs = 90

#corr = 0.25
#corr = 0.5
corr = 0.75

# dist = "NORMAL"
dist = "STUDENT"

###############################

means = [0, 0]
S = [[1, corr], [corr, 1]]
df = 3

if dist == "NORMAL":
    obs = np.transpose(np.random.multivariate_normal(means, S, num_obs))
elif dist == "STUDENT":
    variance = 1.0 * df / (df - 2)
    obs = np.transpose(funcs.multivariate_t_rvs(means, S, df, num_obs)) / math.sqrt(variance)
else:
    raise Exception()

pearson = np.corrcoef(obs)[0, 1]
tau = stats.kendalltau(stats.stats.rankdata(obs[0]), stats.stats.rankdata(obs[1]))[0]
pearson_est_tau = math.sin(math.pi * tau / 2)

sign_corr = sum((obs[0] > 0) == (obs[1] > 0)) * 1.0 / num_obs
pearson_est_sign = math.sin(math.pi * (sign_corr - 0.5))

sign_corr_no_means = sum(((obs[0] - np.mean(obs[0])) > 0) == ((obs[1] - np.mean(obs[1])) > 0)) * 1.0 / num_obs
pearson_est_sign_no_means = math.sin(math.pi * (sign_corr_no_means - 0.5))

num_thresholds = 100
for tt in range(0, num_thresholds + 1):
    t = 1.0 * tt / num_thresholds
    true_graph = int(corr > t)
    pearson_graph = int(pearson > t)
    sign_graph = int(pearson_est_sign > t)
    sign_graph_no_means = int(pearson_est_sign_no_means > t)
    tau_graph = int(pearson_est_tau > t)
    print "%s, %s, %s, %s, %s, %s" % (tt, true_graph, pearson_graph, sign_graph, sign_graph_no_means, tau_graph)
