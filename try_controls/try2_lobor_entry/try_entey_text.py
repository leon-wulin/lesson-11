# -*- coding: UTF-8 -*-
# writen by leon
# writen time: 2019/12/7



import tkinter as tk
from tkinter import ttk

top_win=tk.Tk()

top_win.title('Hellow world window')

win_size_pos='800x600'

top_win.geometry(win_size_pos)

entry_classtext=tk.Entry(
    top_win,
    show='',
    width=50,
    font=('Arial',14)
)
entry_classtext.place(x=100,y=100)

top_win.mainloop()
