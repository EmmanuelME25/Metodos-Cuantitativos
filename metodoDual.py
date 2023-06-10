#  GUI
import tkinter
import numpy as np
import matplotlib.pyplot as plt
from tkinter import ttk
from tkinter import messagebox
import tkinter as tk

solucionesx = []
solucionesy = []
soluciones = []

x1 = None
x2 = None
x3 = None
y1 = None
y2 = None
y3 = None
c1 = None
c2 = None
c3 = None
# Funcioón botón


def set_window_responsive(root):
    root.grid_rowconfigure(0, weight=1)  # Fila principal expandible
    root.grid_columnconfigure(0, weight=1)  # Columna principal expandible

    frame.grid_rowconfigure(0, weight=1)  # Filas internas expandibles
    frame.grid_rowconfigure(1, weight=1)
    frame.grid_rowconfigure(2, weight=1)
    frame.grid_rowconfigure(3, weight=1)
    frame.grid_rowconfigure(4, weight=1)
    frame.grid_columnconfigure(0, weight=1)  # Columna interna expandible

    # Ajustar el tamaño de la letra de los widgets
    style = ttk.Style()
    # Cambiar "Arial" y 12 según tus preferencias
    style.configure(".", font=("Arial", 12))


def calcular():
    global x1, x2, x3, y1, y2, y3, c1, c2, c3, soluciones
    # Recuperar información del formulario
    a1 = a1_entry.get()
    a2 = a2_entry.get()
    a3 = a3_entry.get()
    b1 = b1_entry.get()
    b2 = b2_entry.get()
    b3 = b3_entry.get()
    t1 = c1_entry.get()
    t2 = c2_entry.get()
    t3 = c3_entry.get()
    r1 = r1_entry.get()
    r2 = r2_entry.get()
    mode = title_combobox.get()

    if a1 and a2 and a3 and b1 and b2 and b3 and t1 and t2 and t3 and r1 and r2 and mode:
        x1 = float(a1)
        x2 = float(b1)
        x3 = float(t1)
        y1 = float(a2)
        y2 = float(b2)
        y3 = float(t2)
        c1 = float(a3)
        c2 = float(b3)
        c3 = float(t3)
        r1 = float(r1)
        r2 = float(r2)

        A = np.array([[x1, y1], [x2, y2], [x3, y3]])
        b = np.array([c1, c2, c3])
        f = np.array([r1, r2])

        recx1 = int(a3) / int(a1)
        recx2 = int(b3) / int(b1)
        recx3 = int(t3) / int(t1)
        recy1 = int(a3) / int(a2)
        recy2 = int(b3) / int(b2)
        recy3 = int(t3) / int(t2)

        x1_label.config(text=f"Restriccion 1: ({recx1},0)")
        x2_label.config(text=f"Restriccion 2: ({recx2},0)")
        x3_label.config(text=f"Restriccion 3: ({recx3},0)")
        y1_label.config(text=f"(0,{recy1})")
        y2_label.config(text=f"(0,{recy2})")
        y3_label.config(text=f"(0,{recy3})")

        solucionesx.append([c1 / x1, 0])
        solucionesy.append([0, c1 / y1])
        solucionesx.append([c2 / x2, 0])
        solucionesy.append([0, c2 / y2])
        solucionesx.append([c3 / x3, 0])
        solucionesy.append([0, c3 / y3])
        x = np.linalg.solve([[x1, y1], [x2, y2]], [c1, c2])
        x1 = np.linalg.solve([[x1, y1], [x3, y3]], [c1, c3])
        x2 = np.linalg.solve([[x3, y3], [x2, y2]], [c3, c2])

        xs = x.tolist()
        soluciones.append(xs)
        xs = x1.tolist()
        soluciones.append(xs)
        xs = x2.tolist()
        soluciones.append(xs)
        solucionesx.sort()
        solucionesy.sort()
        solucionesx.sort()

        if mode == "Maximizar":
            res = []
            a = []
            a1 = []

            a.append(solucionesx[2])
            a.append(solucionesy[2])
            a.append(soluciones[0])
            a.append(soluciones[1])
            a.append(soluciones[2])

            for i in range(len(a)):
                x, y = a[i]
                res.append(r1 * x + r2 * y)

            res.sort()
            minimo = res[1]

            for i in range(len(a)):
                x, y = a[i]
                if (r1 * x + r2 * y) == res[1]:
                    x_min, y_min = x, y

            print("Resultado:", minimo)
            print("Coordenadas:", x_min, ",", y_min)
            x4_label.config(text=f"Tras el analisis de datos se obtiene que en el punto "
                                 f"({x_min},{y_min}), se obtiene un valor minimo de {minimo}")

        if mode == "Minimizar":
            res = []
            a = []
            a1 = []

            a.append(solucionesx[0])
            a.append(solucionesy[0])
            a.append(soluciones[0])
            a.append(soluciones[1])
            a.append(soluciones[2])

            for i in range(len(a)):
                x, y = a[i]
                res.append(r1 * x + r2 * y)

            res.sort()
            maximo = res[3]

            for i in range(len(a)):
                x, y = a[i]
                if (r1 * x + r2 * y) == res[3]:
                    x_max, y_max = x, y

            print("Resultado:", maximo)
            print("Coordenadas:", x_max, ",", y_max)
            x5_label.config(text=f"Tras el analisis de datos se obtiene que en el punto "
                                 f"({x_max},{y_max}), se obtiene un valor maximo de {maximo}")
            fig = plt.figure()
            fig.clf()
            ax = fig.subplots(1, 1)

            ax.plot(recx1, recy1, label='Primera Restriccion')
            ax.plot(recx2, recy2, label='Segunda Restriccion')
            ax.plot(recx3, recy3, label='Tercera Restriccion')
            ax.scatter(x, y)
            ax.set_xlabel('x')
            ax.set_ylabel('y')

            ax.legend()
            fig.tight_layout()

            plt.plot([recx1, 0], [0, recy1], color='blue',
                     linewidth=1, linestyle="-")
            plt.plot([recx2, 0], [0, recy2], color='orange',
                     linewidth=1, linestyle="-")
            plt.plot([recx3, 0], [0, recy3], color='green',
                     linewidth=1, linestyle="-")

            plt.grid()
            plt.show()

    else:
        tkinter.messagebox.showwarning(title="Error", message="Faltan datos")


