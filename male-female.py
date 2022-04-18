#Graph distribution of male and female

import pandas as pd
import matplotlib.pyplot as plt

# Import CSV data files as Pandas Dataframe
ms_global = pd.read_csv("MS_GLOBAL_STATS.csv")

# Print Head
print(ms_global.head(89))

# Print DataFrame Summary
print(ms_global.info())

# Removing Missing Values of MS_GLOBAL
missing_values_count = ms_global.isnull().sum()
droprows = ms_global.dropna(how='all')
dropcolumns = droprows.dropna(axis=1, how='all')
cleaned_data = dropcolumns.fillna(0)
df = cleaned_data.drop_duplicates()

#Set unique Index as Country Column
df.set_index("Country", inplace=True)

#Sort by Country
df.sort_values(by ='Country', axis=0, ascending=True, inplace=False, kind='quicksort', na_position='last', ignore_index=False, key=None)

#Remove unnecissary columns
df = df[["Female", "Male"]]

#Slice to only include relevant Countries
df = df.loc[['Ireland', 'United Kingdom', 'United States of America', 'Spain', 'France', 'China', 'Global', 'European'], :]

#Lambda Function will convert numbers to percentages
stacked_data = df.apply(lambda x: x*100/sum(x), axis=1)
print(stacked_data)

#Create Visualization
stacked_data.plot(kind="bar", stacked=True, color=["deeppink", "royalblue"])
plt.title("Male / Female Proportion of People with MS")
plt.xlabel("Place")
plt.ylabel("Percentage of People with MS (%)")
plt.tight_layout()

plt.show()
