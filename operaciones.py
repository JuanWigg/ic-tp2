import random
from individuo import Individuo

def generar_poblacion(cantidad):
    individuos = []
    for i in range(cantidad):
        individuos.append(generar_individuo())
    return individuos

def generar_individuo():
    individuo = Individuo()
    individuo.setRandomContenedores()
    return individuo

def seleccionPorVentana(individuos):
    individuos.sort(key=lambda x: x.fitness(), reverse=True)
    individuos_seleccionados = []
    for i in range(len(individuos)):
        individuos_seleccionados.append(individuos[random.randint(0,i)]) 
    return individuos_seleccionados

def cruza(padre1, padre2):
    punto_corte = random.randint(1, len(padre1.contenedores)-1)
    print("Punto de corte: ", punto_corte)
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


