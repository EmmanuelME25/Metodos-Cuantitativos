#  GUI
import tkinter
import numpy as np
import matplotlib.pyplot as plt
from tkinter import ttk
from tkinter import messagebox

soluciones=[]

x1 = None
x2 = None
x3 = None
y1 = None
y2 = None
y3 = None
c1 = None
c2 = None
c3 = None


#Funcioón botón
def calcular():
    global x1, x2, x3, y1, y2, y3, c1, c2, c3, soluciones
    #Recuperar información del formulario
    a1 = a1_entry.get()
    a2 = a2_entry.get()
    a3 = a3_entry.get()
    b1 = b1_entry.get()
    b2 = b2_entry.get()
    b3 = b3_entry.get()
    r1 = r1_entry.get()
    r2 = r2_entry.get()
    r3 = r3_entry.get()
    z1 = z1_entry.get()
    z2 = z2_entry.get()
    mode = title_combobox.get()

    if a1 and a2 and a3 and b1 and b2 and b3 and r1 and r2 and r3 and z1 and z2 and mode:
        x1=float(a1)
        x2=float(a2)
        x3=float(a3)
        y1=float(b1)
        y2=float(b2)
        y3=float(b3)
        c1=float(r1)
        c2=float(r2)
        c3=float(r3)
        f1=float(z1)
        f2=float(z2)

        A = np.array([[x1, y1], [x2, y2], [x3, y3]])
        b = np.array([c1, c2, c3])
        f = np.array([f1, f2])

        # Encontrar los vértices del polígono
        vertices = []
        for i in range(len(A)):
            for j in range(len(A)):
                if i != j:
                    sistema = np.array([A[i], A[j]])
                    sol = np.linalg.solve(sistema, b[[i, j]])
                    if (sol >= 0).all():
                        vertices.append(sol)
        vertices = np.array(vertices)

        # Encontrar las soluciones factibles
        soluciones = []
        for i in range(len(vertices)):
            v = vertices[i]
            if (A @ v <= b).all():
                soluciones.append(v)
        soluciones = np.array(soluciones)  # Convertir la lista a un arreglo de NumPy

        # Encontrar la solución óptima
        if mode == "Minimizar":
            valores = f @ soluciones.T
            idx_opt = np.argmin(valores)
            opt_val = valores[idx_opt]
            opt_sol = soluciones[idx_opt]

        elif mode == "Maximizar":
            valores = f @ soluciones.T
            idx_opt = np.argmax(valores)
            opt_val = valores[idx_opt]
            opt_sol = soluciones[idx_opt]

        # Graficar las soluciones y la solución óptima
        plt.figure(figsize=(8, 6))

        # Graficar las líneas de restricción
        for i in range(len(A)):
            x = np.linspace(0, b[i] / A[i, 1])
            y = (b[i] - A[i, 0] * x) / A[i, 1]
            plt.plot(x, y, label="Restricción {}".format(i + 1))

        # Graficar los puntos críticos
        plt.scatter(soluciones[:, 0], soluciones[:, 1], marker='o', color='r', label="Puntos críticos")

        # Graficar la solución óptima
        plt.scatter(opt_sol[0], opt_sol[1], marker='*', color='g', s=200, label="Solución óptima")
        plt.title("Metodo grafico")
        plt.xlabel("X")
        plt.ylabel("Y")
        plt.legend()
        plt.show()


    else:
        tkinter.messagebox.showwarning(title="Error", message="Faltan datos")



window = tkinter.Tk()
window.title("Método simplex")

frame = tkinter.Frame(window)
frame.pack()


# Almacenamiento de variables
requisitos_frame = tkinter.LabelFrame(frame, text="Almacenamiento de Variables")
requisitos_frame.grid(row = 0,column = 0, padx=20, pady=10)

a1_label = tkinter.Label(requisitos_frame, text="Valor X1")
a1_label.grid(row=0,column=0)
a1_entry = tkinter.Entry(requisitos_frame)
a1_entry.grid(row=1,column=0)

a2_label = tkinter.Label(requisitos_frame, text="Valor X1")
a2_label.grid(row=0,column=1)
a2_entry = tkinter.Entry(requisitos_frame)
a2_entry.grid(row=1,column=1)

a3_label = tkinter.Label(requisitos_frame, text="Valor X1")
a3_label.grid(row=0,column=2)
a3_entry = tkinter.Entry(requisitos_frame)
a3_entry.grid(row=1,column=2)


b1_label = tkinter.Label(requisitos_frame, text="Valor X2")
b1_label.grid(row=2,column=0)
b1_entry = tkinter.Entry(requisitos_frame)
b1_entry.grid(row=3,column=0)

b2_label = tkinter.Label(requisitos_frame, text="Valor X2")
b2_label.grid(row=2,column=1)
b2_entry = tkinter.Entry(requisitos_frame)
b2_entry.grid(row=3,column=1)

b3_label = tkinter.Label(requisitos_frame, text="Valor X2")
b3_label.grid(row=2,column=2)
b3_entry = tkinter.Entry(requisitos_frame)
b3_entry.grid(row=3,column=2)

for widget in requisitos_frame.winfo_children():
    widget.grid_configure(padx=10, pady=5)

#Almacenar restricciones
restricciones_frame = tkinter.LabelFrame(frame, text="Restricciones")
restricciones_frame.grid(row=1, column=0, sticky="news", padx=20,pady=10)

r1_label = tkinter.Label(restricciones_frame, text="C para ec. 1 ")
r1_label.grid(row=0,column=0)
r1_entry = tkinter.Entry(restricciones_frame)
r1_entry.grid(row=1,column=0)

r2_label = tkinter.Label(restricciones_frame, text="C para ec. 2")
r2_label.grid(row=0,column=1)
r2_entry = tkinter.Entry(restricciones_frame)
r2_entry.grid(row=1,column=1)

r3_label = tkinter.Label(restricciones_frame, text="C para ec. 3")
r3_label.grid(row=0,column=2)
r3_entry = tkinter.Entry(restricciones_frame)
r3_entry.grid(row=1,column=2)

for widget in restricciones_frame.winfo_children():
    widget.grid_configure(padx=10, pady=5)

#Ecuación objetivo
ecuacion_frame = tkinter.LabelFrame(frame, text="Ecuación objetivo")
ecuacion_frame.grid(row=2, column=0, sticky="news", padx=20,pady=10)

z1_label = tkinter.Label(ecuacion_frame, text="Valor X1")
z1_label.grid(row=0,column=0)
z1_entry = tkinter.Entry(ecuacion_frame)
z1_entry.grid(row=1,column=0)

z2_label = tkinter.Label(ecuacion_frame, text="Valor X2")
z2_label.grid(row=0,column=1)
z2_entry = tkinter.Entry(ecuacion_frame)
z2_entry.grid(row=1,column=1)

mm_label = tkinter.Label(ecuacion_frame, text="Modo")
title_combobox = ttk.Combobox(ecuacion_frame, values=["Minimizar", "Maximizar"])
mm_label.grid(row=0,column=2)
title_combobox.grid(row=1,column=2)

for widget in ecuacion_frame.winfo_children():
    widget.grid_configure(padx=10, pady=5)

#Button
button = tkinter.Button(frame, text="Calcular", command=calcular)
button.grid(row=3,column=0,sticky="news",padx=20,pady=10)



window.mainloop()