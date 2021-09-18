from tkinter import Tk
from tkinter import Frame
from tkinter import *

#Crear compnente raiz
root = Tk()
root.title("Hola mundo")
root.resizable(1,1)

frame =  Frame(root,width=500, height=500)
frame.pack(fill='both', expand=1)
frame.config(cursor='pirate')
frame.config(bg='white')
frame.config(bd='25')
frame.config(relief='sunken')

root.config(cursor='spider')
root.config(bg='green')
root.config(bd='10')
root.config(relief='ridge')

#Crear etiquetas : Label
etiqueta_nombre = Label(frame, text='Nombre: ')
etiqueta_nombre.pack(fill='both')

#Crear Caja de texto : Entry
entry_nombre = Entry(frame)
entry_nombre.pack(fill='both')

#TextArea
text_area = Text(frame)
text_area.pack(fill='both')



root.mainloop()
