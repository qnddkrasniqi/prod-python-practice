import tkinter as tk


window = tk.Tk()

greeting = tk.Label(
    master=window,
    text='Hello, Tkinter',
    fg='white',
    bg='black',
    width=10,
    height=10
)

greeting.pack()

window.mainloop()
