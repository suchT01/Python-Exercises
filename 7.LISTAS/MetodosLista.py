lista=[1,2,3,4,5]
print(lista)
lista.append(6) # Primer metodo para agrandar lista
print(lista)
lista.insert(2,2.5) # Insertar un valor en la lista
print(lista)

# -----------------

print(lista.count(5)) # Revisa cuantos elementos del parametro seleccion hay en la lista
print(lista.index(4)) # Encuentra el numero deseado

lista2=[5,3,4,1,2]
lista2.sort()         # Arregla una lista de enteros en orden
print(lista2)
lista2.reverse()      # Revierte el orden de una lista
print(lista2)

#---------------------

lista3=["Python",24,"Rene","alexander",12]
print(lista3)
# Arreglar alexander a Alexander
lista3[3]="Alexander"
print(lista3)
lista3.pop() # Elimina el ultimo dato de la lista
print(lista3)
lista3.remove("Python") # ELimina cualquier valor de una lista, hay que decirle cual es
print(lista3)
