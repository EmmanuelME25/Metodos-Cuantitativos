import tkinter as tk
from tkinter import ttk, messagebox
import matplotlib.pyplot as plt

class MetodoGraficoApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Método GRAFICO")

        self.create_widgets()

    def create_widgets(self):
        # Frame para la entrada de datos
        requisitos_frame = ttk.LabelFrame(self.master, text="Almacenamiento de Restricciones")
        requisitos_frame.pack(padx=20, pady=10)

        # Etiquetas y campos de entrada para cada restricción
        self.restricciones = []
        for i in range(3):
            restriccion_frame = ttk.Frame(requisitos_frame)
            restriccion_frame.pack(pady=5)

            x1_label = ttk.Label(restriccion_frame, text="Valor de X1:")
            x1_label.pack(side=tk.LEFT)
            x1_entry = ttk.Entry(restriccion_frame)
            x1_entry.pack(side=tk.LEFT, padx=5)
            x2_label = ttk.Label(restriccion_frame, text="Valor de X2:")
            x2_label.pack(side=tk.LEFT)
            x2_entry = ttk.Entry(restriccion_frame)
            x2_entry.pack(side=tk.LEFT, padx=5)
            c_label = ttk.Label(restriccion_frame, text="Valor de C:")
            c_label.pack(side=tk.LEFT)
            c_entry = ttk.Entry(restriccion_frame)
            c_entry.pack(side=tk.LEFT, padx=5)

            self.restricciones.append((x1_entry, x2_entry, c_entry))

        # Botones para calcular y borrar los datos
        botones_frame = ttk.Frame(self.master)
        botones_frame.pack(pady=10)

        ttk.Button(botones_frame, text="Calcular", command=self.calcular).pack(side=tk.LEFT, padx=5)
        ttk.Button(botones_frame, text="Borrar", command=self.borrar_datos).pack(side=tk.LEFT)

        # Labels para mostrar los resultados y el gráfico
        self.x1_label = ttk.Label(self.master, text="")
        self.x1_label.pack()
        self.x2_label = ttk.Label(self.master, text="")
        self.x2_label.pack()
        self.x3_label = ttk.Label(self.master, text="")
        self.x3_label.pack()
        self.y1_label = ttk.Label(self.master, text="")
        self.y1_label.pack()
        self.y2_label = ttk.Label(self.master, text="")
        self.y2_label.pack()
        self.y3_label = ttk.Label(self.master, text="")
        self.y3_label.pack()

        self.fig, self.ax = plt.subplots()
        self.ax.set_xlabel('x')