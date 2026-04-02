from pprint import pprint
import random 
from itertools import product
from enum import Enum
from collections import defaultdict
import math 

class Couleurs(Enum):
    B = 0
    J = 1
    V = 2

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
                res.append(Couleurs.V)
            else:
                 res.append(Couleurs.J)
            occurences[lettre] -= 1
        else:
             res.append(Couleurs.B)
    return tuple(res)

# -----------------------------------------------------------------------------------------------------------------------------------------
# print(wordle_game(5, 6))

def mots_selon_couleur(essai, code_couleur, mots_valables):
    # idee 1: Faire la fonction inverse de wordle essai (brute force)
    
    occurences = {}
    res = []

    for l in range(len(essai)):
        if code_couleur[l] == Couleurs.J:
            occurences[essai[l]] = occurences.get(essai[l], 0) + 1
            
    for i in range(len(mots_valables)):
        mot = mots_valables[i]
        for j in range(len(code_couleur)):
            statement = not ((code_couleur[j] == Couleurs.V and not mot[j] == essai[j]) or (code_couleur[j] == Couleurs.J and mot[j] == essai[j]) or (occurences.get(mot[j], 0) == 0))
            if statement:
                    res.append(mot)
                    break
            else: 
                occurences[mot[j]] = occurences.get(mot[j], 1) - 1                     

    return res

    

def meilleur_essai(mots_valables): 
    mot_max = '' 
    max_entropie = 0

    for essai in mots_valables:
        curr_entropie = 0
        for etat in list(product(Couleurs, repeat=len(mots_valables[0]))):
            p = len(mots_selon_couleur(essai, etat, mots_valables)) / len(mots_valables)
            curr_entropie += -p * math.log2(p)

        if curr_entropie > max_entropie:
            mot_max = essai
            max_entropie = curr_entropie
        
    return mot_max


def wordle_game(taille_mot, nb_essais):
    if taille_mot < 2: 
        return "Parametre invalide: Taille mot trop petite!"
  
    mots_de_longueurs = creer_dict()
    mots_valables = mots_de_longueurs[taille_mot + 1]

    solution = random.choice(mots_valables)
    print(solution)
    etat_gagne =  tuple([Couleurs.V] * taille_mot)
    while nb_essais > 0:
        
        # Amelioration possible: Table de hachage
        essai = meilleur_essai(mots_valables)
        print(essai)
        etat = wordle_essai(solution, essai)

        mots_valables = mots_selon_couleur(essai,etat,mots_valables)

        if etat == etat_gagne:
            return 'Gagne!'
        nb_essais -= 1
        
        print(essai, etat, mots_valables)

    return f'Perdu... Le mot etait {solution}'

print(wordle_game(3, 5))