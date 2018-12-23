import fmna.generate as generate
import fmna.stats as stats

corr_coef = 0.5
means = [0, 0]
S = [[1, corr_coef], [corr_coef, 1]]

obs = generate.multivariate_normal(means, S, 1000000)
#obs = generate.multivariate_t(means, S, 3, 1000000)

pearson = stats.corr_pearson(obs[:, 0], obs[:, 1])
sign = stats.corr_sign(obs[:, 0], obs[:, 1])
sign_no_means = stats.corr_sign_no_means(obs[:, 0], obs[:, 1])
tau = stats.corr_kendall(obs[:, 0], obs[:, 1])
spearman = stats.corr_spearman(obs[:, 0], obs[:, 1])

print(pearson,
      stats.to_pearson_from("sign", sign),
      stats.to_pearson_from("sign", sign_no_means),
      stats.to_pearson_from("kendall", tau),
      stats.to_pearson_from("spearman", spearman))
