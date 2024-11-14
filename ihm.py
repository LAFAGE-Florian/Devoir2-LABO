'''
PARTIE MENU 
'''
from laboratoire import *
from laboratoire import *


# importer les exceptions

def afficher_menu(): 
    print("1. Enregistrer l'arrivée d'une nouvelle personne.")
    print("2. Enregistrer le départ d'une personne.")
    print("3. Modifier le bureau occuper par une personne.")
    print("4. Changer le nom d'une personne.")
    print("5. Présence d'une personne dans le laboratoire.")
    print("6. Obtenir le bureau d'une personne.")
    print("7. Produire la liste du personnel.")
    print("8. Produire la liste des bureaux occupés.")
    print("0. Quitter.")


def demander_choix():
    return (input("Votre choix: "))


def gerer_arrivee(labo):
    try:
        nom = input("Nom de la personne: ")
        bureau = input("Numéro du bureau: ")
        enregistrer_arrivee(labo, nom, bureau)
        print(f"{nom} ajouté au bureau {bureau}.")
    except PresentException:
                print(f'{nom} est déjà présent dans le laboratoire')

def gerer_depart(labo):
    try:
        nom = input("Nom de la personne: ")
        enregistrer_depart(labo, nom)
        print(f"{nom} a été supprimé")
    except AbsentException:
        print(f'{nom} ne fait pas partie du laboratoire')


def gerer_bureau(labo):
    try:
        nom = input("Nom de la personne: ")
        nouveau_bureau = input("Numéro du nouveau bureau: ")
        modifier_bureau(labo, nom, nouveau_bureau)
    except AbsentException:
        print(f'{nom} ne fait pas partie du laboratoire')


def gerer_nom(labo):
    try: 
        nom_actuel = input("Nom de la personne: ")
        nouveau_nom = input("Nouveau nom de la personne: ")
        modifier_nom(labo, nom_actuel, nouveau_nom)
    except AbsentException: 
        print(f'{nom_actuel} ne fait pas partie du laboratoire')


def traiter_choix(choix, labo): 
        if choix == '1': 
            gerer_arrivee(labo)
        elif choix == '2': 
            gerer_depart(labo)       
        elif choix == '3':
            gerer_bureau(labo)
        elif choix == '4':
            gerer_nom(labo)
        elif choix == '5':
            nom = input("Nom de la personne: ")
            reponse = est_membre(labo, nom)
            print(f'{nom} est présent.e dans le laboratoire' if reponse else f'{nom} est incconu.e')
        elif choix == '6':
            try : 
                nom = input('Nom de la personne: ')  
                obtenir_bureau(labo, nom)
                print(f'Le bureau de {nom} est le bureau: {labo[nom]}')
            except AbsentException:
                print(f'{nom} est incconu.e')
        elif choix == '7':
            personnel = liste_personnel(labo)
            for nom, bureau in personnel:
                print(f"{nom} - bureau : {bureau}")
        elif choix == '8':
            bureaux = liste_bureau(labo)
            for bureau, noms in bureaux:
                print(f'Bureaux {bureau}:')
                for nom in noms:
                    print(f'- {nom}')
        elif choix == '0':
            print('Au revoir...')
        else: 
            print('Choix invalide.')


def main():
    quitter = False
    labo = laboratoire()
    while not quitter: 
        afficher_menu()
        choix = demander_choix()
        print()
        traiter_choix(choix, labo)
        print(labo)
        print()
        quitter = choix == 0

if __name__ == '__main__':
    main()
