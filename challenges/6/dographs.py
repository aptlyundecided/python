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

# Get the first 20
TOP_TWENTY = FILTERED_CARS.head(20)

#
sns.set(style='ticks')

# Create the line graph / pointplot.
CP = sns.barplot(x='Car', y='MPG', data=TOP_TWENTY, palette="muted")

# Rotate the labels so they fit
CP.set_xticklabels(TOP_TWENTY['Car'], rotation=90)

# Graph ADMIN STUFF
CP.set_xlabel('Car Types')
CP.set_ylabel('MPG per Car')
CP.set_title('MPG of cars from the late 70\'s and early 80\'s')
#
sns.plt.tight_layout()

# Show the graph
sns.plt.show()

# END
