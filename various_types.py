import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches

# Import CSV data files as Pandas Dataframe
ms_global = pd.read_csv("MS_ATLAS_2013.csv")

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

#Set Index to Country Column
df.set_index("Country", inplace=True)

#Sort Values by country alphabetically
df.sort_values(by ='Country', axis=0, ascending=True, inplace=False, kind='quicksort', na_position='last', ignore_index=False, key=None)
print(df)

#Create a reusable function for creating a bar chart
#Can pass a place paramter into function (Country / Region row from the Dataframe)
def msTypePieChart(place):
    #Slice to necissary Columns
    place = place[["% Relapsing Remitting MS", "% Primary Progressive MS", "% Progressive Relapsing MS"]]

    #add numbers for 3 types of MS to array
    array = place.values[0]

    #Create Pie Chart Visualizations
    mylabels = ["Relapsing Remitting MS", "Primary Progressive MS", "Progressive Relapsing MS"]
    myexplode = [0.2, 0, 0]
    plt.pie(array, labels=mylabels, explode=myexplode, shadow=True)
    plt.title(place.index[0])
    plt.tight_layout()
    plt.show()

    return None

#Use the function to create pie charts for 4 relevant countries
msTypePieChart(df.loc[['Ireland']])
msTypePieChart(df.loc[['United Kingdom']])
msTypePieChart(df.loc[['Spain']])
msTypePieChart(df.loc[['France']])


