## Seleccion, Cruza y mutación

from individuo import Individuo
import operaciones as op

poblacion = op.generar_poblacion(3)
#print(poblacion)


individuo = Individuo()
individuo.setContendores([1,0,0,0,0,0,0,0,0,0])
individuo2 = Individuo()
individuo2.setContendores([1,1,1,1,1,1,1,1,1,1])
individuo3 = Individuo()
individuo3.setContendores([1,0,1,0,0,0,0,0,0,0])

individuos = []
individuos.append(individuo2)
individuos.append(individuo)
individuos.append(individuo3)
#print(op.seleccionPorVentana(individuos))

#print(op.cruza(individuo, individuo2))


print(op.mutacion(individuo2))





