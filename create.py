mots = open("mots.txt")

def plus_long():
    res = ''
    for mot in mots:
        if len(mot)>len(res):
            res = mot
    return len(res)


def fonc(taille_mot):
    with open(f'mots_{taille_mot}', 'w', encoding="utf-8") as f:
        for mot in mots: 
            if taille_mot == len(mot):
                f.write(mot + '\n')
    f.close()
    

for i in range(3):
    fonc(i)

mots.close()