import csv
import requests
import sys
#checks if the watchlist.csv file exists
try:
    w = open("Watchlist.csv")
except IOError:
    #this sys exit is temporary
    sys.exit("That file does not exist")

def check_ticker_validity(requested_ticker):
    list = open('Stocklist.csv')
    list_csv = csv.reader(list)
    tickervalidity = False
    for row in list_csv:
        if requested_ticker in row:
            tickervalidity = True
    if tickervalidity == True:
        print("That ticker is valid and will be added")
    else:
        print("debug: The ticker is nonexistent")

Input_test = input("What ticker do you want to add?")
print("Is this the ticker that you want to add? ",Input_test)
check_ticker_validity(Input_test)
#if it doesnt return an error message or create a csvfile

#checks the watchlist for the Ticker
def check_watchlist_for():
    pass


#adds the ticker to watchlist.csv
def append_ticker_to_csv():
    pass

# reads the existing watchlist file
"""
with open('Watchlist.csv', newline = '') as csvfile:
  spamreader = csv.reader(csvfile, delimiter = " ", quotechar = '|')
  for row in spamreader:
    print(', '.join(row))
"""
