import pandas as pd

def classify_canopy_cover(cc: float) -> str:
    """categorization of canopy cover into classes based on boku document for ffmc overprint

    Args:
         cc (float): canopy cover in %

    Returns:
        str: canopy cover encoded
    """

    if (cc <= 20):
        return "cc<=20"
    elif (cc > 20) & (cc <= 40):
        return "20<cc<=40"
    elif (cc > 40) & (cc <= 60):
        return "40<cc<=60"
    elif (cc > 60) & (cc <= 80):
        return "60<cc<=80"
    elif (cc > 80):
        return "cc>80"
    else:
        return "None"


def classify_ffmc(cc: float) -> str:
    """categorization of ffmc into classes based on boku document for ffmc overprint

    Args:
         ffmc (float): fine fuel moisture code

    Returns:
        str: ffmc encoded
    """

    if (cc < 78):
        return "ffmc<78"
    elif (cc >= 78) & (cc < 87):
        return "78<=ffmc<87"
    elif (cc >= 87) & (cc < 91):
        return "87<=ffmc<91"
    elif (cc >= 91) & (cc < 93):
        return "91<=ffmc<93"
    elif (cc >= 93):
        return "ffmc>=93"
    else:
        return "None"


def classify_aspect(aspect: float) -> str:
    """converts aspect degree values to cardinal direction classes

    Args:
        aspect (float): value between 0 and 360, indicating exposition of slope

    Returns:
        (str): cardinal direction class
    """
    if (aspect >= 337.5) | (aspect < 22.5):
        return "N"
    elif (aspect >= 22.5) & (aspect < 67.5):
        return "NE"
    elif (aspect >= 67.5) & (aspect < 112.5):
        return "E"
    elif (aspect >= 112.5) & (aspect < 157.5):
        return "SE"
    elif (aspect >= 157.5) & (aspect < 202.5):
        return "S"
    elif (aspect >= 202.5) & (aspect < 247.5):
        return "SW"
    elif (aspect >= 247.5) & (aspect < 292.5):
        return "W"
    elif (aspect >= 292.5) & (aspect < 337.5):
        return "NW"
    else:
        return "None"



def classify_population(population: float) -> int:
    """categorization of population into classes after www.statistik.at

    Args:
        population (float): population density (nr of people per km2)

    Returns:
        int: population encoded
    """

    if (population == 0):
        return "0"
    elif (population > 0) & (population <= 50):
        return "0-50 P/km2"
    elif (population > 50) & (population <= 100):
        return "50-100 P/km2"
    elif (population > 100) & (population <= 500):
        return "100-500 P/km2"
    elif (population > 500) & (population <= 1000):
        return "500-1000 P/km2"
    elif (population > 1000):
        return ">1000 P/km2"
    else: 
        return "None"


def classify_slope(slope: float) -> str:
    """categorization of slope into classes after Müller & Vacik (2020)

    Args:
        slope (float): inclination in ° (ranges from 0-90)

    Returns:
        str: slope encoded
    """

    if (slope < 10):
        return "<10%"
    elif (slope >= 10) & (slope < 20):
        return "10-20"
    elif (slope >= 20) & (slope < 30):
        return "20-30"
    elif (slope >= 30) & (slope < 40):
        return "30-40"
    elif (slope >= 40):
        return ">=40%"
    else: 
        return "None"
    

def classify_elevation(elevation: float) -> str:
    """categorization of elevation into classes after Müller & Vacik (2020)

    Args:
        elevation (float): elevation in meter a.s.l

    Returns:
        str: elevation encoded
    """

    if (elevation < 500):
        return "<500"
    elif (elevation >= 500) & (elevation < 800):
        return "500-800"
    elif (elevation >= 800) & (elevation < 1500):
        return "800-1500"
    elif (elevation >= 1500) & (elevation < 1800):
        return "1500-1800"
    elif (elevation >= 1800) & (elevation < 2200):
        return "1800-2200"
    elif (elevation >= 2200):
        return ">=2200"
    else:
        return "None"


def apply_encoding(original_value: str, mapping: dict):
    """encodes nuts id to numerical id

    Args:
        original_value (str)
        mapping (dict): defines mapping between original value and encoded value
    """

    return mapping[original_value]


def map_to_binary(x):
    return "Yes" if x > 0 else "No"


forest_type_mapping = {
    0: "coniferous non pine",
    1: "coniferous with mixed pine",
    2: "pine pure",
    3: "coniferous deciduous mixed with pine",
    4: "coniferous deciduous mixed non pine",
    5: "deciduous pure",
    6: "low and no vegetation"
}


def temporal_train_test_split(train_data: pd.DataFrame, date_col: str, train_size: float) -> tuple:
    """function splits dataframe into train and test dataframe. Split criteria is the date. Newer samples are contained in the testset. Older samples in the training set.
    Args:
        train_data (pd.DataFrame): Training data set that shall be splitted into training and test set
        date_col (str): date column, which will be used to split data by time
        train_size (float): size (%) of training dataset
    Returns:
        tuple: tuple contains two dataframes -> training and test set
    """
    train_data[date_col] = pd.to_datetime(train_data.date)
    train_data = train_data.sort_values(by=date_col)
    split_index = int(train_size * len(train_data))
    train_df = train_data.iloc[:split_index]
    test_df = train_data.iloc[split_index:]
    return train_df, test_df
