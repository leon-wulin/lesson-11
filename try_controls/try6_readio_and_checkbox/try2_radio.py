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
var_sel.set(0)
text_of_btn = ('北京', '上海', '广州', '深圳')
value_of_btn=(0,1,2,3)


def show_seleted():
    v=var_sel.get()
    print(text_of_btn[v])
    return


for idx in range(4):
    red_btn = tk.Radiobutton(
        frame_root1,
        text=text_of_btn[idx],
        variable=var_sel,
        value=value_of_btn[idx],
        command=show_seleted
    )
    red_btn.place(x=20 + idx * 190, y=40)
#-------------------------------------------------------------------------------

top_win.geometry(win_size_pos)

top_win.mainloop()
