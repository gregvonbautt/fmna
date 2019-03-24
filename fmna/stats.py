import math

import numpy as np
import scipy.stats as stats


def corr_pearson(v1, v2):
    return np.corrcoef(v1, v2)[0, 1]


def corr_sign(v1, v2):
    return sum((v1 > 0) == (v2 > 0)) * 1.0 / v1.shape[0]


def corr_sign_no_means(v1, v2):
    return sum((v1 - np.mean(v1)> 0) == (v2 - np.mean(v2) > 0)) * 1.0 / v1.shape[0]


def corr_kendall(v1, v2):
    return stats.kendalltau(stats.stats.rankdata(v1), stats.stats.rankdata(v2))[0]


def corr_spearman(v1, v2):
    return stats.spearmanr(v1, v2).correlation


def to_pearson_from(type, value):
    if type == "sign":
        return math.sin((value - 0.5) * math.pi)
    elif type == "kendall":
        return math.sin(value * math.pi / 2)
    elif type == "spearman":
        return math.sin(value * math.pi / 6) * 2
    else:
        raise Exception("Cannot convert from to pearson from " + type)

def corr_matr(obs, corr_func):
    num_vars = obs.shape[1]
    res = np.zeros(shape=[num_vars, num_vars])
    for i in range(0, num_vars):
        for j in range(0, num_vars):
            v1 = obs[:, i]
            v2 = obs[:, j]
            res[i, j] = corr_func(v1, v2)
    return res

def to_pearson_from_matr(type, m):
    res = np.zeros(m.shape)
    for i in range(0, res.shape[0]):
        for j in range(0, res.shape[0]):
            res[i, j] = to_pearson_from(type, m[i, j])
    return res

