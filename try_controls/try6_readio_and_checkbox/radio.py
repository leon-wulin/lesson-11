# -*- coding: UTF-8 -*-
# writen by leon
# writen time: 2019/12/14


import tkinter.messagebox
import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
top_win=tk.Tk()

top_win.title('Hellow world window')

win_size_pos='800x600'
#-------------------------------------------------------------------------------
frame_root1 = tk.Frame(top_win, bg='gray', width=760, height=300)
frame_root1.place(x=20, y=20)

var_sel=tk.IntVar()
var_sel.set(1)


def show_seleted():
    print(var_sel.get())
    return
radio_btn1=tk.Radiobutton(
    frame_root1,
    text='one',
    value=1,
    variable=var_sel,
    bg="#60F4F4",
    fg='white',
    command=show_seleted
)
radio_btn1.place(x=20,y=20)


radio_btn2=tk.Radiobutton(
    frame_root1,
    text='two',
    value=2,
    variable=var_sel,
    bg="#60F4F4",
    fg='white',
    command=show_seleted
)
radio_btn2.place(x=220,y=20)


radio_btn3=tk.Radiobutton(
    frame_root1,
    text='three',
    value=3,
    variable=var_sel,
    bg="#60F4F4",
    fg='white',
    command=show_seleted
)
radio_btn3.place(x=420,y=20)
#-------------------------------------------------------------------------------

top_win.geometry(win_size_pos)

top_win.mainloop()
