#test file for check_ticker_validity
import csv
import requests
import sys

list = open('Stocklist.csv')
list_csv = csv.reader(list)


requested_ticker = input('Please enter the ticker.')

tickervalidity = False
for row in list_csv:
    if requested_ticker in row:
        tickervalidity = True

if tickervalidity == True:
    print("That ticker is valid")
else:
    print(requested_ticker, ' is not valid.')



#    print("123")
#print("456")


"""
def get_listing():
    parameters = {}
    parameters["function"] = "LISTING_STATUS"
    parameters['apikey'] = "RSDENX6YMEDJPVM6"
    response = open(requests.get("https://www.alphavantage.co/query", params = parameters))
    csv_response = csv.reader(response)
    print(csv_response)
"""
#ticker = input("Please input desired ticker.")
"""
with open(get_listing(), newline = "") as csvfile:
    spawnreader = csv.reader(csvfile, delimiter = " ", quotechar = '|')
    for row in spamreader:
        print(', '.join(row))
"""
