# -*- coding: utf-8 -*-
"""
Created on Sat Apr 29 20:39:38 2023

@author: Montoya32
"""

#  GUI
import tkinter
from tkinter import ttk
from tkinter import messagebox
import matplotlib.pyplot as plt

# Definir variables globales
x1 = None
x2 = None
x3 = None
y1 = None
y2 = None
y3 = None

def dibujar_linea():
    global x1, x2, x3, y1, y2, y3
    # Puntos
    x = (x1,0)
    y = (0,y1)
    plt.plot(x, y, 'red',label='Restriccion 1')
    xx = (x2,0)
    yy = (0,y2)
    plt.plot(xx, yy, 'blue', label='Restriccion 2')
    xc = (x3,0)
    yc = (0,y3)
    plt.plot(xc, yc, 'purple', label='Restriccion 3')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title('Metodo Grafico')
    plt.grid(True)
    plt.legend(loc='upper right')
    plt.show()

#Funcioón botón
def calcular():
    global x1, x2, x3, y1, y2, y3
    #Recuperar información del formulario
    a1 = a1_entry.get()
    a2 = a2_entry.get()
    a3 = a3_entry.get()
    b1 = b1_entry.get()
    b2 = b2_entry.get()
    b3 = b3_entry.get()
    c1 = c1_entry.get()
    c2 = c2_entry.get()
    c3 = c3_entry.get()
    

    if a1 and a2 and a3 and b1 and b2 and b3 and c1 and c2 and c3:
        #Logica Matematica
        x1 = int(a3)/int(a1)
        x2 = int(b3)/int(b1)
        x3 = int(c3)/int(c1)
        y1 = int(a3)/int(a2)
        y2 = int(b3)/int(b2)
        y3 = int(c3)/int(c2)
        print(a1,a2,a3,x1,x2,x3,y1,y2,y3)
        
        x1_label.config(text=f"Restriccion 1: ({x1},0)")
        x2_label.config(text=f"Restriccion 2: ({x2},0)")
        x3_label.config(text=f"Restriccion 3: ({x3},0)")
        y1_label.config(text=f"(0,{y1})")
        y2_label.config(text=f"(0,{y2})")
        y3_label.config(text=f"(0,{y3})")
        
        # Dibujar línea
        dibujar_linea()
    else:
        tkinter.messagebox.showwarning(title="Error", message="Faltan datos")





window = tkinter.Tk()
window.title("Método GRAFICO")

frame = tkinter.Frame(window)
frame.pack()


# Almacenamiento de variables
requisitos_frame = tkinter.LabelFrame(frame, text="Almacenamiento de Restricciones")
requisitos_frame.grid(row = 0,column = 0, padx=20, pady=10)
#Primera Restriccion
a1_label = tkinter.Label(requisitos_frame, text="Valor de X1")
a1_label.grid(row=0,column=0)
a1_entry = tkinter.Entry(requisitos_frame)
a1_entry.grid(row=1,column=0)

a2_label = tkinter.Label(requisitos_frame, text="Valor de X2")
a2_label.grid(row=0,column=1)   
a2_entry = tkinter.Entry(requisitos_frame)
a2_entry.grid(row=1,column=1)

a3_label = tkinter.Label(requisitos_frame, text="Valor de C")
a3_label.grid(row=0,column=2)
a3_entry = tkinter.Entry(requisitos_frame)
a3_entry.grid(row=1,column=2)

#Segunda Restriccion
b1_label = tkinter.Label(requisitos_frame, text="Valor de X1")
b1_label.grid(row=2,column=0)
b1_entry = tkinter.Entry(requisitos_frame)
b1_entry.grid(row=3,column=0)

b2_label = tkinter.Label(requisitos_frame, text="Valor de X2")
b2_label.grid(row=2,column=1)
b2_entry = tkinter.Entry(requisitos_frame)
b2_entry.grid(row=3,column=1)

b3_label = tkinter.Label(requisitos_frame, text="Valor de C")
b3_label.grid(row=2,column=2)
b3_entry = tkinter.Entry(requisitos_frame)
b3_entry.grid(row=3,column=2)
#Cuarta Restriccion
c1_label = tkinter.Label(requisitos_frame, text="Valor de X1")
c1_label.grid(row=4,column=0)
c1_entry = tkinter.Entry(requisitos_frame)
c1_entry.grid(row=5,column=0)

c2_label = tkinter.Label(requisitos_frame, text="Valor de X2")
c2_label.grid(row=4,column=1)
c2_entry = tkinter.Entry(requisitos_frame)
c2_entry.grid(row=5,column=1)

c3_label = tkinter.Label(requisitos_frame, text="Valor de C")
c3_label.grid(row=4,column=2)
c3_entry = tkinter.Entry(requisitos_frame)
c3_entry.grid(row=5,column=2)

for widget in requisitos_frame.winfo_children():
    widget.grid_configure(padx=10, pady=5)

#Almacenar restricciones
restricciones_frame = tkinter.LabelFrame(frame, text="Funcion Z")
restricciones_frame.grid(row=1, column=0, sticky="news", padx=20,pady=10)

r1_label = tkinter.Label(restricciones_frame, text="Valor X1")
r1_label.grid(row=0,column=0)
r1_entry = tkinter.Entry(restricciones_frame)
r1_entry.grid(row=1,column=0)

r2_label = tkinter.Label(restricciones_frame, text="Valor X2")
r2_label.grid(row=0,column=1)
r2_entry = tkinter.Entry(restricciones_frame)
r2_entry.grid(row=1,column=1)

#Button
button = tkinter.Button(frame, text="Agregar Campo")
button.grid(row=1,column=1,sticky="news")

for widget in restricciones_frame.winfo_children():
    widget.grid_configure(padx=10, pady=5)

#Button
button = tkinter.Button(frame, text="Calcular", command=calcular)
button.grid(row=3,column=0,sticky="news",padx=20,pady=10)


#Resultados Obtenidos al despejar Restricciones
resultados_frame = tkinter.LabelFrame(frame, text="Resultados")
resultados_frame.grid(row=4, column=0, sticky="news", padx=20, pady=10)

x1_label = tkinter.Label(resultados_frame, text=f"Restriccion 1: ({x1},0)")
x1_label.grid(row=0, column=0)

x2_label = tkinter.Label(resultados_frame, text=f"Restriccion 2: ({x2},0)")
x2_label.grid(row=1, column=0)

x3_label = tkinter.Label(resultados_frame, text=f"Restriccion 3: ({x3},0)")
x3_label.grid(row=2, column=0)

y1_label = tkinter.Label(resultados_frame, text=f"(0,{y1})")
y1_label.grid(row=0, column=1)

y2_label = tkinter.Label(resultados_frame, text=f"(0,{y2})")
y2_label.grid(row=1, column=1)

y3_label = tkinter.Label(resultados_frame, text=f"(0,{y3})")
y3_label.grid(row=2, column=1)


window.mainloop()