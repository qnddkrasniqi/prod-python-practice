import tkinter as tk

window = tk.Tk()

text_box = tk.Text()
text_box.pack()


def get_text():
    txt = text_box.get('1.0', '2.5')
    print(txt)


def insert_text():
    text_box.insert(tk.END, 'Hello')


get_btn = tk.Button(
    master=window,
    text='Get text',
    command=get_text
)

insert_btn = tk.Button(
    master=window,
    text='Insert text',
    command=insert_text
)

get_btn.pack()
insert_btn.pack()

window.mainloop()
