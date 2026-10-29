def compresser(s: str) -> str:
    morceaux = []
    compteur = 1
    for i in range(1, len(s)):
        if s[i] == s[i - 1]:
            compteur += 1
        else:
            morceaux.append(f"{compteur}{s[i - 1]}")
            compteur = 1
    morceaux.append(f"{compteur}{s[- 1]}")
    return "".join(morceaux)


value = "wwwggopp"

print(compresser(value))
