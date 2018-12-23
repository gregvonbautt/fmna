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
corr = 0.5
###############################

means = [0, 0]
S = [[1, corr], [corr, 1]]
df = 3

obs_normal = np.transpose(np.random.multivariate_normal(means, S, num_obs))

variance = 1.0 * df / (df - 2)
obs_student = np.transpose(funcs.multivariate_t_rvs(means, S, df, num_obs)) / math.sqrt(variance)

uniform_obs = np.random.random_sample(num_obs)

def obsWithMixtureParam(mixture_param):
    student_prob = (uniform_obs < mixture_param) * 1.0
    normal_prob = 1 - student_prob
    return np.multiply(student_prob, obs_student) + np.multiply(normal_prob, obs_normal)

def one_run(p, tt, obs):
    t = tt * 1.0 / 100

    pearson = np.corrcoef(obs)[0, 1]

    tau = stats.kendalltau(stats.stats.rankdata(obs[0]), stats.stats.rankdata(obs[1]))[0]
    pearson_est_tau = math.sin(math.pi * tau / 2)
    
    sign_corr = sum((obs[0] > 0) == (obs[1] > 0)) * 1.0 / num_obs
    pearson_est_sign = math.sin(math.pi * (sign_corr - 0.5))
    
    sign_corr_no_means = sum(((obs[0] - np.mean(obs[0])) > 0) == ((obs[1] - np.mean(obs[1])) > 0)) * 1.0 / num_obs
    pearson_est_sign_no_means = math.sin(math.pi * (sign_corr_no_means - 0.5))

    true_graph = int(corr > t)
    pearson_graph = int(pearson > t)
    sign_graph = int(pearson_est_sign > t)
    sign_graph_no_means = int(pearson_est_sign_no_means > t)
    tau_graph = int(pearson_est_tau > t)

    print "%s, %s, %s, %s, %s, %s, %s" % (p, tt, true_graph, pearson_graph, sign_graph, sign_graph_no_means, tau_graph)

num_mixture_params = 20
for p in range(0, num_mixture_params + 1):
    mixture_param = 1.0 * p / num_mixture_params
    obs = obsWithMixtureParam(mixture_param)
    one_run(p, 25, obs)
    one_run(p, 50, obs)
    one_run(p, 75, obs)