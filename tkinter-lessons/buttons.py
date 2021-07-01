import tkinter as tk


def print_smth():
    print('smth')


window = tk.Tk()

button = tk.Button(
    master=window,
    text='Click me!',
    command=print_smth
)

button.pack()

window.mainloop()
