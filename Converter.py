import tkinter as Tk
from tkinter import ttk


root = Tk.Tk()
root.title('Currency Converter')
root.geometry("420x520")

label_from = Tk.Label(root, text='From:')
label_from.pack()

listbox_from = Tk.Listbox(root, exportselection=0)
listbox_from.pack(fill='both', expand=True)

items = {
    'USD': {'USD': [1],'TRY': [19.6], 'SEK': [10.25], 'JPY': [134.71], 'EUR': [0.91]},
    'TRY': {'TRY': [1],'USD': [0.051], 'SEK': [0.53], 'JPY': [7.14], 'EUR': [0.047]},
    'SEK': {'SEK': [1],'USD': [0.097], 'TRY': [1.88], 'JPY': [13.15], 'EUR': [0.088]},
    'JPY': {'JPY': [1],'USD': [0.0074], 'TRY': [0.14], 'SEK': [0.076], 'EUR': [0.0067]},
    'EUR': {'EUR': [1],'USD': [1.10], 'TRY': [21.32], 'SEK': [11.37], 'JPY': [149.42]}
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
style.configure('Pink.TButton', background='#F0F0F8',foreground='#404040',font=('Arial Bold',16))

def calculate_currency(): 
    from_item = listbox_from.curselection()
    to_item = listbox_to.curselection()
    amount = Input.get()

    if not amount:
        Result.set("Please enter an amount")
    else:
        amount = float(amount)
        from_index = from_item[0]
        from_item = list(items)[from_index]
        to_index = to_item[0]
        to_item = list(items)[to_index]
        exchange_rate = items[from_item][to_item][0]
        currency = amount * exchange_rate
        Result.set(f"Result: {currency:.2f}")
  
    

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
convert_button.pack(fill='y', expand=False, pady=10)



style = ttk.Style()
style.configure('TLabel', background='#FFFF00')


root.configure(bg='#FFFF00')


root.mainloop()





        
