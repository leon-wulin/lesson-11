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
tittle='my lable frame'
lfm_step1=ttk.Labelframe(
top_win,text=tittle,width=240, height=500)
lfm_step1.place(x=20,y=20)

lbl_text=tk.Label(lfm_step1,text='oh! mygod',bg='blue',fg='white')
lbl_text.grid(row=0,column=0,pady=10,padx=10)

lbl_text=tk.Label(lfm_step1,text='oh! mygod',bg='blue',fg='white')
lbl_text.grid(row=1,column=0,pady=5,padx=5)

lbl_text=tk.Label(lfm_step1,text='oh! mygod',bg='blue',fg='white')
lbl_text.grid(row=2,column=0,pady=5,padx=5)

lbl_text=tk.Label(lfm_step1,text='oh! mygod',bg='blue',fg='white')
lbl_text.grid(row=3,column=0,pady=5,padx=5)

lbl_text=tk.Label(lfm_step1,text='oh! mygod',bg='blue',fg='white')
lbl_text.grid(row=4,column=0,pady=5,padx=5)

lbl_text=tk.Label(lfm_step1,text='oh! mygod',bg='blue',fg='white')
lbl_text.grid(row=0,column=1,pady=5,padx=5)

lbl_text=tk.Label(lfm_step1,text='oh! mygod',bg='blue',fg='white')
lbl_text.grid(row=1,column=1,pady=5,padx=5)

lbl_text=tk.Label(lfm_step1,text='oh! mygod',bg='blue',fg='white')
lbl_text.grid(row=2,column=1,pady=5,padx=5)

lbl_text=tk.Label(lfm_step1,text='oh! mygod',bg='blue',fg='white')
lbl_text.grid(row=3,column=1,pady=5,padx=5)

lbl_text=tk.Label(lfm_step1,text='oh! mygod',bg='blue',fg='white')
lbl_text.grid(row=4,column=1,pady=5,padx=5)
#-------------------------------------------------------------------------------

top_win.geometry(win_size_pos)

title='My label frame generated by for'
lfm_step2=ttk.Labelframe(
top_win,text=title,width=240, height=500)
lfm_step2.place(x=400,y=20)

for r in range(5):
    for c in range(3):
        ent_row=tk.Entry(
            lfm_step2,
            show=None,
            width=5,
            bg='red',
            fg='white')
        ent_row.grid(row=r,column=c,pady=5,padx=5)
top_win.mainloop()
