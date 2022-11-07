import random
from random import random as random_extra
from typing import List
from individuo import Individuo
cant_mutaciones = 0

def generar_poblacion(cantidad):
    individuos = []
    for _ in range(cantidad):
        individuos.append(generar_individuo())
    return individuos

def generar_individuo():
    individuo = Individuo()
    individuo.setRandomContenedores()
    return individuo

def seleccion_por_ruleta(individuos):
    fitness_total = float(sum(map(lambda x: x.fitness(), individuos)))
    individuos_probabilidad_individual = list(map(lambda x: x.fitness()/fitness_total,individuos))
    acumulado = 0
    individuos_probabilidad_acumulada = []
    
    for i in range(len(individuos_probabilidad_individual)):
        individuos_probabilidad_acumulada.append(calcular_acumulado(individuos_probabilidad_individual[i], acumulado))
        acumulado = individuos_probabilidad_acumulada[i]
    
    individuos_seleccionados = []
    for _ in range(len(individuos)):
        numero_seleccionado = random_extra()
        posicion_actual = 0
        while individuos_probabilidad_acumulada[posicion_actual] < numero_seleccionado:
            posicion_actual += 1
        individuos_seleccionados.append(individuos[posicion_actual]) 
    return individuos_seleccionados

def calcular_acumulado(probabilidad_individuo, acumulado_hasta_momento):
    nuevo_acumulado = probabilidad_individuo + acumulado_hasta_momento
    return nuevo_acumulado

def seleccion_por_torneo(individuos):
    individuos_por_torneo = max(len(individuos) / 3, 2)
    individuos_seleccionados = []
    for _ in range(len(individuos)):
        individuos_a_competir = random.choices(individuos, k = individuos_por_torneo)
        individuos_a_competir.sort(key=lambda x: x.fitness(), reverse=True)
        individuos_seleccionados.append(individuos_a_competir[0]) 
    return individuos_seleccionados

def seleccion_por_ventana(individuos):
    individuos.sort(key=lambda x: x.fitness(), reverse=True)
    individuos_seleccionados = []
    for i in range(len(individuos)):
        individuos_seleccionados.append(individuos[random.randint(0,i)]) 
    return individuos_seleccionados

def cruza(padre1, padre2):
    punto_corte = random.randint(1, len(padre1.contenedores)-1)
    #print("Punto de corte: ", punto_corte)
    primera_parte_padre1, segunda_parte_padre1 = padre1.dividirContenedores(punto_corte)
    primera_parte_padre2, segunda_parte_padre2 = padre2.dividirContenedores(punto_corte)
    hijo1 = Individuo()
    hijo1.setContendores(primera_parte_padre1 + segunda_parte_padre2)
    hijo2 = Individuo()
    hijo2.setContendores(primera_parte_padre2 + segunda_parte_padre1)
    return hijo1, hijo2

def mutar_contenedor(valor):
    return 0 if valor==1 else 1

def mutacion(individuo):
    global cant_mutaciones
    print("Mutacion #", cant_mutaciones)
    cant_mutaciones += 1
    mutador = Individuo()
    mutador.setRandomContenedores()
    print("Cromosoma de mutacion: ", mutador.contenedores)
    contenedores_mutados = []
    for i in range(len(individuo.contenedores)):
        if mutador.contenedores[i] == 1:
            contenedores_mutados.append(mutar_contenedor(individuo.contenedores[i]))
        else:
            contenedores_mutados.append(individuo.contenedores[i])
    individuo_mutado = Individuo()
    individuo_mutado.setContendores(contenedores_mutados)
    return individuo_mutado

def get_2_individuos(individuos):
    seleccionados = random.choices(individuos, k = 2)
    return seleccionados[0], seleccionados[1]

def mutar_segun_probabilidad(individuo: Individuo, probabilidad: float):
    return mutacion(individuo) if probabilidad>random_extra() else individuo


def avanzar_generacion(individuos: List):
    seleccionados = seleccion_por_ventana(individuos)
    
    padre1,padre2 = get_2_individuos(seleccionados)

    hijo1,hijo2 = cruza(padre1,padre2)

    hijo1 = mutar_segun_probabilidad(hijo1,0.025)
    hijo2 = mutar_segun_probabilidad(hijo2,0.025)

    areemplazar1,areemplazar2 = get_2_individuos(individuos)

    individuos.remove(areemplazar1)
    individuos.remove(areemplazar2)

    individuos.append(hijo1)
    individuos.append(hijo2)

def avanzar_generacion_generacional(individuos: List, probabilidad_mutacion: float, funcion_seleccion: any):
        nueva_gen = []
        seleccionados = funcion_seleccion(individuos).copy()

        while len(seleccionados)>1:
            padre1,padre2 = get_2_individuos(seleccionados)

            hijo1,hijo2 = cruza(padre1,padre2)

            hijo1 = mutar_segun_probabilidad(hijo1, probabilidad_mutacion)
            hijo2 = mutar_segun_probabilidad(hijo2, probabilidad_mutacion)
            
            seleccionados.remove(padre1)
            seleccionados.remove(padre2)
            
            nueva_gen.append(hijo1)
            nueva_gen.append(hijo2)

        if len(seleccionados)==1:
            print("Quedo un individuo sin pareja: ", seleccionados[0])
            print("Pasa a la siguiente generacion")
            nueva_gen.append(seleccionados[0])
            seleccionados.remove(seleccionados[0])

        return nueva_gen


def get_fittest(poblacion: List):
    poblacion.sort(key=lambda x: x.fitness(), reverse=True)
    return poblacion[0]