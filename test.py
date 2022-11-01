import operaciones as op

poblacion = op.generar_poblacion(20)
print(poblacion)

op.avanzar_generacion(poblacion)

contador = 1000
#(op.get_fittest(poblacion).fitness()<650) or 
while((contador < 1)):
    op.avanzar_generacion(poblacion)
    contador -= 1

print("Listo!")
print("El + fit: ", op.get_fittest(poblacion))
print("Con un fitness de: ", op.get_fittest(poblacion).fitness())