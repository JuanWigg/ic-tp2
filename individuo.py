import random
from time import time

class Individuo:
    pesos_containers = [100, 155, 50, 112, 70, 80, 60, 118, 110, 55]

    def __init__(self):
        self.contenedores = []

    def __repr__(self):
        return str(self.contenedores)

    def fitness(self):
        total = 0
        for i in range(10):
            total += self.contenedores[i] * self.pesos_containers[i]
        return 0 if total>700 else total
    
    def setContendores(self, contenedores):
       self.contenedores = contenedores
    
    def setRandomContenedores(self):
        for i in range(10):
            self.contenedores.append(random.randint(0,1))

    def dividirContenedores(self, punto_corte):
        return self.contenedores[:punto_corte], self.contenedores[punto_corte:]
