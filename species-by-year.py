import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt 

df = pd.read_csv('seastarkat_count_totals_download.csv')

df = df[df['site_code'] == "BML"]
# dfAlg=iloc['ALEG']

year = df[df.columns[8]]
#year = df['year'].unique()

total = df[df.columns[14]]

plt.scatter(year, total)

#print(total)

# df.plot()
plt.show()

# lat=df[df.columns[3]]
# lon=df[df.columns[4]]
# temp=df[df.columns[15]]

# N=228242
# print (temp)
# colors = temp
# area = temp

# plt.scatter(lat, lon, s=area, c=colors, alpha=0.5)
# plt.show()









# plt.scatter(lat,lon)
 
# plt.show()

# temp = df[f:50]
# print(temp)