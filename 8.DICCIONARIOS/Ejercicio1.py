diccionario={"Guatemala": "Ciudad de Guatemala", 
"El Salvador": "San Salvador", "Honduras": "Honduras",
"Nicaragua": "Managua", "Costa Rica": "San Jose",
 "Panama": "Panama", "Argentina": "Buenos Aires",
  "Colombia": "Bogota", "Venezuela": "Caracas", "España": "Madrid"}
pais=input("De que pais desea saber su capital: ")
letra=pais.title() in diccionario
if letra==True:
    print(diccionario[pais.title()])
else:
    print("El pais no se encuentra")