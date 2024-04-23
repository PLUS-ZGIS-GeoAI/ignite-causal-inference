
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from dowhy import gcm
from utils import load_model


def construct_ate_dict(exposition_classes, ref_value):
    ate_dict = {"ref_value": ref_value, "ate": {}}  
    for region in exposition_classes:
        ate_dict["ate"][region] = {}
    return ate_dict

def get_ate_with_confidence_for_factor_classes(ate_dict: dict, factor_name: str, causal_model):
    for cl in ate_dict["ate"].keys():
        effect_median, effect_interval = gcm.confidence_intervals(
            gcm.bootstrap_sampling(gcm.average_causal_effect, 
                                causal_model, "fire", 
                                interventions_alternative={factor_name: lambda x: cl},
                                interventions_reference={factor_name: lambda x: ate_dict["ref_value"]}, 
                                num_samples_to_draw=1000))
        ate_dict["ate"][cl]["median"] = effect_median[0]
        ate_dict["ate"][cl]["interval"] = effect_interval[0]
    return ate_dict

def save_plot_ate_with_confidence(ate_data, path_to_file):
    regions = list(ate_data['ate'].keys())
    ate_values = [ate_data['ate'][region]['median'] for region in regions]
    lower_bounds = [ate_data['ate'][region]['interval'][0] for region in regions]
    upper_bounds = [ate_data['ate'][region]['interval'][1] for region in regions]
    fig, ax = plt.subplots()
    y_pos = np.arange(len(regions))
    ax.errorbar(ate_values, y_pos, xerr=[np.array(ate_values) - np.array(lower_bounds), np.array(upper_bounds) - np.array(ate_values)],
                fmt='o', color='black', capsize=5, markersize=5)
    ax.set_yticks(y_pos)
    ax.set_yticklabels(regions)
    ax.axvline(x=0, color='gray', linestyle='--')
    ax.set_xlabel('ATE')
    ax.set_title('Average Treatment Effect (ATE) with Confidence Intervals')
    plt.savefig(path_to_file)


if __name__ == "__main__":

    experiment = "all_data"
    causal_model, causal_mechanisms_summary, eval_summary = load_model(rf"models/model_{experiment}pkl")
    data_obs_prep = pd.read_csv(rf"data/data_prep/data_train_{experiment}.csv")

    forest_cover_classes = ["cc<=20", "20<cc<=40", "40<cc<=60", "60<cc<=80", "cc>80"]
    exposition_classes = ["N", "NE", "E", "SE", "S", "SW", "W", "NW"]
    forest_type_classes = ["coniferous non pine", "coniferous with mixed pine", "pine pure", 
                        "coniferous deciduous mixed with pine", "coniferous deciduous mixed non pine", "deciduous pure", "low and no vegetation"]
    
    # estimate ATE for exposition
    ate_dict_exposition = construct_ate_dict(exposition_classes, "E")
    for exp in exposition_classes:
        effect_median, effect_interval = gcm.confidence_intervals(
                    gcm.bootstrap_sampling(gcm.average_causal_effect, 
                                        causal_model, "fire", 
                                        interventions_alternative={'exposition': lambda x: exp, 
                                                            'forest_type': lambda x: "pine pure", 
                                                            'forest_coverage': lambda x: "40<cc<=60"},
                                        interventions_reference={'exposition': lambda x: "E", 
                                                        'forest_type': lambda x: "pine pure",
                                                        'forest_coverage': lambda x: "40<cc<=60"},
                                        observed_data=data_obs_prep))
        
        ate_dict_exposition["ate"][exp]["median"] = effect_median[0]
        ate_dict_exposition["ate"][exp]["interval"] = effect_interval[0]
    save_plot_ate_with_confidence(ate_dict_exposition, f"results/ate_exposition_{experiment}.png")

    
    # estimate ATE for forest type
    ate_dict_foresttype = construct_ate_dict(forest_type_classes, "coniferous non pine")
    for ft in forest_type_classes:
        effect_median, effect_interval = gcm.confidence_intervals(
                    gcm.bootstrap_sampling(gcm.average_causal_effect, 
                                        causal_model, "fire", 
                                        interventions_alternative={'forest_type': lambda x: ft, 
                                                            'forest_coverage': lambda x: "40<cc<=60"},
                                        interventions_reference={'forest_type': lambda x: "coniferous non pine", 
                                                        'forest_coverage': lambda x: "40<cc<=60"},
                                        observed_data=data_obs_prep))
        ate_dict_foresttype["ate"][ft]["median"] = effect_median[0]
        ate_dict_foresttype["ate"][ft]["interval"] = effect_interval[0]
    save_plot_ate_with_confidence(ate_dict_foresttype, f"results/ate_forest_type_{experiment}.png")


    # estimate ATE for forest coverage
    ate_dict_forestcoverage = construct_ate_dict(forest_cover_classes, "40<cc<=60")
    for fcc in forest_cover_classes:
        effect_median, effect_interval = gcm.confidence_intervals(
                    gcm.bootstrap_sampling(gcm.average_causal_effect, 
                                        causal_model, "fire", 
                                        interventions_alternative={'forest_coverage': lambda x: fcc},
                                        interventions_reference={'forest_coverage': lambda x: "40<cc<=60"},
                                        observed_data=data_obs_prep))
        ate_dict_forestcoverage["ate"][fcc]["median"] = effect_median[0]
        ate_dict_forestcoverage["ate"][fcc]["interval"] = effect_interval[0]
    save_plot_ate_with_confidence(ate_dict_forestcoverage, f"results/ate_forest_coverage_{experiment}.png")