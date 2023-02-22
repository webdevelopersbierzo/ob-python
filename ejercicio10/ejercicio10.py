import sys
import tkinter
from tkinter import ttk

windows = tkinter.Tk()

windows.columnconfigure(0, weight=1)
windows.columnconfigure(1, weight=3)
seleccionado = tkinter.StringVar()

r1 = ttk.Radiobutton(windows, text='Si', value='1', variable='selected')
r2 = ttk.Radiobutton(windows, text='NO', value='1', variable='selected')
r3 = ttk.Radiobutton(windows, text='Quizas', value='1', variable='selected')

r1.grid(column=0, row=1, pady=5, padx=0)
r2.grid(column=0, row=2, pady=5, padx=0)
r3.grid(column=0, row=3, pady=5, padx=0)

windows.mainloop()
sys.exit(0)