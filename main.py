liste = [1,2,3]


def update_liste(value):
    value[:] = [6,7,8,9]
    print(value)
    
print(liste)
update_liste(liste)
print(liste)