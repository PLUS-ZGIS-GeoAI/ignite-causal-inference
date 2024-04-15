from dowhy import gcm
from src.causal_graph import causal_graph


def load_data():
    x = 2
    return x


if __name__ == "__main__":

    causal_model = gcm.ProbabilisticCausalModel(causal_graph)
    #causal_mechanisms_summary = gcm.auto.assign_causal_mechanisms(causal_model, X)
    #X = load_data()
    #gcm.fit(causal_model, X)

