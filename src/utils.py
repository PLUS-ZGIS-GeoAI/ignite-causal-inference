import cloudpickle
from dowhy import gcm

def save_model(path_to_model: str, 
               model: gcm.ProbabilisticCausalModel, 
               summary: str, 
               evaluation_report: str) -> None:
    dict_to_save = {'model': model,'summary': summary, 'evaluation_report': evaluation_report}
    with open(path_to_model , 'wb') as buff:
        cloudpickle.dump(dict_to_save, buff)

def load_model(path_to_file):
    with open(path_to_file , 'rb') as buff:
        model_dict = cloudpickle.load(buff)
    summary = model_dict['summary']
    model = model_dict['model']
    evaluation_report = model_dict['evaluation_report']
    return model, summary, evaluation_report