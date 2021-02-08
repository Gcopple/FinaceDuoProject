import csv

#checks if the watchlist.csv file exists

#if it doesnt return an error message or create a csvfile


# reads the existing watchlist file
with open('Watchlist.csv', newline = '') as csvfile:
  spamreader = csv.reader(csvfile, delimiter = " ", quotechar = '|')
  for row in spamreader:
    print(', '.join(row))
