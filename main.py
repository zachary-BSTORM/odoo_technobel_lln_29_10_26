def indice_pic(nombres: list) -> int:
    g = 0
    d = len(nombres) - 1
    while g < d:
        middle = (g + d) // 2
        if nombres[middle] < nombres[middle + 1]:
            g = middle + 1
        else:
            d = middle
    return g


value = [9,8,7,6,5]

print(indice_pic(value))


# [1,2,3,4,5,6,7,8,9]
#  0                 len() - 1