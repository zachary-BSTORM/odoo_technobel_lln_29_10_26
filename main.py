def position_insertion(nombres: list, cible: int) -> int:
    g = 0
    d = len(nombres)
    
    while g < d:
        middle = (g + d) // 2
        if nombres[middle] < cible:
            g = middle + 1
        elif nombres[middle] > cible:
            d = middle
        else:
            return middle
    return g
print(position_insertion([1, 3, 5, 6], 7))
# [1, 3, 5, 7], 5 