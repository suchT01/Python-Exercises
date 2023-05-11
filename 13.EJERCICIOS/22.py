import math
def cooking_time(eggs):
    time=0
    if eggs>8:
        op=math.ceil(eggs/8)
        for i in range(op):
            time+=5
        return time
    elif 0<eggs<8:
        return 5
    else:
        return 0

print(cooking_time(5199))