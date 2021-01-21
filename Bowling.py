def calcule_score_jeu(indice_jeu, liste_jeux):
    somme_score_jeu_simple = liste_jeux[indice_jeu][0] + liste_jeux[indice_jeu][1]
    if jeu_est_un_spare(liste_jeux[indice_jeu]):
        return 10 + calcule_bonus_spare(indice_jeu, liste_jeux)
    elif jeu_est_un_strike(liste_jeux[indice_jeu]):
        return 10 + calcule_bonus_strike(indice_jeu, liste_jeux)
    else :
        return somme_score_jeu_simple


def calcule_score_partie(liste_jeux):
    somme_score_partie = 0
    for indice_jeu in range(10):
        somme_score_partie += calcule_score_jeu(indice_jeu, liste_jeux)
    return somme_score_partie


def jeu_est_un_spare(jeu):
    if jeu[0] + jeu[1] == 10 and jeu[0] != 10:
        return True
    return False


def calcule_bonus_spare(indice_jeu, liste_jeux):
    valeur_bonus_spare = liste_jeux[indice_jeu + 1][0]
    return valeur_bonus_spare


def jeu_est_un_strike(jeu):
    if jeu[0] == 10:
        return True
    return False


def calcule_bonus_strike(indice_jeu, liste_jeux):
    nb_strike_consecutif = 0
    while jeu_est_un_strike(liste_jeux[indice_jeu+nb_strike_consecutif]):
        if nb_strike_consecutif+indice_jeu+1 == len(liste_jeux):
            break
        else:
            nb_strike_consecutif += 1
    valeur_bonus_strike = 10 + liste_jeux[indice_jeu + nb_strike_consecutif][0]
    if nb_strike_consecutif == 1:
        return liste_jeux[indice_jeu + 1][0] + liste_jeux[indice_jeu + 1][1]
    return valeur_bonus_strike


