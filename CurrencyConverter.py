#importing liberaries
from forex_python.converter import CurrencyRates
import tkinter as tk
from tkinter import *
import tkinter.messagebox

window = Tk()# creating empty window

window.title("ProjectGurukul Currency Conversion")# adding title to the window
window.geometry("700x400")

head = tk.Label( font=('Helvetica', 19, 'bold'), text='Currency Converter',
                     bg='grey', fg='black')
head.grid(row=1, column=0, sticky=W)
#declaring variables
from_var = tk.StringVar(window)
to_var = tk.StringVar(window)
#initializing variables
from_var.set("currency")
to_var.set("currency")

#function for realtime conversion
def RealTimeCurrencyConversion():
    from forex_python.converter import CurrencyRates
    c = CurrencyRates()

    from_currency = "currency"
    to_currency = "currency"

    if (Amount1.get() == ""):
        tkinter.messagebox.showinfo("Error !!")

    elif (from_currency == "currency" or to_currency == "currency"):
        tkinter.messagebox.showinfo("Error !!")

    else:
        new_amt = c.convert(from_currency, to_currency, float(Amount1.get()))
        new_amount = float("{:.4f}".format(new_amt))
        Amount2.insert(0, str(new_amount))

#list of currency
CurrenyCode_list = ["INR", "USD", "CAD", "CNY", "DKK", "EUR"]

#creating labels
Label_1 = Label(window, font='Helvetica', text="", padx=2, pady=2, bg="grey", fg="black")
Label_1.grid(row=1, column=0, sticky=W)

amount = tk.Label(window, font='Helvetica', text="   Amount  :  ", bg="grey", fg="black")
amount.grid(row=2, column=0, sticky=W)

from_curr = tk.Label(window, font='Helvetica', text="   From Currency  :  ", bg="grey", fg="black")
from_curr.grid(row=3, column=0, sticky=W)

to_cur = tk.Label(window, font='Helvetica', text="    To Currency  :  ", bg="grey", fg="black")
to_cur.grid(row=4, column=0, sticky=W)

convert_amt = tk.Label(window, font='Helvetica', text="  Converted Amount  :  ", bg="grey", fg="black")
convert_amt.grid(row=8, column=0, sticky=W)

Label_1 = Label(window, font='Helvetica', text="", padx=2, pady=2, bg="grey", fg="black")
Label_1.grid(row=5, column=0, sticky=W)

Label_2 = Label(window, font='Helvetica', text="", padx=2, pady=2, bg="grey", fg="black")
Label_2.grid(row=7, column=0, sticky=W)

FromCurrency = tk.OptionMenu(window, from_var, *CurrenyCode_list)
ToCurrency = tk.OptionMenu(window, to_var, *CurrenyCode_list)

FromCurrency.grid(row=3, column=1, ipadx=45, sticky=E)
ToCurrency.grid(row=4, column=1, ipadx=45, sticky=E)

Amount1 = tk.Entry(window)
Amount1.grid(row=2, column=1, ipadx=28, sticky=E)

Amount2 = tk.Entry(window)
Amount2.grid(row=8, column=1, ipadx=31, sticky=E)

button= Button(window, font='arial', text="   Convert  ", padx=2, pady=2, bg="blue", fg="white",
                 command=RealTimeCurrencyConversion)
button.grid(row=6, column=0)

Label_1 = Label(window, font='Helvetica', text="", padx=2, pady=2, bg="grey", fg="black")
Label_1.grid(row=9, column=0, sticky=W)

window.configure(background='grey')
window.mainloop()