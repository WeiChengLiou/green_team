##
from vis.output import exp_graph, write_d3
import pandas as pd
import json
import networkx as nx
import numpy as np

fi = 'G1101_2016_list.json'
ret = json.loads(open(fi).read())

##
df = pd.DataFrame(ret)
coms = pd.concat([
    (df[['source', 'taxcode_source']]
     .drop_duplicates()
     .rename(columns={
         'source': 'com',
         'taxcode_source': 'taxcode',
     })
    ),
    (df[['target', 'taxcode_target']]
     .drop_duplicates()
     .rename(columns={
         'target': 'com',
         'taxcode_target': 'taxcode',
     })
    ),
])
coms = coms.drop_duplicates()


##
G = nx.DiGraph()
for x in ret:
    G.add_edge(x['source'], x['target'])

print('Nodes: %d' % G.number_of_nodes())
print('Edges: %d' % G.number_of_edges())

##
for x in coms.itertuples():
    G.node[x.com]['name'] = x.com
    G.node[x.com]['group'] = int(x.taxcode == 'NA')


##
exp_graph(G, fi='output')
write_d3('output')

##
