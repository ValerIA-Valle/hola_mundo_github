from tkinter import ttk
import tkinter as tk

class Login(ttk.Frame):
    def __init__(self, ventana):
        super().__init__(ventana)

        self.ven = ventana
        self.ven.geometry("350x450")
        self.ven.title("Sistema Login")
        self.ven.config(bg = "#00ddff")
        self.ven.resizable(False, False)
        self.ven.wm_attributes("-alpha", 0.89)
        self.ven.iconbitmap("iconos/ico.png")

        #Quitamos la barra del menú
        self.ven.overrideredirect(True)

        def Salir():
            self.ven.destroy()

        #ponemos un botón para cerrar la ventana
        self.btnSalir= tk.Button(self.ven, text="X", width=6, height=2, command=Salir)
        self.btnSalir.place(x=290, y=5)
        self.btnSalir.config(bg="#ffaa00")

        