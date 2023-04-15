# GUI - Graphical User Interface
# Tkinter - TK Interface
# Importamos el módulo de tkinter
import tkinter as tk
# Importamos el módulo del tema de tkinter
from tkinter import PhotoImage, ttk

import os, sys

# Creamos un objeto usando la clase Tk
ventana = tk.Tk()
# Modificamos el tamaño de la ventana (pixeles)
ventana.geometry('600x400')
# Cambiamos el nombre de la ventana
ventana.title('Hola Mundo')
# Configuramos el ícono de la aplicación
photo = PhotoImage(file="play.png")
ventana.iconphoto(False, photo)
# Creamos un boton (widget), el objeto padre es ventana
boton1 = ttk.Button(ventana, text='Dar click')
# Utilizar el pack layout manager para mostrar el botón de la ventana
boton1.pack()
# Iniciamos la ventana (esta línea la ejecutamos al final)
# Si la ejecutamos antes, no se muestran los cambios anteriores
ventana.mainloop()

# import tkinter as tk

# ventana = tk.Tk()
# ventana.geometry('600x400')
# ventana.title('Hola Mundo')
# ventana.iconbitmap('./icono.ico')
# ventana.mainloop()