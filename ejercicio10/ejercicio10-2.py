import sys
import tkinter
from tkinter import ttk

window = tkinter.Tk()

window.columnconfigure(0, weight=1)
window.columnconfigure(1, weight=3)

frame = ttk.Frame(window)

label = tkinter.Label(frame, text="Quien ganara la champions")
label.grid(column=0, row=0, sticky=tkinter.W, padx=10, pady=10)
lista = ['Real Madrid', 'Barcelona', 'Liverpool', 'Manchester city','PSG' ]
lista_item = tkinter.StringVar(value=lista)

listbox = tkinter.Listbox(window, height=100, listvariable=lista_item)

listbox.grid(column=0, row=1, sticky=tkinter.W)

frame.grid(column=0, row=0, sticky=tkinter.W)

window.mainloop()
sys.exit(0)