import tkinter as Tk
from tkinter import ttk


root = Tk.Tk()
root.title('Currency Converter')
root.geometry("520x900")

listbox = Tk.Listbox(root)
listbox.pack(fill=Tk.BOTH, expand=True)

currencies = ["Dollar", "TL", "SEK", "Yen","Euro"]

currency_listbox = Tk.Listbox(root)
currency_listbox.pack()

for currency in currencies:
    currency_listbox.insert(Tk.END, currency)

currencies_2 = ["Dollar", "TL", "SEK", "Yen","Euro"]

currency2_listbox = Tk.Listbox(root)
currency2_listbox.pack()

for currency2 in currencies:
    currency2_listbox.insert(Tk.END, currency2)


style = ttk.Style()
style.configure('Pink.TButton', background='#ff007f',foreground='white',font=('Arial Bold',16))


def calculate_currency_value(): 
    global TL_Var
    TL= float(TL_var.get())
    exchange_rate= 0.051
    Dollar = TL * exchange_rate
    return (Dollar,TL)
    
def calculate_SEK():  
     global TL_var
     TL = float(TL_var.get())
     exchange_rate= 0.53
     SEK = TL * exchange_rate
     return (SEK,TL)

def calculate_Yen():
    global TL_var
    TL = float(TL_var.get())
    exchange_rate= 0.14
    Yen = TL * exchange_rate
    return (Yen,TL)

def calculate_Euro():
    global TL_var
    TL = float(TL_var.get())
    exchange_rate= 0.047
    Euro = TL * exchange_rate
    return (Euro,TL)

def calculate_SEK():
    global Dollar_var
    Dollar = float(Dollar_var.get())
    exchange_rate= 10.25
    SEK = Dollar * exchange_rate
    return (SEK, Dollar)

def calculate_Yen():
    global Dollar_Var
    Dollar = float(Dollar_var.get())
    exchange_rate= 134.71
    Yen = Dollar * exchange_rate
    return (Yen,Dollar)

def calculate_Euro():
    global Dollar_var
    Dollar = float(Dollar_var.get())
    exchange_rate= 0.91
    Euro = Dollar * exchange_rate
    return (Euro, Dollar)

def calculate_Yen():
    global SEK_var
    SEK = float(SEK_var.get())
    exchange_rate= 13.15
    Yen = SEK * exchange_rate
    return (Yen, SEK)

def calculate_Euro():
    global SEK_var
    SEK = float(SEK_var.get())
    exchange_rate= 0.088
    Euro = SEK * exchange_rate
    return (Euro, SEK)

def calculate_Yen():
    global Yen_var
    Yen = float(Yen_var.get())
    exchange_rate= 0.0067
    Euro = Yen * exchange_rate
    return (Euro, Yen)

    
    
    
    
    
    


Dollar = Tk.StringVar() 
TL = Tk.StringVar()
SEK = Tk.StringVar()
Yen = Tk.StringVar()
Euro = Tk.StringVar()

def get_Dollar():
    Dollar_index = currency_listbox.curselection()
    if Dollar_index:
        Dollar.set(currencies[Dollar_index[0]])

def get_TL():
    TL_index = currency_listbox.curselection()
    if TL_index:
        TL.set(currencies[TL_index[0]])

def get_SEK():
    SEK_index = currency_listbox.curselection()
    if SEK_index:
        SEK.set(currencies[SEK_index[0]])

def get_Yen():
    Yen_index = currency_listbox.curselection()
    if Yen_index:
        Yen.set(currencies[Yen_index[0]])

def get_Euro():
    Euro_index = currency_listbox.curselection()
    if Euro_index:
        Euro.set(currencies[Euro_index[0]])












calculate_currency = ttk.Frame(root)
calculate_currency.pack(padx=10, pady=10, fill='x', expand=True)



convert_button = ttk.Button(calculate_currency,text="Convert",style='Pink.TButton',command=calculate_currency_value)
convert_button.pack(fill='y', expand=False, pady=6)






style = ttk.Style()
style.configure('TLabel', background='#ffb6c1')


root.configure(bg='#ff69b4')


root.mainloop()
