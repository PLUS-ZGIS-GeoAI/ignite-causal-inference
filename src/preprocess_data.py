import pandas as pd
import geopandas as gpd
from preprocessing_functions import (classify_aspect,
                                    classify_canopy_cover,
                                    forest_type_mapping,
                                    apply_encoding, 
                                    classify_population, 
                                    classify_elevation,
                                    classify_slope,
                                    map_to_binary, 
                                    temporal_train_test_split)


def preprocess_data(data: pd.DataFrame) -> pd.DataFrame:
    """data preprocessing - mainly classification"""

    data.rename(columns={"farmyard_d": "farmyard_density", 
                         "hiking_ds": "hikingtrail_density", 
                         "forest_ds": "forestroad_density", 
                         "rail_dens": "railway_density", 
                         "foresttype": "forest_type", 
                         "pop_dens": "population_density", 
                         "canopy_cov": "canopy_coverage"}, inplace=True)

    data.dropna(subset=("forest_type", "canopy_coverage"), inplace=True)
    processed_data_dict = {

        "date": data["date"],
        "loc_uncertainty": data["Pufferradi"],

        "exposition": data["aspect"].apply(classify_aspect),
        "elevation": data["elevation"].apply(classify_elevation),
        "slope": data["slope"].apply(classify_slope),

        "farmyard": data["farmyard_density"].apply(map_to_binary),
        "forestroad": data["forestroad_density"].apply(map_to_binary),
        "railway": data["railway_density"].apply(map_to_binary),
        "hikingtrail": data["hikingtrail_density"].apply(map_to_binary),
        "population": data["population_density"].apply(classify_population),

        "forest_type": data['forest_type'].apply(lambda x: apply_encoding(int(x), forest_type_mapping)),
        "forest_coverage": data["canopy_coverage"].apply(classify_canopy_cover),

        "ffmc": data["ffmc"],
        "fire": data["fire"].astype("str")}
    return pd.DataFrame(processed_data_dict)



if __name__ == "__main__":

    # read in training data
    path_to_observational_data = r"data/data_all_factors/training_data.shp"
    obs_data_raw = gpd.read_file(path_to_observational_data)
    obs_data_raw.date = pd.to_datetime(obs_data_raw.date)

    # preprocess data
    data_obs_prep = preprocess_data(obs_data_raw)

    # split both datasets temporally into train and test set 
    data_train, data_test = temporal_train_test_split(data_obs_prep, "date", 0.7)

    # save data
    data_train.to_csv(r"data/data_prep/data_train.csv")
    data_test.to_csv(r"data/data_prep/data_test.csv")