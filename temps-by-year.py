#presents graph based on median year values to show trends
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

#reads in temp file
df = pd.read_csv("daily_temperature_means_PST.csv")


#new df for one location
#Need to change this so it works for inputted locations
temp = df[df['marine_site_name'] == "Ecola"]


#list of unique years
yearList = temp['year'].unique()
#print(yearList)
#for loop to calculate mean for every year in 'years' list
for x in yearList:
    newdf = temp[temp['year'] == x]
    tempMean = newdf['mean'].mean()
    plt.plot(x, tempMean, marker = "o", color = "m")
plt.show()