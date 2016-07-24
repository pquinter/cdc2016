from matplotlib import pyplot as plt
import pandas as pd
import numpy as np
import seaborn as sns

#mc
# Calcular el numero de segundos en un anio

#cc
seg_min, min_hr, hr_dia, dia_anio = 60, 60, 24, 365
seg_min * min_hr * hr_dia * dia_anio


#mc
# Escribir un programa que imprima 0 si un programa es palindrome, -1 si no. 
#
# Pista palabra[::-1] regresa la palabra al reves

# cc
palabra = 'anitalavalatina'
(palabra[::-1] == palabra) - 1

#mc
# #if
# Escribir una funcion que identifique el numero mas grande de un grupo de tres
#cc
#Funcion previa para idenificar el numero mas grande de un par
par = [1,2]
def mas_grande_par(par):
    """
    Identifica el numero mas grande de un par
    """
    if par[0] > par[1]: return par[0]
    else: return par[1]

trio = [1,2,5]
def mas_grande_tres(trio):
    """
    Identifica el numero mas grande de un grupo de tres
    """
    return mas_grande_par([trio[2], mas_grande_par(trio[:2])])

#mc
# Escribir una funcion que regrese nucleotidos complementarios (una sola letra)
#cc
def base_comp(base):
    """Regresa el nucleotido complementario"""
    # Convertir a minusculas
    base = base.lower()
    if base == 'a':
        return 'T'
    elif base == 't':
        return 'A'
    elif base == 'g':
        return 'C'
    elif base == 'c':
        return 'G'
    else: raise TypeError('Input incorrecto, solo acepta "As, Ts, Gs y Cs"')

#mc
# Calcular un factorial
#cc
def factorial(n):
    """Calcula factorial"""
    for i in range(1,n): n*=i
    return n
#mc
# Calcular secuencia de ADN complementaria
#cc
def sec_comp(secuencia):
    """Calcula secuencia de ADN complementaria"""
    complemento = ''
    for b in secuencia:
        complemento += base_comp(b)
    return complemento
#mc
# Traducir ADN
#cc
# Bases de ADN
bases = ['T', 'C', 'A', 'G']

# Hacer lista de codones
codons = []
for first_base in bases:
    for second_base in bases:
        for third_base in bases:
            codons += [first_base + second_base + third_base]
codons = [first_base + second_base + third_base for first_base in bases for second_base in bases for third_base in bases] 
# Amino acidos
amino_acids = 'FFLLSSSSYY**CC*WLLLLPPPPHHQQRRRRIIIMTTTTNNKKSSRRVVVVAAAADDEEGGGG'

# Hacer diccionario
codon_dict = dict(zip(codons, amino_acids))

#mc
# Comparar velocidad de funcion de numpy y funcion de python
#cc
# Crear una matriz de 10 mil numeros aleatorios entre 0 y 1
x = np.random.random(10000)

# Funcion de python para sumar
def python_sum(x):
    """Suma los numeros de x"""
    x_sum = 0.0
    for n in x:
        x_sum += n
    return x_sum

# Comparar velocidad
suma_python = %timeit -o python_sum(x)
suma_numpy = %timeit -o x.sum()
print(suma_python.best/suma_numpy.best)

#mc
# Crear y graficar lineas
#cc
def linea(m, x, b):
    """Funcion de una linea"""
    return m * x + b
# hacer la linea
m, x, b = 0.5, np.arange(10), 0
# graficar
plt.plot(x, linea(x))
# graficar coseno
x = np.linspace(0,100)
plt.plot(x, np.cos(x))
x_smooth = np.linspace(0,100,1000)
plt.plot(x_smooth, np.cos(x_smooth))

#mc
# Demostracion de seaborn y bokeh con graficos matplotlib
#cc

import seaborn as sns
x = np.random.random(10000)
plt.plot(x,'.')

import bokeh.io
import bokeh.mpl
import bokeh.plotting
# Configurar Bokeh para plots inline
bokeh.io.output_notebook()
# Hacer plot interactivo con bokeh (pegar despues de plot)
bokeh.plotting.show(bokeh.mpl.to_bokeh())

