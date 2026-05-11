from itertools import product
from enum import Enum
from collections import defaultdict
import math
import random

class Couleurs(Enum):
    B = 0 # Noir/Gris
    J = 1 # Jaune
    V = 2 # Vert

def creer_dict():
    mots_de_longueurs = defaultdict(list)
    try:
        with open("mots.txt", "r", encoding="utf-8") as f:
            for line in f:
                mot = line.strip().upper() # On normalise en majuscules
                if mot:
                    mots_de_longueurs[len(mot)].append(mot)
    except FileNotFoundError:
        print("Erreur : mots.txt introuvable.")
    return mots_de_longueurs

def verifier(solution, essai):
    """Calcule le score exact (Vert, Jaune, Gris) avec la priorité aux Verts."""
    taille = len(solution)
    res = [Couleurs.B] * taille
    sol_list = list(solution)
    ess_list = list(essai)

    # 1ère passe : Les Verts
    for i in range(taille):
        if ess_list[i] == sol_list[i]:
            res[i] = Couleurs.V
            sol_list[i] = None # On "consomme" la lettre
            ess_list[i] = None

    # 2ème passe : Les Jaunes
    for i in range(taille):
        if ess_list[i] is not None and ess_list[i] in sol_list:
            res[i] = Couleurs.J
            sol_list[sol_list.index(ess_list[i])] = None
            
    return tuple(res)


# VERSION 2 
def calculer_entropie(essai, mots_valables):
    """Calcule l'entropie selon la formule H(X) = -sum(p * log2(p))"""
    distributions = defaultdict(int)
    for mot in mots_valables:
        score = verifier(mot, essai)
        distributions[score] += 1
    
    entropie = 0
    total = len(mots_valables)
    for count in distributions.values():
        p = count / total
        entropie -= p * math.log2(p)
    return entropie

def meilleur_essai(mots_valables, mots_possibles):
    if len(mots_valables) == 1:
        return mots_valables[0]
        
    best_mot = ""
    max_h = -1
    
    for essai in mots_possibles:
        h = calculer_entropie(essai, mots_valables)
        if h > max_h:
            max_h = h
            best_mot = essai
    return best_mot

def wordle_game(taille_mot, nb_essais):
    dico = creer_dict()
    mots_possibles = dico[taille_mot]
    
    if not mots_possibles:
        return "Aucun mot de cette taille trouvé."

    mots_valables = list(mots_possibles)
    solution = random.choice(mots_valables)
    
    print(f"La solution (cachée) est : {solution}")
    
    for i in range(nb_essais):
        essai = meilleur_essai(mots_valables, mots_possibles)
        score = verifier(solution, essai)
        
        print(f"Essai {i+1}: {essai} -> {score}")
        
        if essai == solution:
            return f"Gagné en {i+1} coups !"
            
        # Filtrage des mots restants
        mots_valables = [m for m in mots_valables if verifier(m, essai) == score]
        print(mots_valables)
        
    return f"Perdu... Le mot était {solution}"

def main():
    print(wordle_game(4, 6))

if __name__ == '__main__':
    main()