w = open("Watchlist.txt")
w_list = []
w_list = w.readlines()

print(w_list)

status = True
while status == True:
    ticker = input("please enter the requested ticker, when done enter 'Done'")
    if ticker == 'Done':
        status = False
    w_list.append(ticker)

for ticker in w_list:
    w.write(ticker)
    w.write('\n')
print(w_list)
print("Done")
