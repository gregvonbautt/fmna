import math

import numpy as np
import scipy.stats as stats


def corr_pearson(v1, v2):
    return np.corrcoef(v1, v2)[0, 1]


def corr_sign(v1, v2):
    return sum((v1 > 0) == (v2 > 0)) * 1.0 / v1.shape[0]


def corr_sign_no_means(v1, v2):
    return sum((v1 - math.mean(v1)> 0) == (v2 - math.mean(v2) > 0)) * 1.0 / v1.shape[0]


def corr_kendall(v1, v2):
    return stats.kendalltau(stats.stats.rankdata(v1), stats.stats.rankdata(v2))[0]


def corr_spearman(v1, v2):
    return stats.spearmanr(v1, v2).correlation


def to_pearson_from(type, value):
    if type == "sign":
        return math.sin(math.pi * (value - 0.5))
    elif type == "kendall":
        return math.sin(math.pi * value / 2)
    else:
        raise Exception("Cannot convert from to pearson from " + type)
