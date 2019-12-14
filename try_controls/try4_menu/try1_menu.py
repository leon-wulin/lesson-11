# -*- coding: UTF-8 -*-
# writen by leon
# writen time: 2019/12/14



import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
import tkinter.messagebox
top_win=tk.Tk()

top_win.title('Hellow world window')

win_size_pos='800x600'

#-------------------------------------------------------------------------------

top_menu =tk.Menu(top_win)
#top_menu.add_command(label='hello',command=None)
#top_menu.add_command(label='quit',command=top_win.quit)

def cmd_menu_item():
    tk.messagebox.showinfo(title='information',
                           message='Menu item clicked!')
    return

filemenu=tk.Menu(top_menu,tearoff=False)
filemenu.add_command(label='open',command=cmd_menu_item)
filemenu.add_command(label='save',command=cmd_menu_item)
filemenu.add_separator()
filemenu.add_command(label='quit',command=top_win.quit)
top_menu.add_cascade(label='file',menu=filemenu)

filemenu=tk.Menu(top_menu,tearoff=False)
filemenu.add_command(label='select all',command=cmd_menu_item)
filemenu.add_separator()
filemenu.add_command(label='copy',command=cmd_menu_item)
filemenu.add_command(label='cut',command=cmd_menu_item)
filemenu.add_command(label='paste',command=cmd_menu_item)
top_menu.add_cascade(label='function',menu=filemenu)





top_win.config(menu=top_menu)
#-------------------------------------------------------------------------------
top_win.geometry(win_size_pos)

top_win.mainloop()
