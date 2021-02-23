import csv
import requests
import sys
#checks if the watchlist.csv file exists
try:
    w = open("Watchlist.txt")
except IOError:
    #this sys exit is temporary
    w = open("Watchlist.txt", 'x')

#checks the ticker for realness
def check_ticker_validity(requested_ticker):
    list = open('Stocklist.csv')
    list_csv = csv.reader(list)
    tickervalidity = False
    for row in list_csv:
        if requested_ticker in row:
            tickervalidity = True
    if tickervalidity == True:
        print("That ticker is valid and will be added")
        return True
    else:
        print("debug: The ticker is nonexistent")
        return False

#checks the watchlist for the ticker
#could possibly make a list instead of csv
def check_watchlist_for(requested_ticker):
    w_list = w.read()
    watchlist_check = False
    if requested_ticker in w_list:
        watchlist_check = True
    if watchlist_check == True:
        print( requested_ticker, " is on the watchlist")
        return True
    else:
        print( requested_ticker, " is not on the watchlist")
        return False



Input_test = input("What ticker do you want to add?")
print("Is this the ticker that you want to add? ",Input_test)
if check_ticker_validity(Input_test) == True:
    if check_watchlist_for(Input_test) == False:
        append_ticker_to_list(Input_test)
#if it doesnt return an error message or create a csvfile




#adds the ticker to watchlist.csv
def append_ticker_to_list(ticker):
    pass

# reads the existing watchlist file
"""
with open('Watchlist.csv', newline = '') as csvfile:
  spamreader = csv.reader(csvfile, delimiter = " ", quotechar = '|')
  for row in spamreader:
    print(', '.join(row))
"""
