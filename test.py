import operaciones as op

poblacion = op.generar_poblacion(4)
print("Poblacion inicial: ")
for individuo in poblacion:
    print(individuo)
    
print(op.avanzar_generacion_generacional(poblacion, probabilidad_mutacion=0.025, funcion_seleccion=op.seleccionPorRuleta))
#op.seleccion_por_torneo(poblacion)


#
#op.avanzar_generacion(poblacion)

# contador = 1000
# while((op.get_fittest(poblacion).fitness()<680) and (contador > 1)):
#     op.avanzar_generacion(poblacion)
#     print(f'Generacion {1001-contador}')
#     contador -= 1

# print("Listo!")
# print("Mejor individuo de la última gen: ", op.get_fittest(poblacion))
# print("Con un fitness de: ", op.get_fittest(poblacion).fitness())