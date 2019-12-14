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
prog_total=600
p=ttk.Progressbar(
    top_win,
    orient='horizontal',
    length=prog_total,
    mode='determinate',
    maximum=prog_total
)

'''
cursor	鼠标位于进度条内时的形状
length	进度条长度
maximum	进度条最大刻度值
mode 	进度条的模式。有两种：‘determinate’和’indeterminate’
orient	进度条的方向，有HORIZONTAL 和VERTICAL两种
style	定义进度条的外观
takefocus	是否可以通过Tab获得输入焦点
variable	与进度条关联的变量。可以设置或获得进度条的当前值
value	设置或者获取进度条的当前值
'''
p.pack()
def prog_start():
    p.start()
    return
def prog_stop():
    p.stop()
    return
btn_start_auto=tk.Button(
    top_win,
    text='Auto start progress',
    command=prog_start
)
btn_start_auto.pack()


btn_stop=tk.Button(top_win,text='stop progress',command=prog_stop)
btn_stop.pack()
prog_current=0
def prog_set():
    global prog_current
    prog_current+=10
    p['value']=prog_current
    return

btn_start_manual=tk.Button(top_win,text='Manual start progress',command=prog_set)
btn_start_manual.pack()
#-------------------------------------------------------------------------------

top_win.geometry(win_size_pos)

top_win.mainloop()
