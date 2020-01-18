import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

df = pd.read_csv("daily_temperature_means_PST.csv")
temp = df[df['marine_site_name'] == "Sage Rock"]
temp.plot(x = 'date', y = 'mean')
plt.show()
print(temp)