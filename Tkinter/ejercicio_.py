import tkinter as tk
from tkinter import ttk, messagebox, Menu



ventana = tk.Tk()

ventana.geometry('330x130')
ventana.title('Login')

usuario = tk.Label(ventana, text='Usuario:', justify='right')
usuario.grid(row=0, column=0,padx=5,pady=7, ipadx=5, ipady=3)

entrada_usuario = ttk.Entry(ventana, width=25, justify='left')
entrada_usuario.grid(row=0,column=1,padx=5,pady=7, ipadx=5, ipady=6)

password = tk.Label(ventana, text='Password:', justify='right')

password.grid(row=1, column=0,padx=3,pady=7, ipadx=5, ipady=3)

entrada_password = ttk.Entry(ventana, width=25, justify='left', show='*')
entrada_password.grid(row=1,column=1,padx=3,pady=7, ipadx=5, ipady=6)

def login():
    texto_usuario = entrada_usuario.get()
    texto_password = entrada_password.get()
    if texto_password and texto_usuario:
        messagebox.showinfo('DatosLogin ', 'Usuario: ' + texto_usuario  + ', Password: ' + texto_password)
    #messagebox.showwarning('No ha ingresado Datos')

boton_login = tk.Button(ventana, text='Login', command=login)
boton_login.grid(row=3,column=1)

ventana.mainloop()