from matplotlib import pyplot as plt
import pandas as pd
import numpy as np
import seaborn as sns


# mc
# # Ejercicios
# Calcular el numero de segundos en un anio

#cc
seg_min, min_hr, hr_dia, dia_anio = 60, 60, 24, 365
seg_min * min_hr * hr_dia * dia_anio


# mc
# Ejercicio: Escribir un programa que imprima 0 si un programa es palindrome,
# -1 si no. Pista palabra[::-1] regresa la palabra al reves

# cc
palabra = 'anitalavalatina'
(palabra[::-1] == palabra) - 1

