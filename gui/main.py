# -*- coding: UTF-8 -*-
# writen by leon
# writen time: 2019/12/21



import tkinter.messagebox
import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk

from class_login import UC_Login
from show import UC_Show
root=tk.Tk()

form_login=UC_Login(root)

root.mainloop()
root.destroy()

root=tk.Tk()
from_show=UC_Show()
root.mainloop()
