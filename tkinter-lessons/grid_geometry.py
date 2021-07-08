import tkinter as tk

window = tk.Tk()

"""
window.rowconfigure([0, 1], weight=1, minsize=75)
window.columnconfigure([0, 1], weight=1, minsize=75)
frame = tk.Frame(master=window, relief=tk.RAISED, borderwidth=1)
frame.grid(row=0, column=0)

label = tk.Label(master=frame, text=f"Row {0}\nColumn {0}")
label.pack()

frame1 = tk.Frame(master=window, relief=tk.RAISED, borderwidth=1)
frame1.grid(row=0, column=1)

label1 = tk.Label(master=frame1, text=f"Row {0}\nColumn {1}")
label1.pack()

frame2 = tk.Frame(master=window, relief=tk.RAISED, borderwidth=1)
frame2.grid(row=1, column=1)

label2 = tk.Label(master=frame2, text=f"Row {1}\nColumn {1}")
label2.pack()
"""

window.columnconfigure([0, 1, 2], weight=1, minsize=75)
window.rowconfigure([0, 1, 2], weight=1, minsize=50)

for row in range(3):
    for column in range(3):
        print(row, column)
        frame = tk.Frame(master=window, relief=tk.RAISED, borderwidth=1)
        frame.grid(row=row, column=column, padx=5, pady=5)

        label = tk.Label(master=frame, text=f"Row {row}\nColumn {column}")
        label.pack(padx=5, pady=5)

window.mainloop()
