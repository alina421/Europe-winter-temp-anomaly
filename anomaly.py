
"""
Winter Temperatures Anomaly of 2023 relative to 1993-2022 years
"""

import xarray as xr
import matplotlib.pyplot as plt
import cartopy.crs as ccrs
import cartopy.feature as cfeature
import numpy as np 

# datasets
long_term = xr.open_dataset("C:/anomaly/1993_2022.nc")
recent_data = xr.open_dataset("C:/anomaly/2023_winter.nc")

# Compute mean temperature for both periods
long_term_mean = long_term['t2m'].mean(dim='time')
recent_mean = recent_data['t2m'].mean(dim='time')

# Calculate the anomaly
anomaly = recent_mean - long_term_mean

# Define the figure and axis with Cartopy projection
fig, ax = plt.subplots(figsize=(10, 12), subplot_kw={'projection': ccrs.PlateCarree()})

# Set the geographical extent to include Europe and Turkey
ax.set_extent([-20, 45, 34, 75], crs=ccrs.PlateCarree())

# Add coastlines and borders for better visualization
ax.coastlines(resolution='50m', linewidths=0.5)
ax.add_feature(cfeature.BORDERS, linestyle=':', linewidths=0.4)

lev = np.linspace(-6, 6, 36) 
color_bar_ticks = np.arange(-6, 7, 2)

# Plot the contour map of temperature anomalies
contour_plot = ax.contourf(anomaly.longitude,anomaly.latitude, anomaly, transform=ccrs.PlateCarree(), cmap='RdBu_r',levels=lev)

# Add color bar
cbar = plt.colorbar(contour_plot, ax=ax, shrink=0.5, pad=0.04)
cbar.set_label('Temperature Anomaly (°C)')
cbar.set_ticks(color_bar_ticks)

# Display the plot with title
plt.title('Winter Temperature Anomaly (2023  vs. 1993-2022  Average)')
plt.show()

