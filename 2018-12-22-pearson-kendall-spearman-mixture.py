import numpy as np

import fmna.experiment as exp
import fmna.generate as generate

fields = [
    ["corr_coef", "DECIMAL(3, 2)"],
    ["mix_p", "DECIMAL(3, 2)"],
    ["num_obs", "INT"]
]
table_name = exp.name().replace("-", "_")
# db.drop_table(table_name)
# db.new_table(table_name, fields)

# количество повторений
num_runs = 3
num_obs = 5

corr_coef = 0.5
###############################
means = [0, 0]
S = [[1, corr_coef], [corr_coef, 1]]

for i in range(0, num_runs):
    # параметр смеси
    for mix_p in np.linspace(0, 1, 21):
        obs = generate.normal_t_mixture(mix_p, means, S, 3, num_obs)
