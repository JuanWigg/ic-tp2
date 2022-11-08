## Seleccion, Cruza y mutación

from individuo import Individuo
import operaciones as op

print("Generando población para las pruebas...")

poblacion = op.generar_poblacion(10)

print("Población generada: ")
for individuo in poblacion:
    print(individuo)


pruebas_por_combinacion = 5



print("Ejecutando pruebas para: Seleccion por ventana - Estacional")
resultado_ventana_estacional = op.ejecutar_prueba(poblacion, pruebas_por_combinacion, op.avanzar_generacion_estacional, 0.025, op.seleccion_por_ventana)

print("Ejecutando pruebas para: Seleccion por torneo - Estacional")
resultado_torneo_estacional = op.ejecutar_prueba(poblacion, pruebas_por_combinacion, op.avanzar_generacion_estacional, 0.025, op.seleccion_por_torneo)

print("Ejecutando pruebas para: Seleccion por ruleta - Estacional")
resultado_ruleta_estacional = op.ejecutar_prueba(poblacion, pruebas_por_combinacion, op.avanzar_generacion_estacional, 0.025, op.seleccion_por_ruleta)

print("Ejecutando pruebas para: Seleccion por ventana - Generacional")
print("Ejecutando pruebas para: Seleccion por torneo - Generacional")
print("Ejecutando pruebas para: Seleccion por ruleta - Generacional")