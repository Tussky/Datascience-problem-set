import pandas as pd
import numpy as np
from scipy.signal import find_peaks
from collections import Counter

def channel_to_df(channel: pd.Series) -> pd.DataFrame:
    """
    For quick plotting, calculates the length which most columns share in common, 
    converts this to a dataframe.
    """
    lengths = []
    for item in channel:
        lengths.append(len(item))

    count = Counter(lengths)
    desired_len = count.most_common()[0][1]

    same_lengths = channel[[item for item in channel.keys() if len(item) == desired_len]]
    df = pd.DataFrame(
        data = same_lengths.to_dict()
    )
    return df
