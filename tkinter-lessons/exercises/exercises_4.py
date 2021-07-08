import tkinter as tk

window = tk.Tk()

ent_pupc = tk.Entry(master=window, fg='white', bg='purple', width=50)
ent_pupc.pack()

ent_pupc.insert(0, 'A po lun me pupca?')

window.mainloop()
