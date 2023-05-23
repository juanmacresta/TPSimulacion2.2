import random
from math import exp
from matplotlib import pyplot as plt
import numpy as np
from scipy import stats
#https://webs.um.es/mpulido/miwiki/lib/exe/fetch.php?media=wiki:simt3.pdf
#1. Generar un numero aleatorio u
#2.Hacer x = 0, P = F = e−λ
#3.Si u < F, ir al paso 5
#4.Hacer P =(λ/(x+1))P, F = F + p, x = x + 1. Ir al paso 3
#5.x es el valor generado de X.

numeros = []
l=3 #lambda
for i in range(1000):
    u=random.random()
    x=0
    P = F = exp(-l)
    while ( u>=F ):
        P = (l / (x+1))*P
        F = F+P
        x=x+1
    numeros.append(x)

#HISTOGRAMA
# plt.hist(numeros,linewidth=1)
# plt.title('Distribución de poisson')
# plt.ylabel('frecuencia')
# plt.xlabel('valores')
# plt.title('Histograma')
# plt.show()


#DISTRIBUCION
# mu =  3 # parametro de forma
# poisson = stats.poisson(mu) # Distribución
# x = np.arange(poisson.ppf(0.01),
#               poisson.ppf(0.99))
# fmp = poisson.pmf() # Función de Masa de Probabilidad

