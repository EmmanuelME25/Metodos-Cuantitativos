#  GUI
import tkinter
import numpy as np
import matplotlib.pyplot as plt
from tkinter import ttk
from tkinter import messagebox

solucionesx=[]
solucionesy=[]
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
        f = np.array([r1, r2])

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
        soluciones.sort()


        if mode == "Minimizar":
            res=[]

            a=[]
            a.append(solucionesx[2])
            a.append(solucionesy[2])
            a.append(soluciones[2])
            a.append(soluciones[1])

            for i in range(len(a)):
                x, y = a[i]
                res.append(f1 * x + f2 * y)
            minimo = min(res)
            indice_min = res.index(minimo)
            x_min, y_min = a[indice_min]
            print("Valor mínimo:", minimo)
            print("Coordenadas asociadas:", x_min, y_min)

        if mode =="Maximizar":
            res = []

            a = []
            a1=[]
            a.append(solucionesx[0])
            a.append(solucionesy[0])

            a1.append(soluciones)

            for i in range(len(a1)):



            for i in range(len(a)):
                x, y = a[i]
                res.append(f1 * x + f2 * y)
            maximo = max(res)
            indice_max = res.index(maximo)
            x_max, y_max = a[indice_max]
            print("Valor maximo:", maximo)
            print("Coordenadas asociadas:", x_max, y_max)

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