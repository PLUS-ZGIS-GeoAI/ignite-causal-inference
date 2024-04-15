import networkx as nx

causal_graph = nx.DiGraph([('exposition', 'forest_type'), 
                           ('exposition', 'forest_coverage'),
                           ('exposition', 'ffmc'),  
                           ('exposition', 'fire'), 
                           ('forest_coverage', 'fire'), 
                           ('forest_type', 'fire'), 
                           ('ffmc', 'fire'), 
                           ('forest_type', 'forest_coverage')])