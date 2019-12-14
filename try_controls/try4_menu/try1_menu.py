# -*- coding: UTF-8 -*-
# writen by leon
# writen time: 2019/12/14



import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
top_win=tk.Tk()

top_win.title('Hellow world window')

win_size_pos='800x600'

#-------------------------------------------------------------------------------

top_menu =tk.Menu(top_win)
top_menu.add_command(label='hello',command=None)
top_menu.add_command(label='quit',command=top_win.quit)

top_win.config(menu=top_menu)
#-------------------------------------------------------------------------------
top_win.geometry(win_size_pos)

top_win.mainloop()
