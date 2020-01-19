#presents graph based on median year values to show trends
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

#reads in temp file
df = pd.read_csv("daily_temperature_means_PST.csv")
temp = df[df['marine_site_name'] == "Ecola"]
yearList = temp['year'].unique()
for x in yearList:
    newdf = temp[temp['year'] == x]
    tempMean = newdf['mean'].mean()
    plt.plot(x, tempMean, marker = "o", color = "m")
plt.show()