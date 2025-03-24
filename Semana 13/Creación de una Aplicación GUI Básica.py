import tkinter as tk
from tkinter import ttk  # creación Para la tabla (ttk.Treeview)

class GestorDatos:
    def __init__(self, ventana):
        self.ventana = ventana
        ventana.title("Gestor de Datos")
        self.ventana.geometry("500x400")

        # Se etiqueta ventana y campo de texto
        self.etiqueta = tk.Label(ventana, text="Ingrese datos:")
        self.etiqueta.pack()
        self.entrada_datos = tk.Entry(ventana)
        self.entrada_datos.pack()

        # Se inserta botón Agregar
        self.boton_agregar = tk.Button(ventana, text="Agregar", command=self.agregar_dato)
        self.boton_agregar.pack()

        # Tabla para mostrar datos
        self.tabla_datos = ttk.Treeview(ventana, columns=("Datos",), show="headings")
        self.tabla_datos.heading("Datos", text="Datos Ingresados")
        self.tabla_datos.pack()

        # Se agrega botón Limpiar
        self.boton_limpiar = tk.Button(ventana, text="Limpiar", command=self.limpiar_datos)
        self.boton_limpiar.pack()

    def agregar_dato(self):
        dato = self.entrada_datos.get()
        if dato:
            self.tabla_datos.insert("", tk.END, values=(dato,))
            self.entrada_datos.delete(0, tk.END)  # Limpia el campo de texto

    def limpiar_datos(self):
        self.tabla_datos.delete(*self.tabla_datos.get_children())  # Limpia la tabla

# Crear la ventana principal
ventana = tk.Tk()
app = GestorDatos(ventana)
ventana.mainloop()
