# 2023 Winter Temperature Anomaly of Europe

This code is designed to analyze and visualize the temperature anomaly during the winter of 2023 relative to the long-term average winter temperatures from 1993 to 2022. 
## Table of Contents
- [About the Dataset](#about-the-dataset)
- [Purpose of the Project](#purpose-of-the-project)
- [Results](#results)
- [License](#license)

## About the Dataset

The datasets contain temperature data over specific periods, formatted as NetCDF files.

***1993-2022 Dataset (1993_2022.nc)***:

**Dimensions**:

 - **Time**: 90 points, representing monthly data from January 1993 to December 2022.
 - **Latitude**: 201 points, covering latitudes from 30°N to 80°N.
 - **Longitude**: 521 points, covering longitudes from -50°W to 80°E.

**Data Variables**:

- **t2m**: This variable represents 2-meter air temperature (in degrees Celsius)

**Content**:
The dataset contains monthly mean 2-meter air temperature data over a 30-year period (1993-2022). This is typically used to analyze long-term temperature trends and calculate climatological averages.

***2023 Winter Dataset (2023_winter.nc)***:

**Dimensions**:

- **Time**: 3 points, representing data for January, February, and December of 2023.
 **Latitude**: 201 points, covering the same latitudes as the long-term dataset (30°N to 80°N).
- **Longitude**: 521 points, covering the same longitudes as the long-term dataset (-50°W to 80°E).

**Data Variables**:
- **t2m**: Similar to the long-term dataset, this variable also represents 2-meter air temperature.

**Content**:
The dataset contains 2-meter air temperature data specifically for the winter months of 2023. This is used to compare the 2023 winter temperatures with the long-term average calculated from the 1993-2022 dataset.

## Purpose of the Project
This project focuses on identifying and visualizing how winter temperatures in 2023 differed from the historical average, which can provide insights into trends related to climate variability or change.

- Data loading
- Calculating Mean Temperatures
- Temperature Anomaly Calculation
- Visualization

## Results
 
The resulting contour map visually represents the spatial distribution of temperature anomalies, highlighting regions that experienced significant deviations from the long-term winter average. This can provide insights into unusual weather patterns, possibly linked to broader climate trends or specific meteorological events during that winter.


### License

This project is licensed under the MIT License - see the LICENSE file for details.
