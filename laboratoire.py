class LaboException(Exception):
    '''Généralise toute les exceptions du labo.'''
    pass
class AbsentException:
    pass
class PresentException: 
    pass


def laboratoire():
    return {}

def enregistrer_arrivee(labo, nom, bureau : int):
    if nom in labo: 
        raise PresentException(f"{nom} est déjà présent dans le laboratoire.")          #  un raise pour lever une exception du prenom qui existe déjà
    labo[nom] = bureau


def enregistrer_depart(labo, nom):
    if nom not in labo:
        raise AbsentException(f"{nom} est inconnue.")                              #  un raise pour lever l'erreur du prenom déjà pas dans le dico
    del labo[nom]


def modifier_bureau(labo, nom, nouveau_bureau):
    if nom not in labo:
        raise AbsentException(f"{nom} est inconnue.")
    labo[nom]=nouveau_bureau


def modifier_nom(labo, nom_actuel, nouveau_nom):
    if nom_actuel not in labo : 
        raise AbsentException(f'{nom_actuel} est inconnue.')
    labo[nouveau_nom] = labo.pop(nom_actuel)


def est_membre(labo, nom):
    return nom in labo             # à voir si fonctionne sinon voir avec .get 


def obtenir_bureau(labo, nom):
    if nom not in labo:
        raise AbsentException(f"{nom} est incconue.")
    return labo[nom]


def liste_personnel(labo):
    return list(labo.items())

def liste_bureau(labo):
    bureaux = {}
    for nom, bureau in labo.items():
        if bureau not in bureaux:
            bureaux[bureau] = []
        bureaux[bureau].append(nom)
    return list(bureaux.items())

   