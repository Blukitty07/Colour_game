import csv
import random

# Retrieve colours for csv file and put them in a list
file = open("00_colour_list_hex_v3.csv", "r")
all_colours = list(csv.reader(file, delimiter=","))
file.close()

# remove first row
all_colours.pop(0)

print(all_colours)
