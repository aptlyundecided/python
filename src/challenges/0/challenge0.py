"""Challenge Zero: Environmental Studies"""
import csv

def highest_temp(filename):
    """Get the highest temp, and the date and time they occured on."""
    date = ''
    time = ''
    temp = 0
    with open(filename, newline='') as this_csvfile:
        reader = csv.DictReader(this_csvfile)

        for row in reader:
            temp_int = int(row['temperature'])
            if temp_int > temp:
                temp = temp_int
                date = row['date']
                time = row['time']
    return [temp, date, time]



TEMP_DATA = highest_temp('../assets/Test_Data.csv')
print(TEMP_DATA)
