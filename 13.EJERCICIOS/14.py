precio=input("Ingrese el precio de un producto: ")
print(precio[:precio.find(".")],"y",precio[precio.find(".")+1:],"Centimos")