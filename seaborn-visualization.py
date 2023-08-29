# python script that shows the spatial distribution of trees concerninf mountains Paiko and Voras , using the Seaborn library in order to visualize the data
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("data_fagus almopia.csv")

population_column = "Population"
individual_column = "Tree"
latitude_column = "lat"
longtidute_column = "long"
voras_df = df[df[population_column] =="Voras" ]
paiko_df = df[df[population_column] =="Paiko" ]

plt.figure(figsize=(10, 8))
sns.scatterplot(x=longtidute_column, y=latitude_column, data=voras_df, label ="Voras")
plt.title("Spatial Distribution of Tree Individuals -Voras Population")
plt.xlabel("longitude")
plt.ylabel("latitude")

sns.scatterplot(x=longtidute_column, y=latitude_column, data=paiko_df, label="Paiko")
plt.title("Spatial Distribution of Tree Individuals -Paiko Population")
plt.xlabel("longitude")
plt.ylabel("latitude")

plt.legend()
plt.show()
