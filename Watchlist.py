import csv
import sys
#checks if the watchlist.csv file exists
try:
    w = open("Watchslist.csv")
except IOError:
    sys.exit("That file does not exist")



#if it doesnt return an error message or create a csvfile


# reads the existing watchlist file
with open('Watchlist.csv', newline = '') as csvfile:
  spamreader = csv.reader(csvfile, delimiter = " ", quotechar = '|')
  for row in spamreader:
    print(', '.join(row))
