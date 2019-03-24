import csv
import math
import numpy as np
import scipy.sparse.csgraph as csgraph

import graphviz as gv

from fmna import db, stats, generate, experiment


def log_yield(p1, p2):
    return math.log(p2 / p1)
    # return p2 / p1


def calc_yields(filename, num_tickers):
    with open(filename) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        yields = None
        for row in csv_reader:
            r = row[1:(num_tickers + 1)]
            if line_count == 0:
                tickers = r
            elif line_count > 1:
                cur_yields = [log_yield(float(p1), float(p2)) for p1, p2 in zip(prev_r, r)]
                yields = np.array(cur_yields) if yields is None else np.vstack([yields, cur_yields])

            prev_r = r
            line_count += 1
    return [tickers, yields]


def draw_mst(mst):
    edges = np.vstack(mst.nonzero()).T
    g = gv.Graph('mst', engine='neato', format='png')
    for e in edges:
        g.edge(tickers[e[0]], tickers[e[1]])
    g.view()


# =======================================================

def table_setup():
    db.drop_table()
    db.new_table([
        ["market", "VARCHAR(10)"],
        ["mix_p", "DECIMAL(3, 2)"],
        ["num_obs", "INT"],
        ["pearson", "FLOAT"],
        ["sign_transform", "FLOAT"],
        ["kendall_transform", "FLOAT"],
        ["spearman_transform", "FLOAT"]
    ])

def build_mst(C):
    return csgraph.minimum_spanning_tree(-C)

def calc_err(mst1, mst2):
    m1 = 1 * (mst1.todense() < 0)
    m2 = 1 * (mst2.todense() < 0)
    return np.sum(1 * (m1 - m2 > 0))

def run_with_num_obs(market, mix_p, means, S, num_obs):
    obs = generate.normal_t_mixture(mix_p, means, S, 3, num_obs)

    pearson = stats.corr_matr(obs, stats.corr_pearson)
    sign_transform = stats.to_pearson_from_matr("sign", stats.corr_matr(obs, stats.corr_sign_no_means))
    kendall_transform = stats.to_pearson_from_matr("kendall", stats.corr_matr(obs, stats.corr_kendall))
    spearman_transform = stats.to_pearson_from_matr("spearman", stats.corr_matr(obs, stats.corr_spearman))

    # print("pearson", np.sum((pearson - S) ** 2))
    # print("sign", np.sum((sign_transform - S) ** 2))
    # print("kendall", np.sum((kendall_transform - S) ** 2))
    # print("spearman", np.sum((spearman_transform - S) ** 2))

    err_pearson = calc_err(build_mst(pearson), TRUE_MST)
    err_sign_transform = calc_err(build_mst(sign_transform), TRUE_MST)
    err_kendall_transform = calc_err(build_mst(kendall_transform), TRUE_MST)
    err_spearman_transform = calc_err(build_mst(spearman_transform), TRUE_MST)

    db.insert([
        ["market", "\"{}\"".format(market)],
        ["mix_p", mix_p],
        ["num_obs", num_obs],
        ["pearson", err_pearson],
        ["sign_transform", err_sign_transform],
        ["kendall_transform", err_kendall_transform],
        ["spearman_transform", err_spearman_transform]
    ])

def single_run():
    for mix_p in np.linspace(0, 1, 21):
        print(mix_p)
        run_with_num_obs(market, mix_p, means, C, num_obs)

# =======================================================

market = 'france'
tickers, yields = calc_yields('data/data-{}.csv'.format(market), 50)
means = np.mean(yields, 0)
C = np.corrcoef(np.transpose(yields))

TRUE_MST = build_mst(C)
# draw_mst(TRUE_MST)

table_setup()
num_obs = 250
experiment.run_x_times(10, single_run)

