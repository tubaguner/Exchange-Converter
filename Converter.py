import tkinter as Tk
from tkinter import ttk


root = Tk.Tk()
root.title('Currency Converter')
root.geometry("420x700")

listbox = Tk.Listbox(root)
listbox.pack(fill=Tk.BOTH, expand=True)

label_from = Tk.Label(root, text='From:')
label_from.pack()

listbox_from = Tk.Listbox(root)
listbox_from.pack(fill='both', expand=True)

items = {
    'USD': {'TRY': [0.51, 0.52], 'SEK': [10.25], 'JPY': [134.71], 'EUR': [0.91, 0.92]},
    'TRY': {'USD': [1.96], 'SEK': [0.53], 'JPY': [7.14], 'EUR': [0.047]},
    'SEK': {'USD': [0.097], 'TRY': [1.88], 'JPY': [13.15], 'EUR': [0.088]},
    'JPY': {'USD': [0.0074], 'TRY': [0.14], 'SEK': [0.076], 'EUR': [0.0067]},
    'EUR': {'USD': [1.10], 'TRY': [21.32], 'SEK': [11.37], 'JPY': [149.42]}
}

for item in items: 
    listbox_from.insert('end',item)

label_to = Tk.Label(root,text='To:')
label_to.pack()

listbox_to = Tk.Listbox(root)
listbox_to.pack(fill='both', expand=True)


for item in items:
    listbox_to.insert('end', item)



style = ttk.Style()
style.configure('Pink.TButton', background='#ff007f',foreground='white',font=('Arial Bold',16))


def calculate_1(): 
    global TRY_var
    TRY= float(TRY_var.get())
    exchange_rate= 0.051
    USD = TRY * exchange_rate
    return (USD,TRY)
    
def calculate_2():  
     global TRY_var
     TRY = float(TRY_var.get())
     exchange_rate= 0.53
     SEK = TRY * exchange_rate
     return (SEK,TRY)

def calculate_3():
    global JPY_var
    TRY = float(TRY_var.get())
    exchange_rate= 0.14
    JPY = JPY * exchange_rate
    return (JPY,TRY)

def calculate_4():
    global TRY_var
    TRY = float(TRY_var.get())
    exchange_rate= 0.047
    EUR = TRY * exchange_rate
    return (EUR,TRY)

def calculate_5():
    global USD_var
    USD = float(USD_var.get())
    exchange_rate= 10.25
    SEK = USD * exchange_rate
    return (SEK, USD)

def calculate_6():
    global USD_Var
    USD = float(USD_var.get())
    exchange_rate= 134.71
    JPY = USD * exchange_rate
    return (JPY,USD)

def calculate_7():
    global USD_var
    USD = float(USD_var.get())
    exchange_rate= 0.91
    EUR = USD * exchange_rate
    return (EUR, USD)

def calculate_8():
    global SEK_var
    SEK = float(SEK_var.get())
    exchange_rate= 13.15
    JPY = SEK * exchange_rate
    return (JPY, SEK)

def calculate_9():
    global SEK_var
    SEK = float(SEK_var.get())
    exchange_rate= 0.088
    EUR = SEK * exchange_rate
    return (EUR, SEK)

def calculate_10():
    global JPY_var
    JPY = float(JPY_var.get())
    exchange_rate= 0.0067
    EUR = JPY * exchange_rate
    return (EUR, JPY)

    
    
USD = Tk.StringVar() 
TRY = Tk.StringVar()
SEK = Tk.StringVar()
JPY = Tk.StringVar()
EUR = Tk.StringVar()

def get_USD():
    USD_index = items.curselection()
    if USD_index:
        USD.set(listbox_to[USD_index[0]])

def get_TRY():
    TRY_index = items.curselection()
    if TRY_index:
        TRY.set(listbox_to[TRY_index[0]])

def get_SEK():
    SEK_index = items.curselection()
    if SEK_index:
        SEK.set(listbox_to[SEK_index[0]])

def get_JPY():
    JPY_index = items.curselection()
    if JPY_index:
        JPY.set(listbox_to[JPY_index[0]])

def get_EUR():
    EUR_index = items.curselection()
    if EUR_index:
        EUR.set(listbox_to[EUR_index[0]])

Output = Tk.StringVar()
output_entry = ttk.Entry(root, textvariable=Output)
output_entry.pack(fill='x',expand=True)
Output.get()
output_entry.focus()





Result = Tk.StringVar()
result_entry = ttk.Entry(root,textvariable=Result)
result_entry.pack(fill='x', expand=True)
Result.get()
result_entry.focus()





convert_button = ttk.Button(root,text="Convert",style='Pink.TButton',command=calculate_1)
convert_button.pack(fill='y', expand=False, pady=6)






style = ttk.Style()
style.configure('TLabel', background='#ffb6c1')


root.configure(bg='#ff69b4')


root.mainloop()
