import tkinter as tk

def mostrar_vista_usuario(ventana):
    for widget in ventana.winfo_children():
        widget.destroy()
    
    tk.Label(ventana, text="Bienvenido, Usuario").pack()
    # Agregar más elementos de la interfaz aquí según sea necesario
    