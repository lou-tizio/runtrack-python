from tkinter import *
import math
import tkinter.messagebox

root = Tk()
root.title("scientific calculator")
root.configure("background=blue")
root.resizable(width=False, height=False)
root.geometry("485x568+0+0")

calculator = Frame(root)
calculator.grid( )

menubar = Menu(calculator)
filename = Menu(menubar, tearoff=0)

menubar.add_cascade(label="Fichier", menu=filename)
filename.add_command(label="standard")
filename.add_command(label="scientific")
filename.add_separator()
filename.add_command(label="Quitter")

root.config(menu=menubar)
root.mainloop()