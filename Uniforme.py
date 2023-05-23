import math
import statistics 
from math import sqrt
import numpy as np
from scipy.stats import uniform
from matplotlib import pyplot as plt
import random


def f(x):
    return 100

def generador_uniforme (a , b , n ) :
    u=[]
    for i in range ( n ):
        r=random.random ()
        valorUniforme = a + r *( b - a )
        u.append(valorUniforme)
    return u


#def exponencial ( media , n ) :
#    sample = []
#    for i in range ( n ) :
#        r = random.random () # Numero random entre 0 y 1
#        x = - media * math.log ( r ) # Aplicacion de la ecuacion (11)
#        sample . append ( x )
#    return sample



x=np.arange(10,20,1)
aleatorios = generador_uniforme(10,20,1000) # genera aleatorios
print(aleatorios)
print (statistics.mean(aleatorios))
cuenta, cajas, ignorar = plt.hist(aleatorios, 10)
plt.plot(x,[f(i) for i in x])
plt.ylabel('frequencia')
plt.xlabel('valores')
plt.title('Histograma Uniforme')
plt.show()


    
