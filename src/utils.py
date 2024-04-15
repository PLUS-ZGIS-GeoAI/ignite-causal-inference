import cloudpickle
from dowhy import gcm

def save_model(path_to_model: str, model: gcm.ProbabilisticCausalModel, summary: str) -> None:
    dict_to_save = {'model': model,'summary': summary}
    with open(path_to_model , 'wb') as buff:
        cloudpickle.dump(dict_to_save, buff)

def load_model(path_to_file):
    with open(path_to_file , 'rb') as buff:
        model_dict = cloudpickle.load(buff)
    summary = model_dict['summary']
    model = model_dict['model']
    return model, summary