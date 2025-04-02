import tkinter as tk
from tkinter import messagebox
from tkcalendar import DateEntry

class AgendaApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Agenda Personal")
        self.root.geometry("650x400")

        self.root.configure(bg='lightblue')

        self.frame_lista = tk.Frame(self.root) # Usamos tk.Frame
        self.frame_lista.pack(pady=10)

        self.tree = tk.ttk.Treeview(self.frame_lista, columns=("Fecha", "Hora", "Descripción"), show="headings")
        self.tree.heading("Fecha", text="Fecha")
        self.tree.heading("Hora", text="Hora")
        self.tree.heading("Descripción", text="Descripción")
        self.tree.pack()

        self.frame_entrada = tk.Frame(self.root) # Usamos tk.Frame
        self.frame_entrada.pack(pady=10)

        tk.Label(self.frame_entrada, text="Fecha:").grid(row=0, column=0)
        self.fecha_entry = DateEntry(self.frame_entrada, date_pattern='yyyy-mm-dd')
        self.fecha_entry.grid(row=0, column=1)

        tk.Label(self.frame_entrada, text="Hora:").grid(row=1, column=0)
        self.hora_entry = tk.Entry(self.frame_entrada)
        self.hora_entry.grid(row=1, column=1)

        tk.Label(self.frame_entrada, text="Descripción:").grid(row=2, column=0)
        self.descripcion_entry = tk.Entry(self.frame_entrada)
        self.descripcion_entry.grid(row=2, column=1)

        self.frame_botones = tk.Frame(self.root) # Usamos tk.Frame
        self.frame_botones.pack(pady=10)

        tk.Button(self.frame_botones, text="Agregar Evento", command=self.agregar_evento, background='green').grid(row=0, column=0, padx=5)
        tk.Button(self.frame_botones, text="Eliminar Evento", command=self.eliminar_evento, background='red').grid(row=0, column=1, padx=5)
        tk.Button(self.frame_botones, text="Salir", command=self.root.quit, background='gray').grid(row=0, column=2, padx=5)

    def agregar_evento(self):
        fecha = self.fecha_entry.get()
        hora = self.hora_entry.get()
        descripcion = self.descripcion_entry.get()

        if fecha and hora and descripcion:
            self.tree.insert("", "end", values=(fecha, hora, descripcion))
            self.hora_entry.delete(0, tk.END)
            self.descripcion_entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Advertencia", "Todas las casillas son obligatorias")

    def eliminar_evento(self):
        seleccionado = self.tree.selection()
        if seleccionado:
            confirmar = messagebox.askyesno("Eliminar", "¿Seguro que deseas eliminar el evento?")
            if confirmar:
                self.tree.delete(seleccionado)
        else:
            messagebox.showwarning("Advertencia", "Seleccionar evento para eliminar")

if __name__ == "__main__":
    root = tk.Tk()
    app = AgendaApp(root)
    root.mainloop()