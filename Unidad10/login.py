from tkinter import Tk
from tkinter import Frame
from tkinter import *


def saludo():
    print("Hola")

#Crear compnente raiz
root = Tk()
root.resizable(10,10)

label_nombre = Label(root, text='Usuario:')
label_nombre.grid(row=0, column=0, sticky=W, padx=10, pady=10)

entry_nombre = Entry(root)
entry_nombre.grid(row=0, column=1, sticky=W, padx=10, pady=10)

label_password = Label(root, text='Password:')
label_password.grid(row=1, column=0, sticky=W, padx=10, pady=10)

entry_password = Entry(root)
entry_password.grid(row=1, column=1, sticky=W, padx=10, pady=10)
entry_password.config(justify='center', show='*')

#Botones

boton_1 = Button(root, text='Login', command='')
boton_1.grid(row=2, column=0, sticky=W, padx=10, pady=10)

boton_2 = Button(root, text='Cancelar', command=saludo)
boton_2.grid(row=2, column=1, sticky=W, padx=10, pady=10)

root.mainloop()