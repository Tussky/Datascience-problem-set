import pandas as pd
import numpy as np
from scipy.signal import find_peaks

def channel_to_df(channel: pd.Series) -> pd.DataFrame:
    """
    Used mainly for quick plotting
    Will drop the last element in edges
    """
    same_lengths = channel[[item for item in channel.keys() if item not in ['edges','peak_vals'] ]]
    df = pd.DataFrame(
        data = same_lengths.to_dict()
    )
    return df
