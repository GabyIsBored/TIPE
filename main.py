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

def verifier(mot, tent, taille_mot):
    score = [Couleurs.B] * taille_mot
    lettres_mot = list(mot)
    
    # 1er passage : on fixe les Verts (prioritaires)
    for i in range(taille_mot):
        if tent[i] == mot[i]:
            score[i] = Couleurs.V
            lettres_mot[i] = None 
            
    # 2ème passage : on fixe les Jaunes
    for i in range(taille_mot):
        if score[i] == Couleurs.B and tent[i] in lettres_mot:
            score[i] = Couleurs.J
            lettres_mot[lettres_mot.index(tent[i])] = None 
            
    return tuple(score)

def mots_selon_couleur(essai, code_couleur, mots_valables):
    taille_mot = len(essai)
    # implementation fais trois tableaux pour trois boucles. CT = 2 * taile_mot * n    
    return [mot for mot in mots_valables if verifier(mot, essai, taille_mot) == code_couleur]

    

def meilleur_essai(mots_valables): 

    if len(mots_valables) == 1:
        return mots_valables[0]
    
    mot_max = '' 
    max_entropie = 0

    for essai in mots_valables:
        curr_entropie = 0
        for etat in list(product(Couleurs, repeat=len(mots_valables[0]))):
            p = len(mots_selon_couleur(essai, etat, mots_valables)) / len(mots_valables)
            if p > 0:
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

    print('Initialisation finie...')

    solution = random.choice(mots_valables)

    print('La solution est: ', solution)

    etat_gagne =  tuple([Couleurs.V] * taille_mot)
    while nb_essais > 0:
        
        # Amelioration possible: Table de hachage
        essai = meilleur_essai(mots_valables)
        etat = wordle_essai(solution, essai)

        mots_valables = mots_selon_couleur(essai,etat,mots_valables)

        print(essai, etat, mots_valables)

        if etat == etat_gagne:
            return 'Gagne!'
        nb_essais -= 1
        
        

    return f'Perdu... Le mot etait {solution}'

print(wordle_game(4, 6))
