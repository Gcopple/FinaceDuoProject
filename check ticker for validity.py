#test file for check_ticker_validity
import csv
import requests
import sys



def get_listing():
    parameters = {}
    parameters["function"] = "LISTING_STATUS"
    parameters['apikey'] = "RSDENX6YMEDJPVM6"
    response = open(requests.get("https://www.alphavantage.co/query", params = parameters))
    csv_response = csv.reader(response)
    print(csv_response)

#ticker = input("Please input desired ticker.")
"""
with open(get_listing(), newline = "") as csvfile:
    spawnreader = csv.reader(csvfile, delimiter = " ", quotechar = '|')
    for row in spamreader:
        print(', '.join(row))
"""
get_listing()
