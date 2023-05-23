import random as rn
from matplotlib import pyplot as plt
import numpy as np
from scipy import stats
import math as mt

def hipergeometrica (N,K,n) :
	x = 0
	c = N - K
	k = K
	for i in range (n-1) :
		r = rn.random()
		if r <= k / N :
			x += 1
			k -= 1
		else :
			c -= 1
		N -= 1
	return x

#GRAFICANDO EL HISTOGRAMA
datos = []
for i in range(1000):
	datos.append(hipergeometrica(500,50,100))
plt.figure("histograma")
plt.hist(datos,20)
plt.ylabel('frequencia')
plt.xlabel('valores')
plt.title('Histograma')

#GRAFICANDO LA DISTRIBUCION
M, n, N = 500, 50, 100 
hipergeometrica = stats.hypergeom(M, n, N)
x = np.arange(0, 21)
fmp = hipergeometrica.pmf(x)
plt.figure("distribucion")
plt.plot(x, fmp, '--')
plt.vlines(x, 0, fmp, colors='b', lw=5, alpha=0.5)
plt.title('Distribución Hipergeométrica')
plt.ylabel('probabilidad')
plt.xlabel('valores')
plt.show()
