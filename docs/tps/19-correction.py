from turtle import forward, right, left, begin_fill, end_fill


def polygon(n, L):
    for _ in range(n):
        forward(L)
        left(360/n)


def level1():
    polygon(4, 100)


def level2():
    for n in range(3, 9):
        polygon(n, 100)


def level3():
    def sierpinsky(n, L):
        if n == 1:
            begin_fill()
            polygon(3, L)
            end_fill()
        else:
            sierpinsky(n-1, L/2)
            forward(L/2)
            sierpinsky(n-1, L/2)
            left(120)
            forward(L/2)
            right(120)
            sierpinsky(n-1, L/2)
            right(120)
            forward(L/2)
            left(120)

    sierpinsky(5, 200)


def level4():
    def hilbertCurveDirect(n, L):
        if n == 1:
            forward(L/2)
            right(90)
            forward(L/2)
            right(90)
            forward(L/2)
        else:
            step = L / 2**n
            right(90)
            hilbertCurveIndirect(n-1, L/2)
            right(90)
            forward(step)
            hilbertCurveDirect(n-1, L/2)
            left(90)
            forward(step)
            left(90)
            hilbertCurveDirect(n-1, L/2)
            forward(step)
            right(90)
            hilbertCurveIndirect(n-1, L/2)
            right(90)

    def hilbertCurveIndirect(n, L):
        if n == 1:
            forward(L/2)
            left(90)
            forward(L/2)
            left(90)
            forward(L/2)
        else:
            step = L / 2**n
            left(90)
            hilbertCurveDirect(n-1, L/2)
            left(90)
            forward(step)
            hilbertCurveIndirect(n-1, L/2)
            right(90)
            forward(step)
            right(90)
            hilbertCurveIndirect(n-1, L/2)
            forward(step)
            left(90)
            hilbertCurveDirect(n-1, L/2)
            left(90)

    hilbertCurveDirect(5, 200)
