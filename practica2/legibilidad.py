# -*- coding: utf-8 -*-
"""
Created on Tue Sep 30 10:25:58 2025

@author: Ferale
"""

nFrases = int(input('Introduce el número de frases: '))
nPalabras = int(input('Introduce el número de palabras: '))
nSilabas = int(input('Introduce el número de sílabas: '))

IFSZ = 206.835 - 62.3*nSilabas/nPalabras - nPalabras/nFrases

if IFSZ <= 40:
    gradoDificultad = 'Muy difícil'
elif IFSZ <= 55:
    gradoDificultad = 'Algo difícil'
elif IFSZ <= 65:
    gradoDificultad = 'Normal'
elif IFSZ <= 80:
    gradoDificultad = 'Bastante Fácil'
else:
    gradoDificultad = 'Muy fácil'

print(f'El grado de dificultad de este texto es {gradoDificultad} y su IFSZ es: {IFSZ}')