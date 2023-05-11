def smash(words):
    o=""
    for i in words:
        if len(words) == 1:
            o=i
            return o
        else:
            o=o+i+" "
    print(o[0:len(o)])

smash(["hello", "world"])