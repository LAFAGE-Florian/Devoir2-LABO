'''
PARTIE MENU 
'''
import laboratoire

# importer les exceptions

def afficher_menu(): 
    print("1. Enregistrer l'arrivée d'une nouvelle personne.")
    print("2. Enregistrer le départ d'une personne.")
    print("3. Modifier le bureau occuper par une personne.")
    print("4. Changer le nom d'une personne.")
    print("5. Savoir si une personne est membre du laboratoire.")
    print("6. Obtenir le bureau d'une personne.")
    print("7. Produire le listing de tous le personnles avec le bureau occupé.")
    print("0. Quitter.")

def menu(): 
    while True: 
        afficher_menu()
        choix = input("Entrer votre choix: ")
        if choix == '1': 
            nom = input("Nom de la personne: ")
            bureau = input("Numéro du bureau: ")
            try:
                labo.enregistrer_arrivee(nom, bureau)
                print(f"{nom} ajouté au bureau {bureau}.")
            except PresentException:
                print(f'')
        elif choix == '2': 
            nom = input("Nom de la personne: ")
            try: 
                labo.enregister_depart(nom)
                print(f"{nom} a été supprimé")
            except AbsentException:
                print(f'')
        elif choix == '3':
            nom = input("Nom de la personne: ")
            nouveau_bureau = input("Numéro du nouveau bureau: ")
            try:
                labo.modifier_bureau(nom, nouveau_bureau)
            except AbsentException:
                print(f'')
        elif choix == '4':
            nom_actuel = input("Nom de la personne: ")
            nouveau_nom = input("Nouveau nom de la personne: ")
            try: 
                labo.modifier_nom(nom_actuel, nouveau_nom)
            except AbsentException: 
                print(f'')
        elif choix == '5':
            nom = input("Nom de la personne: ")
            if labo.est_membre(nom):
                print(f'{nom} est présent.e dans le laboratoire')
            else : 
                print(f"{nom} n'est pas présent.e dans le laboratoire")
        elif choix == '6':
            nom = input('Nom de la personne: ')  
            try : 
                labo.obtenir_bureau(nom)
            except AbsentException:
                print(f'')
        elif choix == '7':
            personnel = labo.liste_personnel()
            for nom, bureau in personnel:
                print(f"{nom} - bureau : {bureau}")
        elif choix == '0':
                print(f'Au revoir...') 
                break
        else: 
            print('Choix invalide.')