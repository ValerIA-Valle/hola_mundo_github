from tkinter import ttk, messagebox
import tkinter as tk


from views.sistema_principal import *

class Login(ttk.Frame):
    def __init__(self, ventana):
        super().__init__(ventana)

        self.ven = ventana
        self.ven.geometry("350x450")
        self.ven.title("Sistema Login")
        self.ven.config(bg = "#FFE5EC") 
        self.ven.resizable(False, False)
        self.ven.wm_attributes("-alpha", 0.95)
        self.ven.iconbitmap("iconos/ico.png")

        #barra de menu
        self.ven.overrideredirect(True)

        def Salir():
            self.ven.destroy()

        def Ingresar():
            try:
                if(self.user.get() == "" and self.pas.get() == ""):
                    messagebox.showerror("Error", "Debe ingresar usuario y contraseña")
                else:
                    usuario = self.user.get()
                    contraseña = self.pas.get()
                    if(usuario == "vale" and contraseña == "1411"):
                        messagebox.showinfo("Bienvenido", "Inicio de sesión exitoso 🦋", )
                        self.ven.destroy()
                        SistemaPrincipal()
            except:
                pass

        #boton para salir de la ventana
        self.btnSalir= tk.Button(self.ven, text="X", width=4, height=1, font=("Arial", 10, "bold"), command=Salir, bd=0, fg="white")
        self.btnSalir.place(x=305, y=10)
        self.btnSalir.config(bg="#E0A96D")

        #variables
        self.user = tk.StringVar()
        self.pas = tk.StringVar()

        # Cargamos la imagen original
        self.img = tk.PhotoImage(file="imagenes/image.png").subsample(4, 4)

        #etiquetas
        #etiqueta para la imagen de logo 
        self.lblLogo = tk.Label(self.ven, image=self.img)
        self.lblLogo.place(x=120, y=15) 
        self.lblLogo.config(bg="#FFE5EC")

        # titulo 
        self.lblTitulo = tk.Label(self.ven, text="ACCESO AL SISTEMA", font=("Arial", 14, "bold"), fg="#4A3E3D")
        self.lblTitulo.place(x=65, y=120)
        self.lblTitulo.config(bg="#FFE5EC")

        # campo de usuario 
        self.lblUser = tk.Label(self.ven, text="Usuario:", font=("Arial", 11, "bold"), fg="#D4AF37") 
        self.lblUser.place(x=65, y=175)
        self.lblUser.config(bg="#FFE5EC")
        
        self.txtUser = tk.Entry(self.ven, textvariable=self.user, font=("Arial", 12), bd=1, relief="solid")
        self.txtUser.place(x=65, y=205, width=220, height=30) 
        self.txtUser.config(bg="#ffffff")

        #campo de contraseña
        self.lblPass = tk.Label(self.ven, text="Contraseña:", font=("Arial", 11, "bold"), fg="#D4AF37") 
        self.lblPass.place(x=65, y=255)
        self.lblPass.config(bg="#FFE5EC")

        self.txtPass = tk.Entry(self.ven, textvariable=self.pas, font=("Arial", 12), bd=1, relief="solid", show="*")
        self.txtPass.place(x=65, y=285, width=220, height=30)
        self.txtPass.config(bg="#ffffff")

        #botón de inicio de sesión 
        self.btnIngresar = tk.Button(self.ven, text="Ingresar", font=("Arial", 12, "bold"),  bd=0, fg="white", command=Ingresar)
        self.btnIngresar.place(x=65, y=350, width=220, height=40)
        self.btnIngresar.config(bg="#E0A96D")


