# -*- coding: UTF-8 -*-
# writen by leon
# writen time: 2019/12/7



import tkinter as tk
from tkinter import ttk
import tkinter.messagebox
from PIL import Image, ImageTk

top_win=tk.Tk()

top_win.title('Hellow world window')

win_size_pos='800x600'

top_win.geometry(win_size_pos)


'''
def cmd_print():

    print('Show in command window...')
    return

'''

def cmd_pop():
    tk.messagebox.showinfo(title='Information',message='Mouse clicked')
    tk.messagebox.showwarning(title='Warning',message='Warning information')
    tk.messagebox.showerror(title='Error',message='Error information')
    print('Show in command window...')
    return

    '''
btn_help=tk.Button(top_win,text="push me",command=cmd_pop)
btn_help.pack()

'''
button_relieves = ('flat', 'groove', 'raised', 'ridge', 'solid', 'sunken')

for r in button_relieves:
    tk.Button(top_win,text=r,relief=r,width=10,height=2).pack()


top_win.mainloop()
