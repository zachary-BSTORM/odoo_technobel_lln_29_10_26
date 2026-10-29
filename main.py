def type_suite(nombres: list[int]) -> str:
    # ecart
    ecart = nombres[1] - nombres[0]  # récupération de l'écart
    if all(nombres[i] - nombres[i - 1] == ecart for i in range(2, len(nombres))):
        return "arithmetique"

    # rapport
    a, b = nombres[0], nombres[1]  # récupération des premières valeurs
    # [2, 6, 18, 54]
    # Si i == 2
    # (nb[i] == 18) & (nb[i - 1] == 6)
    #  ( 18 * 2 ) == (6 * 6 )
    #  (36)       == (36)
    if all(nombres[i] * a == nombres[i - 1] * b for i in range(2, len(nombres))):
        return "geometrique"

    return "aucune"

ar = [2, 4, 6, 8]
geo = [2, 6, 18, 54]
aucun = [1, 2, 4, 7]


type_suite(ar)
type_suite(geo)
type_suite(aucun)
