# scenario des donctions
class LaboException(Exception):
    '''Généralise toute les exceptions du labo.'''
    pass
class AbsentException:
    pass
class PresentException: 
    pass

labo = {}

labo['Milo'] = 301
labo['Lucas'] = 302
labo['Elisa'] = 303
print(labo)

def enregistrer_arrivee(nom, bureau):
    if nom in labo: 
        raise PresentException(f"{nom} est déjà présent dans le laboratoire.")          #  un raise pour lever une exception du prenom qui existe déjà
    labo[nom] = bureau

enregistrer_arrivee('Milo', 304)
assert labo['Mel'] == 304

def enregistrer_depart (nom):
     if nom not in labo:
        raise AbsentException(f"{nom} est inconnue.")
     del labo[nom]

enregistrer_depart('Elisa')
assert 'Elisa' not in labo

def modifier_bureau(nom, nouveau_bureau):
     if nom not in labo:
        raise AbsentException(f"{nom} est inconnue.")
     labo[nom]=nouveau_bureau

modifier_bureau('Milo', 310)
assert labo['Milo'] == 310

def modifier_nom(nom_actuel, nouveau_nom):
    if nom_actuel not in labo : 
        raise AbsentException(f'{nom_actuel} est inconnue.')
    labo[nouveau_nom] = labo.pop(nom_actuel)

modifier_nom('Mel', 'Melanie')
assert 'Melanie' in labo 

def est_membre(nom):
     return nom in labo             # à voir si fonctionne sinon voir avec .get 

est_membre('Lucas')
assert est_membre('Lucas') == True 

def obtenir_bureau(nom):
     if nom not in labo:
        raise AbsentException(f"{nom} est incconue.")
     return labo[nom]

obtenir_bureau('Melanie')
assert obtenir_bureau('Melanie') == 304

def liste_personnel():
     print(list(labo.items()))

liste_personnel()