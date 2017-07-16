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

# MAKE AN HTML TABLE
TOP_TEN_TABLE = TOP_TEN.to_html()

#
# [!] Here comes HTML stuff NOT HANDLED IN PANDAS [!]
#
# P.S. FORGIVE THE UGLINESS!
#

HTMLFILE = open('top_ten_mpg.html', 'w')

# Create opening portion of HTML
HTML_1 = """
<html>
<head>
<title> TOP TEN MPG </title>
</head>
<body>
<h1> Top Ten MPG Table </h1>
"""

# Create closing half of HTML
HTML_2 = """
</body>
</html>
"""

# Create the concatenated HTML and HTML TABLE
ALL_HTML = HTML_1 + TOP_TEN_TABLE + HTML_2

# Write to file.
HTMLFILE.write(ALL_HTML)

# END
