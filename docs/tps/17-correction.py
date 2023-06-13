def voisins(v, M):
    n = len(M)
    return [u for u in range(n) if M[u][v] == 1]


def parcoursEnLongueur(v, M):
    aVisiter = [v]
    dejaVus = [v]

    while len(aVisiter) > 0:
        u = aVisiter.pop()
        for w in voisins(u, M):
            if w not in dejaVus:
                dejaVus.append(w)
                aVisiter.append(w)

    return dejaVus


def parcoursEnLargeur(v, M):
    aVisiter = [v]
    dejaVus = [v]

    while len(aVisiter) > 0:
        u = aVisiter.pop(0)
        for w in voisins(u, M):
            if w not in dejaVus:
                dejaVus.append(w)
                aVisiter.append(w)

    return dejaVus


def connexe(M):
    return len(parcoursEnLongueur(0, M)) == len(M)


def fibonacci(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fibonacci(n-1) + fibonacci(n-2)


def parcours(v, M, dejaVus):
    for w in voisins(v, M):
        if not dejaVus[w]:
            dejaVus[w] = True
            parcours(w, M, dejaVus)
    return dejaVus


def chemins(M, v, n):
    if n == 0:
        return [[v]]
    rep = []
    for w in voisins(v, M):
        for chemin in chemins(M, w, n-1):
            rep.append([w] + chemin)
    return rep


def parcoursEnTroisTemps(v, M, couleur):
    """
    un sommet est soit pas vu (couleur 0), soit en train d'être vu (couleur 1),
    soit déjà vu (couleur 2)
    couleur est un tableau de longueur n donnant la couleur de chaque sommet
    la fonction renvoie None si elle trouve un cycle et couleur si elle ne trouve pas de cycle
    """

    couleur[v] = 1
    for w in voisins(v, M):
        if couleur[w] == 0:
            if parcoursEnTroisTemps(w, M, couleur) is None:
                return None
        elif couleur[w] == 1:
            return None
    couleur[v] = 2
    return couleur


def aUnCycle(M):
    couleur = [0 for _ in range(len(M))]
    for u in range(len(M)):
        if couleur[u] == 0:
            couleur = parcoursEnTroisTemps(u, M, couleur)
            if couleur is None:
                return True
    return False


M_diamant_0 = [
    [0, 1, 1, 0],
    [0, 0, 0, 1],
    [0, 0, 0, 1],
    [0, 0, 0, 0],
]

M_diamant_1 = [
    [0, 1, 1, 0],
    [0, 0, 1, 1],
    [0, 0, 0, 1],
    [0, 0, 0, 0],
]

M_diamant_2 = [
    [0, 1, 1, 0],
    [0, 0, 0, 1],
    [0, 1, 0, 1],
    [0, 0, 0, 0],
]

M_diamant_avec_cycle_0 = [
    [0, 1, 1, 0],
    [0, 0, 0, 1],
    [0, 0, 0, 1],
    [1, 0, 0, 0],
]

M_diamant_avec_cycle_1 = [
    [0, 1, 1, 0],
    [0, 0, 0, 1],
    [0, 0, 0, 1],
    [0, 1, 0, 0],
]

M_diamant_avec_cycle_2 = [
    [0, 1, 1, 0],
    [0, 0, 0, 1],
    [0, 0, 0, 1],
    [0, 0, 1, 0],
]

M_diamant_avec_cycle_3 = [
    [0, 1, 1, 0],
    [0, 0, 0, 1],
    [0, 0, 0, 1],
    [0, 0, 0, 1],
]


def main():
    assert not aUnCycle(M_diamant_0)
    assert not aUnCycle(M_diamant_1)
    assert not aUnCycle(M_diamant_2)

    assert aUnCycle(M_diamant_avec_cycle_0)
    assert aUnCycle(M_diamant_avec_cycle_1)
    assert aUnCycle(M_diamant_avec_cycle_2)
    assert aUnCycle(M_diamant_avec_cycle_3)


if __name__ == "__main__":
    main()
