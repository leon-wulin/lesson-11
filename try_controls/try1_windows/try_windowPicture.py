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
image=Image.open('图片2.png')
bk_img=ImageTK.PhotoImage(image)    

lbl_background=tk.Label(
    top_win,
    text='hello word',
    bg='blue'
)

lbl_background.place(x=0,y=0,width=800,height=600)
#-------------------------------------------------------------------------------

top_win.geometry(win_size_pos)

top_win.mainloop()
