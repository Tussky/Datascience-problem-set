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
with h5py.File(filename, 'r') as hdf_file:
    channels = pd.DataFrame(
        columns = ['peak_vals'],
        index = hdf_file.keys(),
    )
    
    for channel_name in hdf_file:
        channels.loc[channel_name] = [np.array(hdf_file[channel_name]['filt_value'])]
    # saving popular channels for easy use
    ch101 = channels
        

# %% [markdown]
# #### Histograming
    channels['counts'], channels['edges'] = zip(*channels['peak_vals'].apply(np.histogram, args=(10_000,)))
    channels['midpoints'] =  [0.5 * (channel_edges[1:] + channel_edges[:-1]) for channel_edges in channels['edges']]

#%%
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


