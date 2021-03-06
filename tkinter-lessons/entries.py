import tkinter as tk


def get_entry_text():
    entry_text = entry.get()
    print(entry_text)


def delete_entry_text():
    entry.delete(0, tk.END)


def insert_text():
    entry.insert(0, 'Python')


window = tk.Tk()

label = tk.Label(master=window, text='Name')
entry = tk.Entry(master=window, fg='black', bg='white', width=50)

button = tk.Button(
    master=window,
    text='Get Entry Text',
    command=get_entry_text
)

delete_btn = tk.Button(
    master=window,
    text='Delete Entry Text',
    command=delete_entry_text
)

insert_btn = tk.Button(
    master=window,
    text='Insert Text',
    command=insert_text
)

label.pack()
entry.pack()
button.pack()
delete_btn.pack()
insert_btn.pack()

window.mainloop()
