import math

import statistics 
from math import sqrt
import numpy as np
from scipy import stats
from matplotlib import pyplot as plt
import random

def generador_exponencial ( media , n ) :
    u = []
    for i in range ( n ) :
        r = random.random () # Numero random entre 0 y 1
        x = - media * math . log ( r ) # Aplicacion de la ecuacion (11)
        u . append ( x )
    return u


aleatorios = generador_exponencial(1,1000) # genera aleatorios
plt.figure("Histograma")
cuenta, cajas, ignorar = plt.hist(aleatorios, 20)

plt.ylabel('frequencia')
plt.xlabel('valores')
plt.title('Histograma Exponencial')

exponencial = stats.expon()
x = np.linspace(exponencial.ppf(0.01),
                exponencial.ppf(0.99), 1000)
fp = exponencial.pdf(x) # Función de Probabilidad


plt.figure('Grafica')
plt.plot(x, fp)
plt.title('Distribución Exponencial')
plt.ylabel('probabilidad')
plt.xlabel('valores')
plt.show()

