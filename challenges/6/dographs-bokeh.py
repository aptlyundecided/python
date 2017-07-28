"""
Let's visualize some data using seaborn.
"""
import pandas as pd
from bokeh.plotting import figure, output_file, show

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

yax = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]

# Create a static output file.
output_file('bokeh00.html')

# create a new plot
P = figure(title="Top 20 MPG from 78-82", x_axis_label='Car Types', y_axis_label='MPG per Car')

# add a line renderer with legend and line thickness
P.line(yax, TOP_TWENTY['MPG'], legend="Temp.", line_width=2)


show(P)
# print(TOP_TWENTY)
# END
