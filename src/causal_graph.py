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
