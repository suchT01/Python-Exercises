print("Para las elecciones tenemos tres candidatos \nCandidato A, B, C \nIngrese el candidato por el que desea votar")
candidato=input()
if candidato[-1:].upper()=="A":
    print("Usted a votado por el Candidato A")
elif candidato[-1:].upper()=="B":
    print("Usted a votado por el candidato B")
elif candidato[-1:].upper()=="C":
    print("Usted a votado por el candidato C")
else:
    print("No ha votado por ninguno")