#Graph distribution of male and female
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches

# Import CSV data files as Pandas Dataframe

ms_global = pd.read_csv("MS_GLOBAL_STATS.csv")
ms_2008 = pd.read_csv("MS_ATLAS_2008.csv")
ms_2013 = pd.read_csv("MS_ATLAS_2013.csv")

#merge 2008 and 2013 datasets
atlas_merge = pd.merge(ms_2008, ms_2013, on="Country", how='left', indicator=True)
print(atlas_merge)

# Print Headers
print(atlas_merge.head())

# Print DataFrame Summary
print(atlas_merge.info())

#Create new column which calulates increase of cases between 2008 and 2013
atlas_merge['Increase'] = atlas_merge['Prevalence of MS'] - atlas_merge['Prevalence of MS, 2008']

arr = []
#Iterate rows of Dataframe and add all with increases to array
for index, row in atlas_merge.iterrows():
    if row['Increase'] > 0:
        arr.append([row['Country'], row['Increase']])

# Represent conversion of array to dataframe
df = pd.DataFrame(data=arr, columns=['Country', 'Increase'])

#Set index to Country
df.set_index('Country', drop=True, append=False, inplace=False, verify_integrity=False)

#Groupby country to combine any possibility of duplicates
df = df.groupby(['Country']).mean()

#Sort by Increase decending
df = df.sort_values(by='Increase', ascending=False)

#Roughly half the DF
df = df.iloc[:-25]
print(df)

#visualization
sns.set_theme(style="whitegrid")
ax = sns.barplot(x="Increase", y=df.index, data=df)
plt.xlabel('% Increase of Prevelance of MS between 2008 and 2013')
plt.title("Countries with most recorded increases between 2008 and 2013")
plt.tight_layout()
plt.show()

