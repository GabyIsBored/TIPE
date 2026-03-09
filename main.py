def wordle_essai(solution, essai):
    occurences = {}
    res = []
    
    for lettre in solution:
        occurences[lettre] = occurences.get(lettre, 0) + 1
    
    for i in range(len(essai)):
        lettre = essai[i]
        if occurences.get(lettre, 0) > 0:
            if solution[i] == lettre:
                res.append("vert")
            else:
                 res.append("jaune")
            occurences[lettre] -= 1
        else:
             res.append("blanc")
    return res


def wordle_game(taille_mot, nb_essais, solution):
    win =  ["vert" for i in range(taille_mot)]
    while nb_essais > 0:
        essai = input('Faire un essai')
        if (len(essai) != taille_mot):
            return 'Erreur'
        state = wordle_essai(solution, essai)
        print(state);
        if state == win:
            return 'Win!'
        nb_essais -= 1
    return 'Lost...'

wordle_game(5, 6, 'sourd')

TEST TEST TEST