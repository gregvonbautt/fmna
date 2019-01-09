from fmna import db, generate, stats, graph, experiment


def table_setup():
    db.drop_table()
    db.new_table([
        ["pearson", "FLOAT"],
        ["sign_transform", "FLOAT"],
        ["kendall_transform", "FLOAT"],
        ["spearman_transform", "FLOAT"]
    ])


def gen(means, S, num_obs):
    return generate.multivariate_t(means, S, 3, num_obs)
    # return generate.multivariate_normal(means, S, num_obs)


def single_run():
    means = [0, 0]
    corr_coef = 0.5
    num_obs = 90
    S = [[1, corr_coef], [corr_coef, 1]]

    obs = gen(means, S, num_obs)
    pearson = stats.corr_pearson(obs[:, 0], obs[:, 1])

    obs = gen(means, S, num_obs)
    sign_transform = stats.to_pearson_from("sign", stats.corr_sign_no_means(obs[:, 0], obs[:, 1]))

    obs = gen(means, S, num_obs)
    kendall_transform = stats.to_pearson_from("kendall", stats.corr_kendall(obs[:, 0], obs[:, 1]))

    obs = gen(means, S, num_obs)
    spearman_transform = stats.to_pearson_from("spearman", stats.corr_spearman(obs[:, 0], obs[:, 1]))

    db.insert([
        ["pearson", pearson],
        ["sign_transform", sign_transform],
        ["kendall_transform", kendall_transform],
        ["spearman_transform", spearman_transform]
    ])


def results():
    res = db.load()
    graph.simple_scatter("Standard Estimator", list(map(lambda l: l[1], res)), [-1, 1])
    graph.simple_scatter("Sign Transform", list(map(lambda l: l[2], res)), [-1, 1])
    graph.simple_scatter("Kendall Tau Transform", list(map(lambda l: l[3], res)), [-1, 1])
    graph.simple_scatter("Spearman Transform", list(map(lambda l: l[4], res)), [-1, 1])


table_setup()
experiment.run_x_times(3000, single_run)
results()
