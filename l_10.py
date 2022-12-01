# -*- coding: utf-8 -*-
"""
Created on Thu Dec  1 15:26:59 2022

@author: dvory
"""

from tkinter import*
from tkinter import ttk
from tkinter.ttk import Radiobutton
from tkinter import messagebox
from tkinter import filedialog
from tkinter import Menu
from tkinter import filedialog
from tkinter.ttk import Combobox

def clicked():
    messagebox.showinfo('Окно', f'Вы нажали {selected.get()}')
def clicked1():
    file = filedialog.askopenfilename(filetypes = (("Textfiles","*.txt"),("all files","*.*")))
    file1=open(file, 'r')
    lb1.configure(text=file1.read())
    file1.close()
def clicked2():
    ch1 = int(chis1.get())
    ch2 = int(chis2.get())
    if (combo.get() == "+"):
        lb2.configure(text=(ch1+ch2))
    if (combo.get() == "-"):
        lb2.configure(text=(ch1-ch2))
    if (combo.get() == "*"):
        lb2.configure(text=(ch1*ch2))
    if (combo.get() == "/"):
        lb2.configure(text=(ch1/ch2))
        
    
    
windows = Tk()
windows.title("Дворянов.Д.Г Ум-222")
windows.geometry('400x250')
tab_control = ttk.Notebook(windows)
tab1 = ttk.Frame(tab_control)
tab2 = ttk.Frame(tab_control)
tab3 = ttk.Frame(tab_control)
tab_control.add(tab1, text = 'Калькулятор')
tab_control.add(tab2, text = 'Выбор')
tab_control.add(tab3, text = 'Файл')

#2
selected=IntVar()
btn = Button(tab2, text='Клик', command=clicked)
rad1 = Radiobutton(tab2, text = '1', value=1, variable=selected)
rad2 = Radiobutton(tab2, text = '2', value=2, variable=selected)
rad3 = Radiobutton(tab2, text = '3', value=3, variable=selected)
rad1.grid(column=0, row=0)
rad2.grid(column=1, row=0)
rad3.grid(column=2, row=0)
btn.grid(column=3, row=0)

#3
lb1=Label(tab3)
menu = Menu(windows)
new_item = Menu(menu)
new_item.add_command(label='Зайгрузить файл', command=clicked1)
menu.add_cascade(label='Файл', menu=new_item)
windows.config(menu=menu)
lb1.grid(column=1, row=0)

#1
chis1 = Entry(tab1)
chis2 = Entry(tab1)
chis1.grid(row=0, column=1, padx=5, pady=2)
chis2.grid(row=0, column=3, padx=5, pady=2)
combo = Combobox(tab1)
combo['values'] = ('+', '-', '*', '/')
combo.grid(column=2, row=0)
bt = Button(tab1, text='Клик', command=clicked2)
bt.grid(column=2, row=1)
lb2=Label(tab1)
lb2.grid(column=4, row=0)

tab_control.pack(expand=1, fill='both')
windows.mainloop()