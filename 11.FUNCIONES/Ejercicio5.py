lista=[]
def medida():
    lista=[]
    x=int(input("Ingrese tamaño de lista: "))
    for i in range(x):
        y=int(input("{} valor: ".format(i+1)))
        lista.append(y)

medida()
print(lista)