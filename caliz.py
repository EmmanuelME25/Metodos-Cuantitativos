import matplotlib.pyplot as plt

# Definir las ecuaciones de las tres restricciones
# Por ejemplo, las siguientes son tres ecuaciones de la forma y = mx + b
def restriccion_1(x):
    return (1/2)*x + 3

def restriccion_2(x):
    return -2*x + 10

def restriccion_3(x):
    return -3*x + 9

# Encontrar los puntos de intersección
# Para encontrar los puntos de intersección, resuelva las ecuaciones simultáneamente
# Por ejemplo, para encontrar el punto de intersección entre restriccion_1 y restriccion_2:
# (1/2)*x + 3 = -2*x + 10
# x = 4
# y = (1/2)*4 + 3 = 5

x1 = 4
y1 = 5

# Encuentre los otros puntos de intersección de manera similar

x2 = (3/5)
y2 = (9/5)

x3 = 2
y3 = -1

# Graficar los puntos de intersección
plt.scatter(x1, y1, color='red')
plt.scatter(x2, y2, color='blue')
plt.scatter(x3, y3, color='green')

# Configurar la gráfica
plt.title('Puntos de intersección de 3 restricciones')
plt.xlabel('Eje x')
plt.ylabel('Eje y')

# Mostrar la gráfica
plt.show()