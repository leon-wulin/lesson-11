# -*- coding: UTF-8 -*-
# writen by leon
# writen time: 2019/12/21


import tkinter.messagebox
import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk


class UC_Login:
    def __init__(self, pwin):
        print('text UC_Login class!')
        self.parent_win = pwin

        self.parent_win.title('login - by class')

        win_size_pos='240x200'

        self.parent_win.geometry(win_size_pos)

        self.__init_widgets()
        return

    def __init_widgets(self):
        '对本窗体自动布局'

        lbl_info = tk.Label(
            self.parent_win,
            text='login form',
            fg='yellow',
            bg='blue',
            width=27,
            height=1
        )
        lbl_info.place(x=20,y=20)


        default_var=tk.StringVar(value='username')
        self.entry_classtext=tk.Entry(
            self.parent_win,
            show=None,
            textvariable=default_var,
            font=('Arial',14)
        )
        self.entry_classtext.place(x=10,y=50)



        default_var=tk.StringVar(value='password')
        self.entry_classtext2=tk.Entry(
            self.parent_win,
            show=None,
            textvariable=default_var,
            font=('Arial',14)
            )


        btn_signin=tk.Button(self.parent_win,text="sign in",command= self.__cmd_login)
        btn_signin.place(x=10,y=150)


        btn_help=tk.Button(self.parent_win,text="forget password?",command= self.__cmd_help)
        btn_help.place(x=90,y=150)

        self.entry_classtext2.place(x=10,y=100)

        return

    def __cmd_login(self):
        un=self.entry_classtext.get()
        pw=self.entry_classtext2.get()
        if un=='king':
            if pw=='123':
                tk.messagebox.showinfo(title='sign in',message='login success')
                self.login_status='OK'
                self.parent_win.quit()
            else:
                tk.messagebox.showerror(title='Error',message='wrong password')
                self.login_status='NO'
        else:
            tk.messagebox.showerror(title='Error',message='wrong username')
            self.login_status='NO'
        return
    def __cmd_help(self):
        tk.messagebox.showinfo(title='help',message='username: king \n password:123')
        return
