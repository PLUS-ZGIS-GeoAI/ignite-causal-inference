import pandas as pd
from dowhy import gcm
import networkx as nx
import matplotlib.pyplot as plt
from causal_graph import causal_graph, causal_graph_complete
from data_preprocessing import (classify_aspect,
                                classify_canopy_cover,
                                classify_ffmc,
                                forest_type_mapping,
                                apply_encoding)
from utils import save_model


def preprocess_data(data: pd.DataFrame) -> pd.DataFrame:
    """data preprocessing - mainly classification"""

    data.dropna(subset=("forest_type", "canopy_cover"), inplace=True)
    processed_data_dict = {
        "exposition": data["aspect"].apply(classify_aspect),
        "forest_type": data['forest_type'].apply(lambda x: apply_encoding(int(x), forest_type_mapping)),
        # "ffmc": data["ffmc"].apply(classify_ffmc),
        "ffmc": data["ffmc"],
        "forest_coverage": data["canopy_cover"].apply(classify_canopy_cover),
        "fire": data["fire"].astype("str")}
    return pd.DataFrame(processed_data_dict)


def create_causal_model(causal_graph: nx.DiGraph, data: pd.DataFrame) -> gcm.ProbabilisticCausalModel:
    """create causal model and auto assign mechanisms - in future causal mechanisms can manually assigned here"""

    causal_model = gcm.ProbabilisticCausalModel(causal_graph)
    causal_mechanisms_summary = gcm.auto.assign_causal_mechanisms(
        causal_model, data)
    return causal_model, causal_mechanisms_summary


def draw_causal_graph(causal_graph: gcm.ProbabilisticCausalModel, path_to_garph_vis: str):
    """draw graph and save as figure"""

    plt.figure(figsize=(6, 4))
    nx.draw(
        G=causal_graph,
        node_size=1200,
        pos=nx.circular_layout(causal_graph))
    node_labels = {node: node for node in causal_graph.nodes()}
    nx.draw_networkx_labels(causal_graph, nx.circular_layout(
        causal_graph), labels=node_labels)
    plt.savefig(path_to_garph_vis)


def main():

    model_name = "model_v1"

    PATH_TO_DATA = r"data/data.csv"
    PATH_TO_MODEL = fr"models/{model_name}.pkl"
    PATH_TO_GRAPH_VIS = fr"models/{model_name}.png"

    data = pd.read_csv(PATH_TO_DATA)
    data_preprocessed = preprocess_data(data)
    causal_model, causal_mechanisms_summary = create_causal_model(
        causal_graph, data_preprocessed)
    draw_causal_graph(causal_graph, PATH_TO_GRAPH_VIS)
    gcm.fit(causal_model, data_preprocessed)
    evaluation_report = gcm.evaluate_causal_model(
        causal_model, data_preprocessed, compare_mechanism_baselines=True, evaluate_invertibility_assumptions=False)
    save_model(PATH_TO_MODEL, causal_model,
               causal_mechanisms_summary, evaluation_report)


if __name__ == "__main__":
    main()
