def premier_client_recurrent(commandes : list[dict[str:str]], minimum:int) -> str:
    compteur = {}
    name = {}
    
    for c in commandes:
        nom = c["client"].strip()
        cle = nom.lower()
        
        if cle not in name:
            name[cle] = nom
        compteur[cle] = compteur.get(cle,0) + 1
        
        if compteur[cle] == minimum:
            return name[cle]
    return "-1"
        
        
        
l = [
    {'ref': 'S001', 'client': ' Azure Interior'}, 
 {'ref': 'S002', 'client': 'Deco Addict'}, 
 {'ref': 'S003', 'client': 'deco addict '}, 
 {'ref': 'S004', 'client': 'Azure Interior'}, 
 {'ref': 'S005', 'client': 'AZURE interior'}
 ]
qty = 2

print(premier_client_recurrent(l,qty))