def reset_variables():
    global solucionesx, solucionesy, soluciones, x1, x2, x3, y1, y2, y3, c1, c2, c3
    solucionesx = []
    solucionesy = []
    soluciones = []

    x1 = None
    x2 = None
    x3 = None
    y1 = None
    y2 = None
    y3 = None
    c1 = None
    c2 = None
    c3 = None

    # Restablecer los valores en los widgets de entrada
    a1_entry.delete(0, "end")
    a2_entry.delete(0, "end")
    a3_entry.delete(0, "end")
    b1_entry.delete(0, "end")
    b2_entry.delete(0, "end")
    b3_entry.delete(0, "end")
    c1_entry.delete(0, "end")
    c2_entry.delete(0, "end")
    c3_entry.delete(0, "end")
    r1_entry.delete(0, "end")
    r2_entry.delete(0, "end")
    title_combobox.set("")


window = tk.Tk()
window.title("Método GRAFICO")

frame = tk.Frame(window)
frame.grid(row=0, column=0, sticky="nsew")
set_window_responsive(window)


# Almacenamiento de variables
requisitos_frame = tkinter.LabelFrame(
    frame, text="Almacenamiento de Restricciones")
requisitos_frame.grid(row=0, column=0, padx=20, pady=10)
# Primera Restriccion
a1_label = tkinter.Label(requisitos_frame, text="Valor de X1")
a1_label.grid(row=0, column=0)
a1_entry = tkinter.Entry(requisitos_frame)
a1_entry.grid(row=1, column=0)

b1_label = tkinter.Label(requisitos_frame, text="Valor de X1")
b1_label.grid(row=0, column=1)
b1_entry = tkinter.Entry(requisitos_frame)
b1_entry.grid(row=1, column=1)

c1_label = tkinter.Label(requisitos_frame, text="Valor de X1")
c1_label.grid(row=0, column=2)
c1_entry = tkinter.Entry(requisitos_frame)
c1_entry.grid(row=1, column=2)

r1_label = tkinter.Label(requisitos_frame, text="Valor X1")
r1_label.grid(row=0, column=3)
r1_entry = tkinter.Entry(requisitos_frame)
r1_entry.grid(row=1, column=3)

