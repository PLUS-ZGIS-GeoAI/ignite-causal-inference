
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


def apply_encoding(original_value: str, mapping: dict):
    """encodes nuts id to numerical id

    Args:
        original_value (str)
        mapping (dict): defines mapping between original value and encoded value
    """

    return mapping[original_value]


forest_type_mapping = {
    0: "coniferous non pine",
    1: "coniferous with mixed pine",
    2: "pine pure",
    3: "coniferous deciduous mixed with pine",
    4: "coniferous deciduous mixed non pine",
    5: "deciduous pure",
    6: "low and no vegetation"
}