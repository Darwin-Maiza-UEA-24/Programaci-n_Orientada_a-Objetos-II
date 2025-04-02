                                # Aplicación GUI de Lista de Tareas
import tkinter as tk
from tkinter import ttk, messagebox

class ListaTareasApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Lista de Tareas")
        self.root.geometry("500x450")

        # Sección de entrada para las nuevas tareas
        self.tarea_entry = ttk.Entry(root, width=40)
        self.tarea_entry.pack(pady=10)

        # Para asignar los botones
        self.agregar_btn = ttk.Button(root, text="Ingresar Tarea", command=self.agregar_tarea)
        self.agregar_btn.pack()

        self.completar_btn = ttk.Button(root, text="Marcar tareas Realizadas", command=self.completar_tarea)
        self.completar_btn.pack()

        self.eliminar_btn = ttk.Button(root, text="Eliminar Tarea", command=self.eliminar_tarea)
        self.eliminar_btn.pack()

        # Lista de tareas (usando Treeview)
        self.tree = ttk.Treeview(root, columns=("Tarea", "Estado"), show="headings")
        self.tree.heading("Tarea", text="Tarea")
        self.tree.heading("Estado", text="Estado")
        self.tree.pack(pady=10)

        # Evento para añadir tarea con teclado (Enter)
        self.tarea_entry.bind("<Return>", lambda event: self.agregar_tarea())

    def agregar_tarea(self):
        tarea = self.tarea_entry.get()
        if tarea:
            self.tree.insert("", tk.END, values=(tarea, ""))
            self.tarea_entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Advertencia", "Introducir una tarea .")

    def completar_tarea(self):
        seleccionado = self.tree.selection()
        if seleccionado:
            item = seleccionado[0]
            tarea = self.tree.item(item, "values")[0]
            self.tree.item(item, values=(tarea, "REALIZADA"))
            self.tree.tag_configure("verde", foreground="green")
            self.tree.item(item, tags=("verde",))
        else:
            messagebox.showwarning("Advertencia", "Por favor, selecciona una tarea.")

    def eliminar_tarea(self):
        seleccionado = self.tree.selection()
        if seleccionado:
            self.tree.delete(seleccionado)
        else:
            messagebox.showwarning("Advertencia", "Selecciona una tarea primero.")

if __name__ == "__main__":
    root = tk.Tk()
    app = ListaTareasApp(root)
    root.mainloop()