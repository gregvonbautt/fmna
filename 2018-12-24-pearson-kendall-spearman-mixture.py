import numpy as np

from fmna import db, generate, stats, experiment, graph


def table_setup():
    db.drop_table()
    db.new_table([
        ["mix_p", "DECIMAL(3, 2)"],
        ["num_obs", "INT"],
        ["pearson", "FLOAT"],
        ["sign_transform", "FLOAT"],
        ["kendall_transform", "FLOAT"],
        ["spearman_transform", "FLOAT"]
    ])


def run_with_num_obs(mix_p, means, S, num_obs):
    obs = generate.normal_t_mixture(mix_p, means, S, 3, num_obs)

    pearson = stats.corr_pearson(obs[:, 0], obs[:, 1])
    sign_transform = stats.to_pearson_from("sign", stats.corr_sign_no_means(obs[:, 0], obs[:, 1]))
    kendall_transform = stats.to_pearson_from("kendall", stats.corr_kendall(obs[:, 0], obs[:, 1]))
    spearman_transform = stats.to_pearson_from("spearman", stats.corr_spearman(obs[:, 0], obs[:, 1]))

    db.insert([
        ["mix_p", mix_p],
        ["num_obs", num_obs],
        ["pearson", pearson],
        ["sign_transform", sign_transform],
        ["kendall_transform", kendall_transform],
        ["spearman_transform", spearman_transform]
    ])


def single_run():
    means = [0, 0]
    corr_coef = 0.5
    S = [[1, corr_coef], [corr_coef, 1]]

    for mix_p in np.linspace(0, 1, 21):
        run_with_num_obs(mix_p, means, S, 50)
        run_with_num_obs(mix_p, means, S, 90)


def count(num_obs, cond):
    table = experiment.table_name()
    select = "SELECT DISTINCT A.mix_p, COALESCE(B.cnt, 0) FROM %s A " \
             "LEFT JOIN (SELECT mix_p, COUNT(*) AS cnt FROM %s " \
             "WHERE num_obs=%i AND %s GROUP BY (mix_p)) B " \
             "ON A.mix_p = B.mix_p " \
             "ORDER BY A.mix_p" % (table, table, num_obs, cond)
    return db.arbitrary_select(select)


def build_graphs(title, values):
    graph.simple_graph(title, list(map(lambda v: [
        list(map(lambda a: a[0], v[0])), list(map(lambda a: a[1], v[0])), v[1]
    ], values)), [0, 1], [0, 1000])


def build_for_num_obs_and_threshold(num_obs, threshold, cond):
    build_graphs("%s observations, threshold %s" % (num_obs, threshold), [
        [count(num_obs, "pearson %s" % cond), "Pearson"],
        [count(num_obs, "sign_transform %s" % cond), "Sign Transform"],
        [count(num_obs, "kendall_transform %s" % cond), "Kendall Transform"],
        [count(num_obs, "spearman_transform %s" % cond), "Spearman Transform"],
    ]);


def results():
    build_for_num_obs_and_threshold(50, "0.25", "< 0.25")
    build_for_num_obs_and_threshold(50, "0.75", "> 0.75")

    build_for_num_obs_and_threshold(50, "0.4", "< 0.4")
    build_for_num_obs_and_threshold(50, "0.6", "> 0.6")

    build_for_num_obs_and_threshold(90, "0.25", "< 0.25")
    build_for_num_obs_and_threshold(90, "0.75", "> 0.75")

    build_for_num_obs_and_threshold(90, "0.4", "< 0.4")
    build_for_num_obs_and_threshold(90, "0.6", "> 0.6")


# table_setup()
# experiment.run_x_times(3000, single_run)
results()
