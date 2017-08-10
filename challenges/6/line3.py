"""
Let's visualize some data using seaborn.
"""
import pandas as pd
import seaborn as sns

# Read in the cars csv
CARS = pd.read_csv('assets/cars.csv', sep=';')

# Drop the first row of the dataframe (it just describes the data type.)
CARS = CARS.drop(CARS.index[[0]])

# Change MPG from string into float
CARS['MPG'] = CARS['MPG'].astype(float)

# Create Zero filter
ZERO_MPG_FILTER = CARS['MPG'] != 0

# Filter Cars
FILTERED_CARS = CARS[ZERO_MPG_FILTER]

# Arrange by descending so the highest are at the top
FILTERED_CARS.sort_values(by=('MPG'), inplace=True, ascending=False)

#
sns.set(style='ticks')

# Create integer version of MPG
FILTERED_CARS['mpg_int'] = FILTERED_CARS['MPG'].astype(int)
FILTERED_CARS['cylinders_int'] = FILTERED_CARS['Cylinders'].astype(int)
FC = FILTERED_CARS['Horsepower'].astype(float)
FX = FC.astype(int)
# [!]
# Not fully function code below here :-(
# [!]
FX.sort_values(axis=0, inplace=True)

print(FX)

FILTERED_CARS['horsepower_int'] = FX

FILTERED_CARS = FILTERED_CARS.drop_duplicates('Car')

AX = sns.pointplot(y='mpg_int', x='horsepower_int', data=FILTERED_CARS, palette='muted')

AX.set_xlabel('Horsepower')
AX.set_ylabel('MPG')
AX.set_title('MPG vs. Horsepower')

# print(FILTERED_CARS['horsepower_int'])

# Rotate the labels so they fit
AX.set_xticklabels(FILTERED_CARS['horsepower_int'], rotation=90)

#
sns.plt.tight_layout()

# Show the graph
sns.plt.show()
