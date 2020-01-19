import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Create dataframe from provided CSV for temperature data
temps = pd.read_csv("daily_temperature_means_PST.csv")
# Delete unused columns
temps.drop(['processing_group', 'month', 'day', 'date', 'day_of_year' , 'time_format'], axis=1)

# Create Lists for Unique Years and Sites for Sorting Purposes
yearList = temps.year.unique()
locList = temps.site_code.unique()

# New Empty Dataframe to be Filled with Averages for Each Site by Year
new_temps = pd.DataFrame(columns=['site_code', 'marine_site_name', 'latitude', 'longitude', 'bioregion', 'island', 'detide_method', 'year', 'n', 'mean', 'stderr'])

# Traverse Through List of Sites to Pull Rows from Main DF
for l in locList:
    # New DF for Specific Sites
    locdf = temps[temps["site_code"]==l]
    # Constant Column Values for Sites
    msite = locdf.iloc[0]['marine_site_name']
    lat = locdf.iloc[0]['latitude']
    longi = locdf.iloc[0]['longitude']
    breg = locdf.iloc[0]['bioregion']
    isl = locdf.iloc[0]['island']
    dmeth = locdf.iloc[0]['detide_method']
    # Traverse Through List of Years to Pull Rows from Site DF
    for y in yearList:
        # New DF for Specific Years
        yeardf = temps[temps["year"]==y]
        # Mean Values for Data by Year
        n_mean = yeardf["n"].mean()
        mean_mean = yeardf["mean"].mean()
        stderr_mean = yeardf["stderr"].mean()
        # Fills Target DF with New Average Data by Year
        new_temps.loc[len(new_temps)] = [l, msite, lat, longi, breg, isl, dmeth, y, n_mean, mean_mean, stderr_mean]

# Create dataframe from provided CSV for population data
pops = pd.read_csv("seastarkat_count_totals_download.csv")
# Delete unused columns
pops.drop(['group_code', 'season_name'], axis=1)

# Merge by row
merge = pd.merge(new_temps, pops, on=['marine_site_name', 'year', 'site_code'])

# Export new DF to CSV
merge.to_csv("merge_data.csv")
