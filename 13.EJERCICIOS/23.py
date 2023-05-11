def small_enough(array, limit):
    for i in array:
        if i>limit:
            return False
    return True

print(small_enough([78, 33, 22, 44, 87, 9, 6],87))