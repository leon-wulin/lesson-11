# -*- coding: UTF-8 -*-
# writen by leon
# writen time: 2019/12/7


import tkinter as tk
from tkinter import ttk
from PIL import image,imageTk
top_win = tk.Tk()

top_win.title('Hellow world window')

win_size_pos = '800x600'

top_win.geometry(win_size_pos)


# --------------------------------------

lbl_hello = tk.Label(
    top_win,
    text='Hello World!',
    fg='white',
    bg='blue',
    font=('Arial', 12),
    width=30,
    height=2
)
lbl_hello.pack()


lbl_programmer = tk.Label(
    top_win, text='I am a programmer '
)


image = image.open('Mr rorys fantastic picture.jpg')
bk_img = ImageTK.PhotoImage(image)
lbl_bk=tk.Label(top_win,image=bk_img)
lbl_bk = pack()
# --------------------------------------

top_win.mainloop()
