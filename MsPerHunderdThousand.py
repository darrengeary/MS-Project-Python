#Graph MS per 100,000 for relevant countries and regions

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Import CSV data files as Pandas Dataframe
ms_global = pd.read_csv("MS_GLOBAL_STATS.csv")

# Print Headers
print(ms_global.head(89))

# Print DataFrame Summary
print(ms_global.info())

# Removing Missing Values of MS_GLOBAL
missing_values_count = ms_global.isnull().sum()
droprows = ms_global.dropna(how='all')
dropcolumns = droprows.dropna(axis=1, how='all')
cleaned_data = dropcolumns.fillna(0)
df = cleaned_data.drop_duplicates()

#Set Index to country and sort by Country alpahbetically
df.set_index("Country", inplace=True)

#Trim to necissary columns and rows
df = df[["Prevalence of MS per 100,000"]]
df = df.loc[['Ireland', 'United Kingdom', 'United States of America', 'Spain', 'France', 'China', 'Global', 'European'], :]

#Sort for decending
df = df.sort_values(by='Prevalence of MS per 100,000', ascending=False)

#Create Visualization
sns.set_theme(style="whitegrid")
ax = sns.barplot(x="Prevalence of MS per 100,000", y=df.index, data=df)
plt.tight_layout()
plt.show()




