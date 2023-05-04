import numpy as np
import matplotlib.pyplot as plt

x1=3
x2=1
x3=3
y1=1
y2=5
y3=2
c1=15
c2=20
c3=24
f1=120
f2=60
solucionesx=[]
solucionesy=[]
soluciones=[]


A = np.array([[x1, y1], [x2, y2], [x3, y3]])
b = np.array([c1, c2, c3])
f = np.array([f1, f2])
mode ="Minimizar"

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


if mode == "Minimizar":
    res=[]
    a=[]
    a1=[]

    a.append(solucionesx[2])
    a.append(solucionesy[2])
    a1.append(soluciones)
    print(a1)
    for i in range(len(a1)):
        x,y = a1[i]
        res.append(f1 * x + f2 * y)

    for i in range(len(a)):
        x, y = a[i]
        res.append(f1 * x + f2 * y)

    res.sort()
    minimo = res[1]
    indice_min = res.index(minimo)
    x_min, y_min = a[indice_min]
    print("Valor mínimo:", minimo)
    print("Coordenadas asociadas:", x_min, y_min)

if mode =="Maximizar":
    res = []
    a = []
    a1 = []

    a.append(solucionesx[0])
    a.append(solucionesy[0])
    a1.append(soluciones)
    print(a1)
    for i in range(len(a1)):
        x, y = a1[i]
        res.append(f1 * x + f2 * y)

    for i in range(len(a)):
        x, y = a[i]
        res.append(f1 * x + f2 * y)

    res.sort()
    minimo = res[1]
    maximo = max(res)
    indice_max = res.index(maximo)
    x_max, y_max = a[indice_max]
    print("Valor maximo:", maximo)
    print("Coordenadas asociadas:", x_max, y_max)