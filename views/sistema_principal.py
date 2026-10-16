import tkinter as tk
from tkinter import ttk, messagebox

class SistemaPrincipal:
    def __init__(self):
        self.ventana = tk.Tk()
        self.ventana.title("Sistema Principal")
        self.ventana.iconbitmap("./iconos/ico.png")
        self.ventana.geometry("1000x600+400+100")
        self.ventana.config(bg="#FFE5EC") # Fondo Rosado Pastel (Igual al Login)
        #self.objeto = DatabaseManager("./BaseDatos/sistema.db")
        self.ventana.resizable(False, False)
        self.ventana.protocol("WM_DELETE_WINDOW", self.confirmar_salida)
        self.ventana.wm_attributes("-alpha", 0.95) # Opacidad idéntica al Login
    
        # Menú vertical (Estilo integrado a los tonos pasteles)
        self.menu_vertical = tk.Frame(self.ventana, bg="#FFE5EC", width=220)
        self.menu_vertical.pack(side="left", fill="y", padx=10, pady=10)
    
        # logo institucional (Reducido automáticamente para que encaje delicadamente)
        try:
            img_original = tk.PhotoImage(file="./imagenes/ai.png")
            self.logo = img_original.subsample(4, 4) # Reducción estática de tamaño
            label_img = tk.Label(self.menu_vertical, image=self.logo, bg="#FFE5EC")
            label_img.pack(pady=15)
        except:
            pass  # si no encuentra imagen no rompe
    
        # Frame para las interfaces (Fondo blanco limpio para trabajar las herramientas)
        self.contenido = tk.Frame(self.ventana, bg="#ffffff", bd=1, relief="solid")
        self.contenido.pack(side="right", fill="both", expand=True, padx=(0, 15), pady=15)
    
        #creacion de objetos
        #self.usuario = UsuarioView(self.contenido, self.objeto, ventana=self.ventana)
        #self.sumita = SumaView(self.contenido, self.objeto)
        #self.triangulito = TrianguloView(self.contenido, self.objeto)
            
        btn_inicio = tk.Button(self.menu_vertical, text="🏠 Inicio", command=self.mostrar_inicio, width=22)
        btn_inicio.pack(pady=8)
        btn_inicio.config(bg="#D4AF37", fg="#ffffff", font=("Arial", 11, "bold"), bd=0, cursor="hand2",
                          activebackground="#C59B27", activeforeground="white")
        
        btn_registro = tk.Button(self.menu_vertical, text="👤 Registro de Usuarios", command="", width=22) #self.usuario.mostrar
        btn_registro.pack(pady=8)
        btn_registro.config(bg="#D4AF37", fg="#ffffff", font=("Arial", 11, "bold"), bd=0, cursor="hand2",
                            activebackground="#C59B27", activeforeground="white")
    
        btn_suma = tk.Button(self.menu_vertical, text="➕ Sumar Dos Números", command="", width=22)#self.sumita.mostrar
        btn_suma.pack(pady=8)
        btn_suma.config(bg="#D4AF37", fg="#ffffff", font=("Arial", 11, "bold"), bd=0, cursor="hand2",
                        activebackground="#C59B27", activeforeground="white")
    
        btn_triangulo = tk.Button(self.menu_vertical, text="🔺 Triángulo", command="", width=22) #self.triangulito.mostrar
        btn_triangulo.pack(pady=8)
        btn_triangulo.config(bg="#D4AF37", fg="#ffffff", font=("Arial", 11, "bold"), bd=0, cursor="hand2",
                            activebackground="#C59B27", activeforeground="white")
    
        # Botón Salir usando el color Rosa Viejo/Cálido del botón X del login
        btn_salir = tk.Button(self.menu_vertical, text="🛑 Salir", command=self.confirmar_salida, width=22)
        btn_salir.pack(side="bottom", pady=20) # Posicionado abajo en el menú de manera fija
        btn_salir.config(bg="#E0A96D", fg="#ffffff", font=("Arial", 11, "bold"), bd=0, cursor="hand2",
                        activebackground="#CE965A", activeforeground="white")
    
        self.mostrar_inicio()
    
        self.ventana.mainloop()
    
    def mostrar_inicio(self):
        # Limpiar contenido
        for widget in self.contenido.winfo_children():
            widget.destroy()
    
        # Fondo blanco del panel principal
        self.contenido.config(bg="#ffffff")
    
        # Frame centrado
        frame_central = tk.Frame(self.contenido, bg="#ffffff")
        frame_central.place(relx=0.5, rely=0.5, anchor="center")
    
        # Imagen de inicio reducida
        try:
            img_inicio_orig = tk.PhotoImage(file="./imagenes/ai.png")
            self.img_inicio = img_inicio_orig.subsample(3, 3)
            label_img = tk.Label(frame_central, image=self.img_inicio, bg="#ffffff")
            label_img.pack(pady=15)
        except:
            pass
    
        # Título principal 
        titulo = tk.Label(
            frame_central,
            text="Bienvenido al Sistema Principal",
            font=("Arial", 22, "bold"),
            bg="#ffffff",
            fg="#4A3E3D"
        )
        titulo.pack(pady=5)
    
        # Subtítulo
        subtitulo = tk.Label(
            frame_central,
            text="Sistema de Gestión Académica",
            font=("Arial", 13, "bold"),
            bg="#ffffff",
            fg="#D4AF37"
        )
        subtitulo.pack(pady=5)
    
        # Línea decorativa elegante en tono dorado
        linea = tk.Frame(frame_central, bg="#D4AF37", height=2, width=350)
        linea.pack(pady=15)
    
    def confirmar_salida(self):
        respuesta = messagebox.askyesno(
            "Confirmar salida",
            "¿Estás seguro de salir del sistema?"
        )
    
        if respuesta:  #Si presiona "Sí"
            self.ventana.destroy()
