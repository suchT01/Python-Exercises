diccionario={1:2,2:3,3:4}
diccionario2={6:7}
print(diccionario)
'''diccionario.pop(2) # Elimina una clave indicando cual se quiere eliminar
print(diccionario)
diccionario.clear() # Elimina todo el diccionario
print(diccionario)'''
print(diccionario.get(2)) # Trae valores llamados por clave
diccionario.setdefault(4,5) # Agregar una nueva clave y valor
print(diccionario)
diccionario.update(diccionario2) # ACtualiza el diccionario juntando dos
print(diccionario)
"Diccionario.copy() Genera otro diccionario igual "
