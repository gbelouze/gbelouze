from math import floor
from matplotlib.pyplot import bar, show
from numpy.random import rand
import numpy as np


def bernoulli(p):
    if rand() < p:
        return 1
    else:
        return 0


def uniformInt(a, b):
    n = b - a
    x = rand()

    for k in range(n):
        # est-ce x ∈ [k/n, k+1/n] ?
        if k/n <= x < (k+1)/n:
            return a + k


def uniformIntOneLine(a, b):
    a + int(floor(rand() * (b-a)))


def loiUniformInt(a, b, k):
    '''ℙ(X=k)'''
    n_simulations = 1_000
    count = 0
    for _ in range(n_simulations):
        if k == uniformInt(a, b):
            count += 1
    return count / n_simulations


def test_loiUniformInt():
    a, b = 10, 20
    X = np.arange(a, b)
    Y = [loiUniformInt(a, b, k) for k in range(a, b)]

    bar(X, Y)
    show()


def binomial(n, p):
    ret = 0
    for _ in range(n):
        ret += bernoulli(p)
    return ret


def loiBinomial(n, p, k, N):
    '''ℙ(X=k)'''
    count = 0
    for _ in range(N):
        if k == binomial(n, p):
            count += 1
    return count / N


def test_loiBinomial():
    n = 30
    p = 1/2
    N = 10_000

    X = np.arange(n)
    Y = [loiBinomial(n, p, k, N) for k in range(n)]
    bar(X, Y)
    show()
