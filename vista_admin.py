import tkinter as tk

def mostrar_vista_admin(ventana):
    for widget in ventana.winfo_children():
        widget.destroy()
    
    tk.Label(ventana, text="Bienvenido, Administrador").pack()
    # Agregar más elementos de la interfaz aquí según sea necesario
