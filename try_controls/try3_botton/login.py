# -*- coding: UTF-8 -*-
# writen by leon
# writen time: 2019/12/7

import tkinter as tk
from tkinter import ttk
import tkinter.messagebox
from PIL import Image, ImageTk

top_win=tk.Tk()

top_win.title('login')

win_size_pos='240x200'

lbl_info = tk.Label(
    top_win,
    text='login form',
    fg='yellow',
    bg='blue',
    width=27,
    height=1
)
lbl_info.place(x=20,y=20)

default_var=tk.StringVar(value='username')
entry_classtext=tk.Entry(
    top_win,
    show=None,
    textvariable=default_var,
    font=('Arial',14)
)
entry_classtext.place(x=10,y=50)

default_var=tk.StringVar(value='password')
entry_classtext2=tk.Entry(
    top_win,
    show=None,
    textvariable=default_var,
    font=('Arial',14)
    )
def cmd_login():
    un=entry_classtext.get()
    pw=entry_classtext2.get()
    if un=='king':
        if pw=='123':
            tk.messagebox.showinfo(title='sign in',message='login success')
        else:
            tk.messagebox.showerror(title='Error',message='wrong password')
    else:
        tk.messagebox.showerror(title='Error',message='wrong username')
    return

btn_signin=tk.Button(top_win,text="sign in",command=cmd_login)
btn_signin.place(x=10,y=150)

def cmd_help():
    tk.messagebox.showinfo(title='help',message='username: king \n password:123')
    return

btn_help=tk.Button(top_win,text="forget password?",command=cmd_help)
btn_help.place(x=90,y=150)

entry_classtext2.place(x=10,y=100)

top_win.geometry(win_size_pos)
top_win.mainloop()
