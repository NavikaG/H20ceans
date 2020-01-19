import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt
import matplotlib 

df = pd.read_csv('seastarkat_count_totals_download.csv')

df = df[df['site_code'] == "ALEG"]

animals = df['species_code'].unique()
N=len(animals)

# print (N)


# dfAlg=iloc['ALEG']

year = df[df.columns[8]]
#year = df['year'].unique()

total = df[df.columns[14]]


label = animals
colors = ['red','green','blue']

for x in animals:
    y=np.random.rand(3,)
    newdf = df[df['species_code'] == x]

    #print(newdf[newdf.columns[13]])
    tempTotal = newdf[newdf.columns[14]]
    tempYear = newdf[newdf.columns[8]]
    
    plt.scatter(tempYear, tempTotal, marker = "o", label=x, color = y)
    plt.legend((animals), loc='upper right')

#plt.scatter(year, total, c = label]

#plt.scatter(year, total, color=N)

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