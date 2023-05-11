palabra1=input("Ingrese la primera palabra: ")
palabra2=input("Ingrese la segunda palabra: ")
if palabra1[-3:]==palabra2[-3:]:
    print("Estas palabras riman")
elif palabra1[-2:]==palabra2[-2:]:
    print("Estas palabras riman un poco")
else:
    print("Estas palabras no riman")