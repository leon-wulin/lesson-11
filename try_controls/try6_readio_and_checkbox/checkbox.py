# -*- coding: UTF-8 -*-
# writen by leon
# writen time: 2019/12/14


import tkinter.messagebox
import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
top_win = tk.Tk()

top_win.title('Hellow world window')

win_size_pos = '800x600'
# -------------------------------------------------------------------------------
frame_root1 = tk.Frame(top_win, bg='light blue', width=760, height=300)
frame_root1.place(x=20, y=20)

text_of_btn = ('北京', '上海', '广州', '深圳')
v1 = tk.IntVar()
v2 = tk.IntVar()
v3 = tk.IntVar()
v4 = tk.IntVar()
value_of_btn = (v1, v2, v3, v4)
'''
    chk_btn1=tk.Checkbutton(
            frame_root1,
            text=text_of_btn[0],
            commad=None
    )
    chk_btn1.place(x=20,y=40)
'''
def show_seleted():
    print('-------------')
    for v in value_of_btn:
        print(v.get())
    return

for idx in range(4):
    chk_btn1 = tk.Checkbutton(
        frame_root1,
        text=text_of_btn[idx],
        variable=value_of_btn[idx],
        command=show_seleted
    )
    chk_btn1.place(x=20 + idx * 190, y=40)
# -------------------------------------------------------------------------------

top_win.geometry(win_size_pos)

top_win.mainloop()
