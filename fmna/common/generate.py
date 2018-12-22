import numpy as np


def multivariate_t(m, S, df=np.inf, n=1):
    m = np.asarray(m)
    d = len(m)
    if df == np.inf:
        x = 1.
    else:
        x = np.random.chisquare(df, n) / df
    z = np.random.multivariate_normal(np.zeros(d), S, (n,))
    return m + z / np.sqrt(x)[:, None]  # same output format as random.multivariate_normal


def normal_t_mixture(mix_p, m, S, df=np.inf, n=1):
    obs_normal = np.random.multivariate_normal(m, S, n)
    obs_t = multivariate_t(m, S, df, n)
    obs_uniform = np.random.random_sample(n)
    take_normal = (obs_uniform >= mix_p) * 1.0
    take_t = 1 - take_normal
    return np.transpose(
        np.transpose(obs_normal) * take_normal +
        np.transpose(obs_t) * take_t
    )
