import math
peso=float(input("Ingrese su peso: "))
estatura=float(input("Ingrese su estatura en metros: "))
imc=round(float((peso/(estatura**2))),2)
print("Tu imc es igual a:",imc)

# Round se usa para redondear y se tiene que importar de math