from io import open
archivo_texto=open("archivo.txt","w")
frase="Estupendo dia para estudiar python"
archivo_texto.write(frase)
archivo_texto.close()