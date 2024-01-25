import tkinter as tk
from tkinter import messagebox
import vista_admin
import vista_usuario
from base_de_datos.cleinte_db import validar_usuario, ingresar_dato


class Ventana_login:
    #constructor
    def __init__(self, ventana):
        self.ventana = ventana
        self.ventana.title("Sistema de Inicio de Sesión")
        self.crear_vista_login()

#ventana principal donde carga el login
    def crear_vista_login(self):
        self.limpiar_pantalla()

        tk.Label(self.ventana, text="Usuario:").pack()
        self.entry_usuario = tk.Entry(self.ventana)
        self.entry_usuario.pack()

        tk.Label(self.ventana, text="Contraseña:").pack()
        self.entry_contraseña = tk.Entry(self.ventana, show="*")
        self.entry_contraseña.pack()

        boton_login = tk.Button(self.ventana, text="Iniciar Sesión", command= lambda: validar_usuario(self.entry_usuario,
                                                                                                         self.entry_contraseña))
        boton_login.pack()
        
        boton_crear_usuario = tk.Button(self.ventana, text="Crear usuario", command=self.crear_registro)
        boton_crear_usuario.pack()
    
    #creacion de ventana segundaria para poder registrar una cuenta
    def crear_registro(self):
         registro = tk.Toplevel()
         registro.title("Registro")
         
         tk.Label(registro, text='Ingresa tu nombre completo').pack()
         self.nombre = tk.Entry(registro)
         self.nombre.pack()
         
         tk.Label(registro, text='Ingresa tu numero de telefono').pack()
         self.numero = tk.Entry(registro)
         self.numero.pack()
         
         tk.Label(registro, text='Ingresa tu correo electronico').pack()
         self.correo = tk.Entry(registro)
         self.correo.pack()
         
         tk.Label(registro, text='Ingresa tu direccion').pack()
         self.direccion = tk.Entry(registro)
         self.direccion.pack()
         
         tk.Label(registro, text='Ingresa tu contraseña').pack()
         self.contraseña = tk.Entry(registro, show= '*')
         self.contraseña.pack()
         
         self.guardar = tk.Button(registro, text='Guardar', command= lambda:ingresar_dato(self.nombre.get(), 
                                                                                                  int(self.numero.get()),
                                                                                                  self.correo.get(),
                                                                                                  self.direccion.get(),
                                                                                                  self.contraseña.get()))
         self.guardar.pack()

    '''def validar_login(self):
        usuario = self.entry_usuario.get()
        contraseña = self.entry_contraseña.get()

        if usuario == "admin" and contraseña == "admin123":
            vista_admin.mostrar_vista_admin(self.ventana)
        elif usuario == "user" and contraseña == "user123":
            vista_usuario.mostrar_vista_usuario(self.ventana)
        else:
            messagebox.showerror("Error", "Credenciales incorrectas")'''

    def limpiar_pantalla(self):
        for widget in self.ventana.winfo_children():
            widget.destroy()

ventana = tk.Tk()
app = Ventana_login(ventana)
ventana.mainloop()
