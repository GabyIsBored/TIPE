from pprint import pprint
import random 

B=0
J=1
V=2

def creer_dict():
    mots_de_longueurs = dict()
    with open("mots.txt") as f:
        les_mots = f.readlines()
        for mot in les_mots:
            mots_de_longueurs[len(mot)] = []
        for mot in les_mots:
            mots_de_longueurs[len(mot)].append(mot[:-1])
    return mots_de_longueurs

def wordle_essai(solution, essai):
    occurences = {}
    res = []
    
    for lettre in solution:
        occurences[lettre] = occurences.get(lettre, 0) + 1
    
    for i in range(len(essai)):
        lettre = essai[i]
        if occurences.get(lettre, 0) > 0:
            if solution[i] == lettre:
                res.append(V)
            else:
                 res.append(J)
            occurences[lettre] -= 1
        else:
             res.append(B)
    return res

def wordle_game(taille_mot, nb_essais):
    if taille_mot < 2: 
        return "Parametre invalide: Taille mot trop petite!"
  
    mots_de_longueurs = creer_dict()
    mots_valables = mots_de_longueurs[taille_mot + 1]

    solution = random.choice(mots_valables)

    etat_gagne =  [V] * taille_mot
    while nb_essais > 0:
        
        # Amelioration possible: Table de hachage
        essai = input('Faire un essai: ').upper()
        if essai not in mots_valables: 
            print('Pas un mot valable!')
            nb_essais += 1
        # -------------------------------

        etat = wordle_essai(solution, essai)
        print(etat)
        if etat == etat_gagne:
            return 'Gagne!'
        nb_essais -= 1
    return f'Perdu... Le mot etait {solution}'

# -----------------------------------------------------------------------------------------------------------------------------------------
print(wordle_game(5, 6))

def generer_couleurs(): # liste des combinaisons possibles
    return

def mots_selon_couleur(essai): # liste des mots possibles selon les couleurs donnes par un essai 
    # Partie redondante si mots_valables passe en argument 
    taille_mot = len(essai)

    if taille_mot < 2: 
        return "Parametre invalide: Taille mot trop petite!"
    
    mots_de_longueurs = creer_dict()
    mots_valables = mots_de_longueurs[taille_mot + 1]
    # -----------------------------------------------------

    mots_possibles = mots_valables
    couleurs = [B, B, B, B, B]
    mots_contraintes = []

    for mot in mots_possibles:
        couleurs_test = wordle_essai(mot,essai)
        for i in range(taille_mot):
            if couleur_lettre[] == couleurs_test[]:
                


    return

def calcul_entropie():  
    return
