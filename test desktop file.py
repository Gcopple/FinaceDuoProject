
import requests
import json
#from PIL import ImakeTk
from tkinter import *
from tkinter import messagebox
import textwrap
#import matplotlib
root = Tk()
root.title("Finance Money Maker")
#root.iconbitmap()

func_label = Label(root, text = "Function:")
func_label.grid(row= 0 , column = 0)
f = Entry(root)
f.grid(row= 0, column = 1)
f.insert(0,"OVERVIEW")
tick_label = Label(root, text = "Ticker:")
tick_label.grid(row= 1 , column = 0)
ticker = Entry(root)
ticker.grid(row= 1, column = 1)
ticker.insert(0,"MMM")

textwidth = 70

def popup():
    data = messagebox.showinfo("function","10k")


def get_data():
    f.get()
    ticker.get()
    parameters = {}
    parameters["function"] = str(f.get())
    parameters["symbol"] = str(ticker.get())
    parameters["apikey"] = "RSDENX6YMEDJPVM6"
    formating = []
    formatted = []
    response = requests.get("https://www.alphavantage.co/query",params = parameters)
    for key,value in response.json().items():
        formating.append(key + ": " + value)
    for strings in formating:
        if len(strings)> textwidth:
            placeholder = textwrap.wrap(strings, width = textwidth)
            formatted.append("\n".join(placeholder))
        else:
            formatted.append(strings)



    printout = "\n".join(formatted)

    #print(response.text)
    #print(response.text)
    #print(response.url)
    Label(root,text = printout,justify = "left").grid(row = 4)
get_data_button =Button(root,text= "Get me the Money!", command = get_data)
get_data_button.grid(row = 3, column = 1)
test_button = Button(root,text = "Test Function button", command = popup)
test_button.grid(row=5, column = 0)
root.mainloop()
