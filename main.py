#  GUI
import tkinter
from tkinter import ttk
from tkinter import messagebox


#Funcioón botón
def calcular():
    #Recuperar información del formulario
    a1 = a1_entry.get()
    a2 = a2_entry.get()
    a3 = a3_entry.get()
    b1 = b1_entry.get()
    b2 = b2_entry.get()
    b3 = b3_entry.get()
    z1 = z1_entry.get()
    z2 = z2_entry.get()
    mode = title_combobox.get()

    if a1 and a2 and a3 and b1 and b2 and b3 and z1 and z2 and mode:
        print(a1,a2,a3)

    else:
        tkinter.messagebox.showwarning(title="Error", message="Faltan datos")



window = tkinter.Tk()
window.title("Método simplex")

frame = tkinter.Frame(window)
frame.pack()


# Almacenamiento de variables
requisitos_frame = tkinter.LabelFrame(frame, text="Almacenamiento de Variables")
requisitos_frame.grid(row = 0,column = 0, padx=20, pady=10)

a1_label = tkinter.Label(requisitos_frame, text="Valor primer variable")
a1_label.grid(row=0,column=0)
a1_entry = tkinter.Entry(requisitos_frame)
a1_entry.grid(row=1,column=0)

a2_label = tkinter.Label(requisitos_frame, text="Valor primer variable")
a2_label.grid(row=0,column=1)
a2_entry = tkinter.Entry(requisitos_frame)
a2_entry.grid(row=1,column=1)

a3_label = tkinter.Label(requisitos_frame, text="Valor primer variable")
a3_label.grid(row=0,column=2)
a3_entry = tkinter.Entry(requisitos_frame)
a3_entry.grid(row=1,column=2)


b1_label = tkinter.Label(requisitos_frame, text="Valor segunda variable")
b1_label.grid(row=2,column=0)
b1_entry = tkinter.Entry(requisitos_frame)
b1_entry.grid(row=3,column=0)

b2_label = tkinter.Label(requisitos_frame, text="Valor segunda variable")
b2_label.grid(row=2,column=1)
b2_entry = tkinter.Entry(requisitos_frame)
b2_entry.grid(row=3,column=1)

b3_label = tkinter.Label(requisitos_frame, text="Valor segunda variable")
b3_label.grid(row=2,column=2)
b3_entry = tkinter.Entry(requisitos_frame)
b3_entry.grid(row=3,column=2)

for widget in requisitos_frame.winfo_children():
    widget.grid_configure(padx=10, pady=5)

#Almacenar restricciones
restricciones_frame = tkinter.LabelFrame(frame, text="Restricciones")
restricciones_frame.grid(row=1, column=0, sticky="news", padx=20,pady=10)

r1_label = tkinter.Label(restricciones_frame, text="Valor restriccion")
r1_label.grid(row=0,column=0)
r1_entry = tkinter.Entry(restricciones_frame)
r1_entry.grid(row=1,column=0)

r2_label = tkinter.Label(restricciones_frame, text="Valor restriccion")
r2_label.grid(row=0,column=1)
r2_entry = tkinter.Entry(restricciones_frame)
r2_entry.grid(row=1,column=1)

r3_label = tkinter.Label(restricciones_frame, text="Valor restriccion")
r3_label.grid(row=0,column=2)
r3_entry = tkinter.Entry(restricciones_frame)
r3_entry.grid(row=1,column=2)

for widget in restricciones_frame.winfo_children():
    widget.grid_configure(padx=10, pady=5)

#Ecuación objetivo
ecuacion_frame = tkinter.LabelFrame(frame, text="Ecuación objetivo")
ecuacion_frame.grid(row=2, column=0, sticky="news", padx=20,pady=10)

z1_label = tkinter.Label(ecuacion_frame, text="Variable objetivo")
z1_label.grid(row=0,column=0)
z1_entry = tkinter.Entry(ecuacion_frame)
z1_entry.grid(row=1,column=0)

z2_label = tkinter.Label(ecuacion_frame, text="Variable objetivo")
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