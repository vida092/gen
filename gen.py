import random
import string
from turtle import *
import colorsys
import time

objetivo = "Frase objetivo"
tamaño_población = 300
tasa_mutación = 0.01


generaciones = 1000
up = (len(objetivo)) * "="

caracteres_posibles = string.ascii_letters + " " +"é" + "\n"

def aptitud(individuo):
    return sum([1 for i, j in zip(individuo, objetivo) if i == j])


def cruce(padre1, padre2):
    punto_cruce = random.randint(0, len(objetivo) - 1)
    return padre1[:punto_cruce] + padre2[punto_cruce:]


def mutación(individuo):
    individuo = list(individuo)
    for i in range(len(individuo)):
        if random.random() < tasa_mutación:
            individuo[i] = random.choice(caracteres_posibles)
    return ''.join(individuo)

def inicializar_población(tamaño):
    población = []
    for _ in range(tamaño):
        individuo = ''.join(random.choice(caracteres_posibles) for _ in range(len(objetivo)))
        población.append(individuo)
    return población

def selección(población):
    torneo = random.sample(población, k=3)
    torneo.sort(key=aptitud, reverse=True)
    return torneo[0]


def algoritmo_genético():
    población = inicializar_población(tamaño_población)
    for generación in range(generaciones):
        nueva_población = []
        for _ in range(tamaño_población):
            padre1 = selección(población)
            padre2 = selección(población)
            hijo = cruce(padre1, padre2)
            hijo = mutación(hijo)
            nueva_población.append(hijo)
        población = nueva_población

        mejor_individuo = max(población, key=aptitud)
        peor_individuo = min(población, key=aptitud)
        print(f"Generación {generación}: {peor_individuo} (aptitud: {aptitud(mejor_individuo)})")

        
        if mejor_individuo == objetivo:
            print(f"\n{up}\n{mejor_individuo}\n\n{up}")
            break
    if mejor_individuo != objetivo:
        print(mejor_individuo)
algoritmo_genético()
