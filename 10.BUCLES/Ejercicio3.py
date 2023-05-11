numeros=[1,2,3,4,5,6,7,8,9,10]
print(numeros)
print("Ingrese dos numeros para saber el rango entre esos numeros.")
x=int(input("Primer numero: "))
y=int(input("Segundo numero: "))
for i in range(x,y+1):
    print(i)
'''
La funcion range indica sobre que rango oscilar, es decir se coloca el
primer numero donde empieza y el segundo numero donde termina el rango
y la segunda cifra no es tomada en cuenta y por eso se coloca y+1

'''
palabra=input("Ingrese una palabra: ")
lista=[palabra]
for i in lista:
    print(palabra)