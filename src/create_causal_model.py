import pandas as pd
from dowhy import gcm
import networkx as nx
from causal_graph import create_causal_graph
from utils import save_model


def create_causal_model(causal_graph: nx.DiGraph, data: pd.DataFrame) -> gcm.ProbabilisticCausalModel:
    """create causal model and auto assign mechanisms - in future causal mechanisms can manually assigned here"""

    causal_model = gcm.ProbabilisticCausalModel(causal_graph)
    causal_mechanisms_summary = gcm.auto.assign_causal_mechanisms(
        causal_model, data)
    return causal_model, causal_mechanisms_summary


def main():

    model_name = "model_all_data"
    PATH_TO_DATA = r"data/data_prep/data_train_all_data.csv"
    PATH_TO_MODEL = fr"models/{model_name}.pkl"

    data = pd.read_csv(PATH_TO_DATA)
    causal_graph = create_causal_graph()
    causal_model, causal_mechanisms_summary = create_causal_model(causal_graph, data)
    gcm.fit(causal_model, data)
    evaluation_report = gcm.evaluate_causal_model(causal_model, 
                                                  data, 
                                                  compare_mechanism_baselines=True, 
                                                  evaluate_invertibility_assumptions=False)
    save_model(PATH_TO_MODEL, 
               causal_model,
               causal_mechanisms_summary, 
               evaluation_report)


if __name__ == "__main__":
    main()
