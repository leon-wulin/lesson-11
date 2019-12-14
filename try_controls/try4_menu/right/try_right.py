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
def cmd_undo():
    tk.messagebox.showinfo(title='info',message='undo')
    return
def cmd_redo():
    tk.messagebox.showinfo(title='info',message="redo")
    return

menubar=tk.Menu(top_win)
menubar.add_command(label='undo',command=cmd_undo)
menubar.add_command(label='redo',command=cmd_redo)


frame=tk.Frame(top_win,width=400,heigh=400,bg='blue')
frame.pack()
def popup(event):
    menubar.post(event.x_root,event.y_root)
frame.bind('button-3',popup)
#-------------------------------------------------------------------------------

top_win.geometry(win_size_pos)

top_win.mainloop()
