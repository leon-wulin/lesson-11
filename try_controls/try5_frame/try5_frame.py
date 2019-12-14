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
frame_root1=tk.Frame(top_win,bg='#60F4F4',width=760,height=200)

frame_root1.place(x=20,y=20)

lbl_test=tk.Label(frame_root1,text='text in frame',bg='#FF7A22')
lbl_test.place(x=20,y=20)
#-------------------------------------------------------------------------------
top_win.geometry(win_size_pos)

top_win.mainloop()
