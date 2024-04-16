import networkx as nx
import matplotlib.pyplot as plt

causal_graph = nx.DiGraph([('exposition', 'forest_type'),
                           ('exposition', 'forest_coverage'),
                           ('exposition', 'ffmc'),
                           ('exposition', 'fire'),
                           ('forest_coverage', 'fire'),
                           ('forest_type', 'fire'),
                           ('ffmc', 'fire'),
                           ('forest_type', 'forest_coverage')])


causal_graph_complete = nx.DiGraph([('exposition', 'forest_type'),
                                    ('exposition', 'forest_coverage'),
                                    ('exposition', 'ffmc'),
                                    ('exposition', 'solar_radiation'),
                                    ('forest_coverage', 'solar_radiation'),
                                    ('forest_coverage', 'streuschicht'),
                                    ('forest_type', 'solar_radiation'),
                                    ('forest_type', 'streuschicht'),
                                    ('forest_type', 'forest_coverage'),
                                    ('ffmc', 'streuschicht'),
                                    ('ffmc', 'solar_radiation'),
                                    ('streuschicht', 'fire'),
                                    ('solar_radiation', "fire")])
