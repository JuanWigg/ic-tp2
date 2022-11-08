## Seleccion, Cruza y mutación

from individuo import Individuo
import operaciones as op

def print_resultados(resultados):
    for i in range(len(resultados)):
        print("Prueba #", i)
        print("Cantidad de generaciones: ", resultados[i][0], " - Individuo más fit: ", resultados[i][1], "- Fitness del individuo: ", resultados[i][2])

print("Generando población para las pruebas...")

poblacion = op.generar_poblacion(4)

print("Población generada: ")
for individuo in poblacion:
    print(individuo)


pruebas_por_combinacion = 5
probabilidad_de_mutacion = 0.010

print("---------------------------------------------------------------------------------------------------------------------")

print("Ejecutando pruebas para: Seleccion por ventana - Estacional Random")
resultado_ventana_estacional = op.ejecutar_prueba(poblacion, pruebas_por_combinacion, op.avanzar_generacion_estacional_random, probabilidad_de_mutacion, op.seleccion_por_ventana)
print_resultados(resultado_ventana_estacional)

print("---------------------------------------------------------------------------------------------------------------------")

print("Ejecutando pruebas para: Seleccion por torneo - Estacional Random")
resultado_torneo_estacional = op.ejecutar_prueba(poblacion, pruebas_por_combinacion, op.avanzar_generacion_estacional_random, probabilidad_de_mutacion, op.seleccion_por_torneo)
print_resultados(resultado_torneo_estacional)

print("---------------------------------------------------------------------------------------------------------------------")

print("Ejecutando pruebas para: Seleccion por ruleta - Estacional Random")
resultado_ruleta_estacional = op.ejecutar_prueba(poblacion, pruebas_por_combinacion, op.avanzar_generacion_estacional_random, probabilidad_de_mutacion, op.seleccion_por_ruleta)
print_resultados(resultado_ruleta_estacional)

print("---------------------------------------------------------------------------------------------------------------------")

print("Ejecutando pruebas para: Seleccion por ventana - Estacional con reemplazo de padres debiles")
resultado_ventana_estacional_debiles = op.ejecutar_prueba(poblacion, pruebas_por_combinacion, op.avanzar_generacion_estacional_padres_debiles, probabilidad_de_mutacion, op.seleccion_por_ventana)
print_resultados(resultado_ventana_estacional_debiles)

print("---------------------------------------------------------------------------------------------------------------------")

print("Ejecutando pruebas para: Seleccion por torneo - Estacional con reemplazo de padres debiles")
resultado_torneo_estacional_debiles = op.ejecutar_prueba(poblacion, pruebas_por_combinacion, op.avanzar_generacion_estacional_padres_debiles, probabilidad_de_mutacion, op.seleccion_por_torneo)
print_resultados(resultado_torneo_estacional_debiles)

print("---------------------------------------------------------------------------------------------------------------------")

print("Ejecutando pruebas para: Seleccion por ruleta - Estacional con reemplazo de padres debiles")
resultado_ruleta_estacional_debiles = op.ejecutar_prueba(poblacion, pruebas_por_combinacion, op.avanzar_generacion_estacional_padres_debiles, probabilidad_de_mutacion, op.seleccion_por_ruleta)
print_resultados(resultado_ruleta_estacional_debiles)

print("---------------------------------------------------------------------------------------------------------------------")

print("Ejecutando pruebas para: Seleccion por ventana - Generacional")
resultado_ventana_generacional = op.ejecutar_prueba(poblacion, pruebas_por_combinacion, op.avanzar_generacion_generacional, probabilidad_de_mutacion, op.seleccion_por_ventana)
print_resultados(resultado_ventana_generacional)

print("---------------------------------------------------------------------------------------------------------------------")

print("Ejecutando pruebas para: Seleccion por torneo - Generacional")
resultado_torneo_generacional = op.ejecutar_prueba(poblacion, pruebas_por_combinacion, op.avanzar_generacion_generacional, probabilidad_de_mutacion, op.seleccion_por_torneo)
print_resultados(resultado_torneo_generacional)

print("---------------------------------------------------------------------------------------------------------------------")

print("Ejecutando pruebas para: Seleccion por ruleta - Generacional")
resultado_ruleta_generacional = op.ejecutar_prueba(poblacion, pruebas_por_combinacion, op.avanzar_generacion_generacional, probabilidad_de_mutacion, op.seleccion_por_ruleta)
print_resultados(resultado_ruleta_generacional)
print("---------------------------------------------------------------------------------------------------------------------")

