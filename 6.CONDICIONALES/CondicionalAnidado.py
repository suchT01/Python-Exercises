nombre=input("Nombre? ")
edad=int(input("Edad? "))
if nombre=="Juan":
    if edad>=18:
        print("Eres Juan y mayor de edad")
    else:
        print("Eres Juan pero no el mayor")
else:
    print("No eres Juan")