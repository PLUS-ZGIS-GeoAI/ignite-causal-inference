import networkx as nx


def create_causal_graph():
    edges_ls = []
    topo_factors = ["elevation", "slope", "exposition"]
    human_factors = ["forestroad", "hikingtrail", "railway", "farmyard", "population"]
    forest_factors = ["forest_coverage", "forest_type"]

    # draw connections from topogrpahical features
    for topo_factor in topo_factors:
        for factor in forest_factors:
            edges_ls.append((topo_factor, factor))
        edges_ls.append((topo_factor, "fire"))
    edges_ls.append(("elevation", "population"))

    # draw connections from human features
    for human_factor in human_factors:
        if human_factor is not "population":
            edges_ls.append(("population", human_factor))
        edges_ls.append((human_factor, "forest_coverage"))
        edges_ls.append((human_factor, "fire"))

    # draw all else connections
    edges_ls.append(("forest_type", "fire"))
    edges_ls.append(("forest_type", "forest_coverage"))
    edges_ls.append(("forest_coverage", "fire"))
    edges_ls.append(("ffmc", "fire"))

    return nx.DiGraph(edges_ls)


def create_simplified_causal_graph():
    """create simplified version of causal graph above"""

    edge_topo_forest = ("Topography", "Forest Characteristics")
    edge_topo_human = ("Topography", "Human Factors")
    edge_topo_fire = ("Topography", "Fire")
    edge_human_forest = ("Human Factors", "Forest Characteristics")
    edge_human_fire = ("Human Factors", "Fire")
    edge_forest_fire = ("Forest Characteristics", "Fire")
    # edge_ffmc_fire = ("FFMC", "Fire")

    return nx.DiGraph(
        [
            edge_topo_forest,
            edge_topo_human,
            edge_topo_fire,
            edge_human_forest,
            edge_human_fire,
            edge_forest_fire,
            # edge_ffmc_fire,
        ]
    )


def create_causasl_graph_without_FFMC():
    edges_ls = []
    topo_factors = ["elevation", "slope", "exposition"]
    human_factors = ["forestroad", "hikingtrail", "railway", "farmyard", "population"]
    forest_factors = ["forest_coverage", "forest_type"]

    # draw connections from topogrpahical features
    for topo_factor in topo_factors:
        for factor in forest_factors:
            edges_ls.append((topo_factor, factor))
        edges_ls.append((topo_factor, "fire"))
    edges_ls.append(("elevation", "population"))

    # draw connections from human features
    for human_factor in human_factors:
        if human_factor is not "population":
            edges_ls.append(("population", human_factor))
        edges_ls.append((human_factor, "forest_coverage"))
        edges_ls.append((human_factor, "fire"))

    # draw all else connections
    edges_ls.append(("forest_type", "fire"))
    edges_ls.append(("forest_type", "forest_coverage"))
    edges_ls.append(("forest_coverage", "fire"))

    return nx.DiGraph(edges_ls)


def create_exposition_forest_type_causal_graph():
    """create simplified version of causal graph above"""

    edge_topo_forest = ("Exposition", "Forest Type")
    edge_topo_fire = ("Exposition", "Fire")
    edge_forest_fire = ("Forest Type", "Fire")

    return nx.DiGraph(
        [
            edge_topo_forest,
            edge_topo_fire,
            edge_forest_fire,
        ]
    )


"""
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



def create_causal_graph_all_factors():
    edges_ls = []
    topo_factors = ["elevation", "slope", "exposition"]
    weather_factors = ["temperature", "precipitation", "humidity", "wind"]
    human_factors = ["forestroad", "hikingtrail", "railway", "farmyard", ]
    forest_factors = ["forest_coverage", "forest_type"]

    for topo_factor in topo_factors:
        other_factors = weather_factors + human_factors + forest_factors
        for factor in other_factors:
            edges_ls.append((topo_factor, factor))
        edges_ls.append((topo_factor, "fire"))
    
    for human_factor in human_factors:
        edges_ls.append((human_factor, "forest_coverage"))
        edges_ls.append((human_factor, "fire"))
    
    for weather_factor in weather_factors:
        edges_ls.append((weather_factor, "ffmc"))
        edges_ls.append((weather_factor, "fire"))
    
    edges_ls.append(("forest_coverage", "fire"))
    edges_ls.append(("ffmc", "fire"))
    edges_ls.append(("forest_type", "fire"))
    edges_ls.append(("forest_type", "forest_coverage"))

    return nx.DiGraph(edges_ls)
"""
