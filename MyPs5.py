# %% [markdown]
# # Spectral Co-Adding
#
# Name: Isaac Anderson
#
# Date: 20th Nov 2025

# %% [markdown]
# ### Peak Finding
# 1. Use the best peak-finding tools from class to find the same 5 most prominent peaks in every channel within one data file (this may involve finding more than 5 peaks and figuring out an algorithm to find which peaks should map to which.)

# %% [markdown]
# #### Reading in files and necessary packages.
import h5py
import nbformat
import plotly.express as px
import plotly.graph_objects as go
import pandas as pd
import numpy as np
from scipy.signal import find_peaks
from utils.ps5 import channel_to_df

filename = "./../Data/Gamma/210601_NBS295-106/20210601_152616_mass-001.hdf5"
with h5py.File(filename, "r") as hdf_file:
    channels = pd.DataFrame(
        columns=["energy"],
        index=hdf_file.keys(),
    )

    for channel_name in hdf_file:
        going_in = np.array(hdf_file[channel_name]["filt_value"])
        going_in = going_in[(0 < going_in) & (going_in < np.percentile(going_in, 99))]
        channels.loc[channel_name] = [going_in]


# %% [markdown]
# #### Histograming & columns
# %%
# important channel information
channels["counts"], channels["edges"] = zip(
    *channels["energy"].apply(np.histogram, args=(10_000,))
)
channels["midpoints"] = [
    0.5 * (channel_edges[1:] + channel_edges[:-1])
    for channel_edges in channels["edges"]
]


# %%
# finding peaks
peaks, peaks_data = zip(*channels["counts"].apply(find_peaks, prominence=4))
peaks = pd.Series(peaks)
peaks_data = pd.Series(peaks_data)
eight_peaks = peaks_data.str['prominences'].apply(np.argsort).str[:8]
channels["prominent_peaks"] = [
    peaks[index][prominent_peak] for index, prominent_peak in enumerate(eight_peaks)
]
channels["prominent_peak_data"] = [
    peaks_data[index]["prominences"] for index, peak_data in enumerate(eight_peaks)
]

# %% 
# Saving popular channels for quick use
chan1 = channels.loc["chan1"]
chan99 = channels.loc["chan99"]
# %%
# Finding the matching peaks 
# %%
# 2. Fit these peaks with a Gaussian on top of a linear background.

# %% [markdown]
# ### Traditional Analysis
# 3. Using splines with 5 peaks, co-add all the channels within one data file.
# 4. Fit the most prominent peak of each individual spectrum after scaling it. Divide the Gaussian mean by the Gaussian width ($\sigma$) and histogram this quantity (which we will refer to as the signal to noise ratio or SNR).
# 5. Add up all the spectra and fit the most prominent peak of the summed spectrum. Plot the SNR as a vertical dashed line on the SNR histogram from #2.
# 6. Repeat steps 2 and 3 for a peak that is 2 orders of magnitude smaller (i.e. 100 times less area)

# %% [markdown]
# ### DTW Analysis
# 7. Use the DTW approach on all the channels within one data file to co-add them.
# 8. Fit the most prominent peak of each individual spectrum after scaling it. Divide the Gaussian mean by the Gaussian width ($\sigma$) and histogram this quantity (which we will refer to as the signal to noise ratio or SNR).
# 9. Add up all the spectra and fit the most prominent peak of the summed spectrum. Plot the SNR as a vertical dashed line on the SNR histogram from #2.
# 10. Repeat steps 2 and 3 for a peak that is 2 orders of magnitude smaller (i.e. 100 times less area)

# %% [markdown]
# ## Side Quest -- DTW Optimization
#
# Repeat steps 7-10 and optimize the various DTW options:
# ```
# alignment_windowed = dtw(s1, s2, keep_internals=True,
#                          window_type="sakoechiba", window_args={'window_size': 2})
# ```

# %% [markdown]
# ## Side Quest -- Wavelets for Drift Correction
#
# Inverse of noise reduction. We're keeping the noise, but removing the slow time constant terms!
