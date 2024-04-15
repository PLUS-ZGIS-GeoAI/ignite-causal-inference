import pandas as pd
from dowhy import gcm
import networkx as nx
from causal_graph import causal_graph
import cloudpickle
from data_preprocessing import (classify_aspect, 
                                classify_canopy_cover, 
                                classify_ffmc, 
                                forest_type_mapping, 
                                apply_encoding)

PATH_TO_DATA = r"data/data.csv"
PATH_TO_MODEL = r"models/model_v1.pkl"

def preprocess_data(data: pd.DataFrame) -> pd.DataFrame:
    data.dropna(subset=("forest_type", "canopy_cover"), inplace=True)
    processed_data_dict = {
        "exposition": data["aspect"].apply(classify_aspect),
        "forest_type": data['forest_type'].apply(lambda x: apply_encoding(int(x), forest_type_mapping)),
        "ffmc": data["ffmc"].apply(classify_ffmc),
        "forest_coverage": data["canopy_cover"].apply(classify_canopy_cover),
        "fire": data["fire"].astype("str")}
    return pd.DataFrame(processed_data_dict)

def create_causal_model(causal_graph: nx.DiGraph, data: pd.DataFrame) -> gcm.ProbabilisticCausalModel:
    causal_model = gcm.ProbabilisticCausalModel(causal_graph)
    causal_mechanisms_summary = gcm.auto.assign_causal_mechanisms(causal_model, data)
    return causal_model, causal_mechanisms_summary

def save_model(path_to_model: str, model: gcm.ProbabilisticCausalModel, summary: str) -> None:
    dict_to_save = {'model': model,'summary': summary}
    with open(path_to_model , 'wb') as buff:
        cloudpickle.dump(dict_to_save, buff)


def main():
    data = pd.read_csv(PATH_TO_DATA)
    data_preprocessed = preprocess_data(data)
    causal_model, causal_mechanisms_summary = create_causal_model(causal_graph, data_preprocessed)
    gcm.fit(causal_model, data_preprocessed)
    save_model(PATH_TO_MODEL, causal_model, causal_mechanisms_summary)

if __name__ == "__main__":
    main()

