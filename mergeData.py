import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Create dataframes from provided CSVs
temps = pd.read_csv("daily_temperature_means_PST.csv")
temps.drop(['processing_group', 'month', 'day', 'date', 'day_of_year' , 'time_format'], axis=1)
yearList = temps.year.unique()
locList = temps.site_code.unique()
new_temps = pd.DataFrame(columns=['site_code', 'marine_site_name', 'latitude', 'longitude', 'bioregion', 'island', 'detide_method', 'year', 'n', 'mean', 'stderr'])
for l in locList:
    locdf = temps[temps["site_code"]==l]
    msite = locdf.iloc[0]['marine_site_name']
    lat = locdf.iloc[0]['latitude']
    longi = locdf.iloc[0]['longitude']
    breg = locdf.iloc[0]['bioregion']
    isl = locdf.iloc[0]['island']
    dmeth = locdf.iloc[0]['detide_method']
    for y in yearList:
        yeardf = temps[temps["year"]==y]
        n_mean = yeardf["n"].mean()
        mean_mean = yeardf["mean"].mean()
        stderr_mean = yeardf["stderr"].mean()
        new_temps.loc[len(new_temps)] = [l, msite, lat, longi, breg, isl, dmeth, y, n_mean, mean_mean, stderr_mean]

pops = pd.read_csv("seastarkat_count_totals_download.csv")
pops.drop(['group_code', 'season_name'], axis=1)
yearList = pops.year.unique()
locList = pops.site_code.unique()
new_pops = pd.DataFrame(columns=['site_code', 'marine_site_name', 'marine_sort_order', 'latitude', 'longitude', 'marine_common_season', 'marine_season_code', 'detide_method', 'year', 'n', 'mean', 'stderr'])
for l in locList:
    locdf = temps[temps["site_code"]==l]

# Merge by row
merge = pd.merge(new_temps, pops, on=['marine_site_name', 'year', 'site_code'])

# Export new DF to CSV
merge.to_csv("merge_data.csv")
