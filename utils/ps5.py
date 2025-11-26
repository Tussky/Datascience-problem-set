import pandas as pd
import numpy as np
from scipy.signal import find_peaks
from collections import Counter

def channel_to_df(channel: pd.Series) -> pd.DataFrame:
    """
    For quick plotting, calculates the length which most columns share in common, 
    converts this to a dataframe.
    """
    unwanted = ['edges','peak_locs', 'energy']

    same_lengths = channel[[item for item in channel.keys() if item not in unwanted]]
    df = pd.DataFrame(
        data = same_lengths.to_dict()
    )
    return df
