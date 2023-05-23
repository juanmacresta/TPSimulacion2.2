import math
import statistics
from math import sqrt
import numpy as np
from scipy import stats
from matplotlib import pyplot as plt
import random as rd

tot = []

def binomiall(n, p):
  x=0
  for i in range(n):
    r=rd.random()
    if r <= p:
        x = x + 1
  return x

for i in range(100):
  tot.append(binomiall(10, 0.41))

plt.hist(tot,20)
plt.title("Histograma Binomial")
plt.xlabel("valores")
plt.ylabel("Frecuencia")
plt.show()



# Graficando Binomial
N, p = 100, 0.41 # parametros de forma 
binomial = stats.binom(N, p) # Distribución
x = np.arange(binomial.ppf(0.01),binomial.ppf(0.99))
fmp = binomial.pmf(x) # Función de Masa de Probabilidad
plt.plot(x, fmp, '--')
plt.vlines(x, 0, fmp, colors='b', lw=5, alpha=0.5)
plt.title('Distribución Binomial')
plt.ylabel('probabilidad')
plt.xlabel('valores')
plt.show()