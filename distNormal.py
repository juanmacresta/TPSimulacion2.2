import random as rd
from matplotlib import pyplot as plt
import numpy as np
from scipy.stats import norm

def generate_normal (mu,sigma,size) :
	normalValuesList = []
	for z in range (size):
		sum = 0.0
		for i in range (12):
			sum += rd.random ()
		normalValue = sigma*(sum-6.0) + mu
		normalValuesList.append(normalValue)
	return normalValuesList

#GRAFICANDO EL HISTOGRAMA
datos = generate_normal(10,1,1000)
plt.hist(datos,20)
plt.ylabel('frequencia')
plt.xlabel('valores')
plt.title('Histograma')
plt.show()

#GRAFICANDO LA DISTRIBUCION
x_axis = np.arange(6, 14, 0.01)
plt.plot(x_axis, norm.pdf(x_axis, 10, 1))
plt.title('Distribucion normal')
plt.ylabel('probabilidad')
plt.xlabel('valores')
plt.show()