import random
def premiere_derniere(nombres: list, cible: int) -> list:
    def get_index(first):
        g = 0
        d = len(nombres) - 1
        res = -1
        while g <= d:
            m = (g + d) // 2
            if nombres[m] == cible:
                res = m
                if first:
                    d = m - 1
                else:
                    g = m + 1
            elif nombres[m] < cible:
                g = m + 1
            else :
                d = m - 1
        return res
    return [get_index(True),get_index(False)]
    
print(premiere_derniere([1, 2, 2, 3, 5, 7], 2))


def quick_sort(value):
    if len(value) <= 1:
        return value
    
    pivot = random.choice(value)
    petit = [v for v in value if v < pivot]
    egal = [v for v in value if v == pivot]
    grande = [v for v in value if v > pivot]
    
    return quick_sort(petit) + egal + quick_sort(grande)

print(quick_sort([5,7,8,9,5,21,1,54,3]))