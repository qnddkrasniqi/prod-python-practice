import tkinter as tk

window = tk.Tk()

window.rowconfigure(list(range(9)), weight=1, minsize=5)
window.columnconfigure([0, 1], weight=1, minsize=40)

label_names = [
    'First name:', 'Last name:', 'Address Line1:',
    'Address Line 2', 'City:', 'State/Provice:',
    'Postal Code:', 'Country:'
]

for i, label_name in enumerate(label_names):
    label = tk.Label(master=window, text=label_name)
    entry = tk.Entry(master=window, width=50)

    label.grid(row=i, column=0)
    entry.grid(row=i, column=1)

frame = tk.Frame(master=window)
frame.grid(row=8, column=0, columnspan=2, sticky='e')

clear_btn = tk.Button(master=frame, text='Clear')
clear_btn.grid(row=0, column=0, padx=5, pady=3)

submit_btn = tk.Button(master=frame, text='Submit')
submit_btn.grid(row=0, column=1, padx=5, pady=3)

window.mainloop()
