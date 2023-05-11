def pedir():
    x=int(input("Primer valor: "))
    y=int(input("Segundo valor: "))
    if x>y:
        return 1
    elif y==x:
        return 0
    else:
        return -1

print(pedir())