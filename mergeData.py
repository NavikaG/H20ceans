import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Create dataframes from provided CSVs
temps = pd.read_csv("daily_temperature_means_PST.csv")
pops = pd.read_csv("seastarkat_count_totals_download.csv")

# Merge by row
merge = pd.merge(temps, pops, on=['marine_site_name', 'latitude', 'longitude', 'year', 'site_code', 'bioregion'], how='inner')

# Export new DF to CSV
merge.to_csv("merge_data.csv")
