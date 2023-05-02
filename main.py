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

def plot_polygon(A, b):
    x = np.linspace(0, np.max(b), 1000)
    fig, ax = plt.subplots(figsize=(6, 6))
    for i in range(A.shape[0]):
        if A[i,1] == 0:
            ax.axvline(x=b[i]/A[i,0], lw=2, color='k', ls='--')
        elif A[i,0] == 0:
            ax.axhline(y=b[i]/A[i,1], lw=2, color='k', ls='--')
        else:
            y = (b[i]-A[i,0]*x)/A[i,1]
            ax.plot(x, y, lw=2, color='k', ls='--')
    ax.set_xlabel('x1', fontsize=14)
    ax.set_ylabel('x2', fontsize=14)
    ax.set_xlim(0, np.max(b))
    ax.set_ylim(0, np.max(b))
    ax.grid(True, lw=1, ls='--', alpha=0.5)
    plt.show()

    # Generate random constraints and critical points
    A = np.random.randint(low=1, high=5, size=(3,2))
    b = np.random.randint(low=10, high=20, size=3)
    f = np.random.randint(low=-5, high=5, size=2)
    mode = "Minimizar"

    # Apply the simplex algorithm
    n, m = A.shape
    b = b.reshape(n, 1)
    c = np.concatenate([f, np.zeros(n)])
    T = np.concatenate([np.concatenate([A, np.eye(n)], axis=1), np.concatenate([-c.reshape(1, n + m)], axis=0)], axis=0)
    idx = np.arange(n, n+m)
    res = []
    vertices = []
    while True:
        x = np.linalg.solve(T[:-1, idx], b)
        res.append(np.dot(f, x))
        if np.all(T[-1, :-1] >= 0):
            break
        j0 = np.argmin(T[-1, :-1]) if mode=="Minimizar" else np.argmax(T[-1, :-1])
        if np.all(T[:-1, j0] <= 0):
            break
        ratios = np.divide(T[:-1, -1], T[:-1, j0])
        ratios[ratios < 0] = np.inf
        j = np.argmin(ratios)
        T[j, :] = T[j, :] / T[j, j0]
        idx[j] = j0
        for i in range(n+1):
            if i != j:
                T[i, :] -= T[i, j0] * T[j, :]
        vertices.append(x[:-m].tolist())
    vertices = np.array(vertices)

    
    # Plot the constraints and critical points
    plot_polygon(A, b)
    plt.scatter(vertices[:,0], vertices[:,1], s=50, c='r')
    plt.xlabel('x1', fontsize=14)
    plt.ylabel('x2', fontsize=14)
    plt.title('Simplex Method with Three Constraints', fontsize=16)
    plt.show()
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
    t1 = c1_entry.get()
    t2 = c2_entry.get()
    t3 = c3_entry.get()
    r1 = r1_entry.get()
    r2 = r2_entry.get()
    mode = title_combobox.get()

    if a1 and a2 and a3 and b1 and b2 and b3 and t1 and t2 and t3 and r1 and r2 and mode:
        x1=float(a1)
        x2=float(b1)
        x3=float(t1)
        y1=float(a2)
        y2=float(b2)
        y3=float(t2)
        c1=float(a3)
        c2=float(b3)
        c3=float(t3)
        r1=float(r1)
        r2=float(r2)

        A = np.array([[x1, y1], [x2, y2], [x3, y3]])
        b = np.array([c1, c2, c3])
        f = np.array([r1, r2])

        recx1 = int(a3)/int(a1)
        recx2 = int(b3)/int(b1)
        recx3 = int(t3)/int(t1)
        recy1 = int(a3)/int(a2)
        recy2 = int(b3)/int(b2)
        recy3 = int(t3)/int(t2)
        
        
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

        print(solucionesy)
        print(solucionesx)
        print(soluciones)
        if mode == "Minimizar":
            res=[]
            x,y = solucionesx[2]
            res.append(r1*x+r2*y)
            x, y = solucionesy[2]
            res.append(r1 * x + r2 * y)
            x, y = soluciones[1]
            res.append(r1 * x + r2 * y)
            x, y = soluciones[2]
            res.append(r1 * x + r2 * y)
            minimo = min(res)
            print("Valor mínimo:", minimo)
            x4_label.config(text=f"Valor mínimo: {minimo}")
        if mode =="Maximizar":
            res = []
            x, y = solucionesx[0]
            res.append(r1 * x + r2 * y)
            x, y = solucionesy[0]
            res.append(r1 * x + r2 * y)
            x, y = soluciones[1]
            res.append(r1 * x + r2 * y)
            x, y = soluciones[0]
            res.append(r1 * x + r2 * y)
            maximo = max(res)
            print("Valor mínimo:", maximo)
            x5_label.config(text=f"Valor mínimo: {maximo}")
        
        plot_polygon(A,b)

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
#Ecuación objetivo
ecuacion_frame = tkinter.LabelFrame(frame, text="Ecuación objetivo")
ecuacion_frame.grid(row=2, column=0, sticky="news", padx=20,pady=10)

r1_label = tkinter.Label(ecuacion_frame, text="Valor X1")
r1_label.grid(row=0,column=0)
r1_entry = tkinter.Entry(ecuacion_frame)
r1_entry.grid(row=1,column=0)

r2_label = tkinter.Label(ecuacion_frame, text="Valor X2")
r2_label.grid(row=0,column=1)
r2_entry = tkinter.Entry(ecuacion_frame)
r2_entry.grid(row=1,column=1)

mm_label = tkinter.Label(ecuacion_frame, text="Modo")
title_combobox = ttk.Combobox(ecuacion_frame, values=["Minimizar", "Maximizar"])
mm_label.grid(row=0,column=2)
title_combobox.grid(row=1,column=2)



for widget in ecuacion_frame.winfo_children():
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