import csv, math, numpy as np, scipy.sparse.csgraph as csgraph
import matplotlib.pyplot as plt
import networkx as nx

import graphviz as gv

def log_yield(p1, p2):
    return math.log(p2 / p1)
    #return p2 / p1

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


tickers, yields = calc_yields('data/data-russia.csv', 50)

C1 = np.cov(np.transpose(yields))
C2 = np.corrcoef(np.transpose(yields))

mst = csgraph.minimum_spanning_tree(-C2)
edges = np.vstack(mst.nonzero()).T


g = gv.Graph('mst', engine='neato', format='png')
for e in edges:
    g.edge(tickers[e[0]], tickers[e[1]])
g.view()

# g = nx.Graph()
# for t in tickers:
#     g.add_node(t)
# for e in edges:
#     g.add_edge(tickers[e[0]], tickers[e[1]])
# nx.draw_networkx(g)
# plt.show()