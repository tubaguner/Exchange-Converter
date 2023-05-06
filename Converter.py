import tkinter as Tk
from tkinter import ttk


root = Tk.Tk()
root.title('Currency Converter')
root.geometry("420x700")

label_from = Tk.Label(root, text='From:')
label_from.pack()

listbox_from = Tk.Listbox(root, exportselection=0)
listbox_from.pack(fill='both', expand=True)

items = {
    'USD': {'TRY': [0.51], 'SEK': [10.25], 'JPY': [134.71], 'EUR': [0.91]},
    'TRY': {'USD': [1.96], 'SEK': [0.53], 'JPY': [7.14], 'EUR': [0.047]},
    'SEK': {'USD': [0.097], 'TRY': [1.88], 'JPY': [13.15], 'EUR': [0.088]},
    'JPY': {'USD': [0.0074], 'TRY': [0.14], 'SEK': [0.076], 'EUR': [0.0067]},
    'EUR': {'USD': [1.10], 'TRY': [21.32], 'SEK': [11.37], 'JPY': [149.42]}
}

for item in items: 
    listbox_from.insert('end',item)

label_to = Tk.Label(root,text='To:')
label_to.pack()

listbox_to = Tk.Listbox(root, exportselection=0)
listbox_to.pack(fill='both', expand=True)

for item in items:
    listbox_to.insert('end', item)



style = ttk.Style()
style.configure('Pink.TButton', background='#ff007f',foreground='white',font=('Arial Bold',16))

def calculate_currency(): 
    from_item =listbox_from.curselection()
    to_item = listbox_to.curselection()
    amount = float(Input.get())
    from_index = from_item [0]
    from_item = list(items) [from_index]
    to_index = to_item [0]
    to_item = list(items) [to_index]
    exchange_rate= items [from_item] [to_item] [0]
    currency = amount * exchange_rate
    Result.set(f"Result: {currency:.2f}")


    
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

Input = Tk.StringVar()
Input_entry = ttk.Entry(root, textvariable=Input)
Input_entry.pack(fill='x',expand=True)
Input.get()
Input_entry.focus()



Result = Tk.StringVar()
result_entry = ttk.Entry(root,textvariable=Result)
result_entry.pack(fill='x', expand=True)
Result.get()
result_entry.focus()



convert_button = ttk.Button(root,text="Convert",style='Pink.TButton',command=calculate_currency)
convert_button.pack(fill='y', expand=False, pady=6)



style = ttk.Style()
style.configure('TLabel', background='#ffb6c1')


root.configure(bg='#ff69b4')


root.mainloop()





        
