"""
A mess around with dataframe.to_html()
"""

# Import tools
import pandas

# Create a dataframe (I'm using the cars data from last time.)
CARS = pandas.read_csv('assets/cars.csv', sep=";")

# Get rid of first row [ I still am not sure about what this row is ]
CARS = CARS.loc[1:]

# Give index a name
CARS.index.name = 'CSV Row Number'

# Change MPG from string into float
CARS['MPG'] = CARS['MPG'].astype(float)

# Create Zero filter
ZERO_MPG_FILTER = CARS['MPG'] != 0

# Filter Cars
FILTERED_CARS = CARS[ZERO_MPG_FILTER]

# Arrange by descending so the highest are at the top
FILTERED_CARS.sort_values(by=('MPG'), inplace=True, ascending=False)

# Get the first 10
TOP_TEN = FILTERED_CARS.head(10)

#
# [!] Here comes the Pickle stuff!
#

# Compress Top Ten into a file, for persistence.
TOP_TEN.to_pickle('top_ten_pickle')

# Read that pickle
PICKLED_TOP_TEN = pandas.read_pickle('top_ten_pickle')

# Display data frame built from pickle.
print(PICKLED_TOP_TEN)

# END
