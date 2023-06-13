import numpy as np


def liste_to_matrice(L):
    n = len(L)
    M = np.zeros((n, n))

    for i, voisins in enumerate(L):
        for j in voisin:
            M[i, j] = 1

    return M


def matrice_to_liste(M):
    n = len(M)
    L = []

    for i in range(n):
        voisins_de_i = []
        for j in range(n):
            if M[i, j] == 1:
                voisins_de_i.append(j)
        L.append(voisins_de_i)

    return L


def ajoute_noeud(M):
    n = len(M)
    new_M = np.zeros((n+1, n+1))
    new_M[:n, :n] = M
    return new_M


def supprime_noeud(M, v):
    n = len(M)
    new_M = np.zeros((n-1, n-1))
    new_M[:v, :v] = M[:v, :v]
    new_M[v:, :v] = M[v+1:, :v]
    new_M[:v, v:] = M[:v, v+1:]
    new_M[v:, v:] = M[v+1:, v+1:]
    return new_M


def ajoute_arete(M, v1, v2):
    M[v1, v2] = 1
    M[v2, v1] = 1


def supprime_arete(M, v1, v2):
    M[v1, v2] = 0
    M[v2, v1] = 0


def voisins(v, M):
    return [w for w in range(len(M)) if M[v][w]]


def parcours(v, M, dejaVus):
    dejaVus[v] = True
    for w in voisins(v, M):
        parcours(w, M, dejaVus)
    return dejaVus


def est_connexe(M):
    n = len(M)
    return all(parcours(0, M, [False for _ in range(n)]))


def parcoursEnProfondeur(v, M):
    n = len(M)
    aVisiter = [v]
    dejaVus = [i == v for i in range(n)]

    while aVisiter:
        u = aVisiter.pop()
        for w in voisins(u, M):
            if not dejaVus[w]:
                aVisiter.append(w)
                dejaVus[w] = True
    return dejaVus
