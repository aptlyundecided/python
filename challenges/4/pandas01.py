"""
First mess around with pandas
"""


# Import tool(s)
import pandas

# Create a dataframe straight from a .csv file
CARS = pandas.read_csv('assets/cars.csv', sep=';')

# Get the names of each of the columns in the data frame
print(list(CARS))

# Create a list of the MPG's without the first column?  IS it because the
# the first column is the name of the column?
CARS['MPG'] = CARS['MPG'].iloc[1:].astype(float)

# Create a zero filter
NON_ZERO_FILTER = CARS['MPG'] != 0

# Filtered MPG
MPG = CARS[NON_ZERO_FILTER]

# Get all those data points
HIGHEST_MPG = MPG.max()
LOWEST_MPG = MPG.min()
AVG_MPG = MPG.mean()
COMMON_MPG = MPG.mode()

# Print the highest MPG
print('')
print(':::HIGHEST MPG:::')
print(HIGHEST_MPG)

#Print the lowest MPG
print('')
print(':::LOWEST MPG:::')
print(LOWEST_MPG)

# Print the AVG MPG
print('')
print(':::AVERAGE MPG:::')
print(AVG_MPG)

# Print the most common MPG
print('')
print(':::MOST COMMON MPG:::')
print(COMMON_MPG)


#END
