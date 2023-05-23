import random as rd
from matplotlib import pyplot as plt
import numpy as np
from scipy.stats import geom
import math as mt

def generate_geometric_values (p, size) :
	geometricValuesList = []
	for i in range (size):
		r = rd.random()
		q = 1 - p
		x = mt.floor(mt.log(r)/mt.log(q))
		geometricValuesList.append(x)
	return geometricValuesList

#GRAFICANDO EL HISTOGRAMA
datos = generate_geometric_values(0.1,1000)
plt.figure("histograma")
plt.hist(datos,20)
plt.ylabel('frequencia')
plt.xlabel('valores')
plt.title('Histograma')

#GRAFICANDO LA DISTRIBUCION
p =  0.1
geometrica = geom(p)
x = np.arange(geometrica.ppf(0.01),
              geometrica.ppf(0.99))
fmp = geometrica.pmf(x)
plt.figure("distribucion")
plt.plot(x, fmp, '--')
plt.vlines(x, 0, fmp, colors='b', lw=5, alpha=0.5)
plt.title('Distribución Geométrica')
plt.ylabel('probabilidad')
plt.xlabel('valores')
plt.show()