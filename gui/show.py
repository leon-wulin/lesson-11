# -*- coding: UTF-8 -*-
# writen by leon
# writen time: 2019/12/21



import tkinter.messagebox
import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk

class UC_Show:
    def __init__(self, pwin):
        print('text UC_Show class!')
        self.parent_win = pwin

        self.parent_win.title('show - by class')

        win_size_pos='800x600'

        self.parent_win.geometry(win_size_pos)

        self.__init_widgets()
        return

    def __init_widgets(self):
        '对本窗体自动布局'

        lbl_info = tk.Label(
            self.parent_win,
            text='show form',
            fg='yellow',
            bg='blue',
            width=27,
            height=1
        )
        lbl_info.place(x=20,y=20)