# Segunda Restriccion
a2_label = tkinter.Label(requisitos_frame, text="Valor de X2")
a2_label.grid(row=2, column=0)
a2_entry = tkinter.Entry(requisitos_frame)
a2_entry.grid(row=3, column=0)

b2_label = tkinter.Label(requisitos_frame, text="Valor de X2")
b2_label.grid(row=2, column=1)
b2_entry = tkinter.Entry(requisitos_frame)
b2_entry.grid(row=3, column=1)

c2_label = tkinter.Label(requisitos_frame, text="Valor de X2")
c2_label.grid(row=2, column=2)
c2_entry = tkinter.Entry(requisitos_frame)
c2_entry.grid(row=3, column=2)

r2_label = tkinter.Label(requisitos_frame, text="Valor X2")
r2_label.grid(row=2, column=3)
r2_entry = tkinter.Entry(requisitos_frame)
r2_entry.grid(row=3, column=3)


for widget in requisitos_frame.winfo_children():
    widget.grid_configure(padx=10, pady=5)

# Almacenar restricciones
# Ecuación objetivo
ecuacion_frame = tkinter.LabelFrame(frame, text="Ecuación objetivo")
ecuacion_frame.grid(row=2, column=0, sticky="news", padx=20, pady=10)

# fUNCION z
a3_label = tkinter.Label(ecuacion_frame, text="Valor de C")
a3_label.grid(row=0, column=0)
a3_entry = tkinter.Entry(ecuacion_frame)
a3_entry.grid(row=1, column=0)

b3_label = tkinter.Label(ecuacion_frame, text="Valor de C")
b3_label.grid(row=0, column=1)
b3_entry = tkinter.Entry(ecuacion_frame)
b3_entry.grid(row=1, column=1)

c3_label = tkinter.Label(ecuacion_frame, text="Valor de C")
c3_label.grid(row=0, column=2)
c3_entry = tkinter.Entry(ecuacion_frame)
c3_entry.grid(row=1, column=2)

mm_label = tkinter.Label(ecuacion_frame, text="Modo")
title_combobox = ttk.Combobox(ecuacion_frame, values=[
                              "Minimizar", "Maximizar"])
mm_label.grid(row=0, column=3)
title_combobox.grid(row=1, column=3)

for widget in ecuacion_frame.winfo_children():
    widget.grid_configure(padx=10, pady=5)

button_frame = tkinter.Frame(frame)
button_frame.grid(row=3, column=0, columnspan=2)

button = tkinter.Button(button_frame, text="Calcular", command=calcular)
button.pack(side="left", padx=10, pady=10)  # Centrar horizontalmente

button = tkinter.Button(button_frame, text="RESET", command=reset_variables)
button.pack(side="left", padx=10, pady=10)  # Centrar horizontalmente

for widget in ecuacion_frame.winfo_children():
    widget.grid_configure(padx=10, pady=5)

# Resultados Obtenidos al despejar Restricciones
resultados_frame = tkinter.LabelFrame(frame, text="Resultados")
resultados_frame.grid(row=4, column=0, sticky="news", padx=20, pady=10)

x1_label = tkinter.Label(resultados_frame, text=f"Restriccion 1: ({x1},0)")
x1_label.grid(row=0, column=0)

x2_label = tkinter.Label(resultados_frame, text=f"Restriccion 2: ({x2},0)")
x2_label.grid(row=1, column=0)

x3_label = tkinter.Label(resultados_frame, text=f"Restriccion 3: ({x3},0)")
x3_label.grid(row=2, column=0)

x4_label = tkinter.Label(resultados_frame, text=f"Minimo: ")
x4_label.grid(row=3, column=0)

x5_label = tkinter.Label(resultados_frame, text=f"Maximo: ")
x5_label.grid(row=4, column=0)

y1_label = tkinter.Label(resultados_frame, text=f"(0,{y1})")
y1_label.grid(row=0, column=1)

y2_label = tkinter.Label(resultados_frame, text=f"(0,{y2})")
y2_label.grid(row=1, column=1)

y3_label = tkinter.Label(resultados_frame, text=f"(0,{y3})")
y3_label.grid(row=2, column=1)

window.mainloop()