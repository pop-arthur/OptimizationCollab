import math

from objects.matrix import *


def intpoint(C, A, X, b, apac, alpha):
    while True:
        v = X.copy()
        D = X.diag()
        print("Initial X: ", X, "\n")
        print("Initial D: ", D, "\n")
        print("Initial v: ", v, "\n")
        input()
        print("Initial A: ", A, "\n")
        AA = A * D
        print("AA",AA, "\n") #fine output
        input()
        print("Initial C: ", C, "\n") #fine output
        CC = D * C
        print("CC",CC, "\n") #fine output
        input()
        F = AA * (AA.transpose())
        print("F",F, "\n") #fine output
        input()
        FI = F.inverse()
        print("FI",FI, "\n") #чёрт его знает, цифры страшные, мб работает
        input()
        H = (AA.transpose() * FI) * AA
        I = Matrix.identity(H.columns, H.columns)
        P = I - H
        Cp = P * CC

        nu = abs(min(Cp.numbers[0]))
        Cpmult = Cp.copy()
        coeff = (alpha / nu)
        for i in range(Cp.rows):
            for j in range(Cp.columns):
                Cpmult.numbers[i][j] = Cpmult.numbers[i][j] * coeff
        I = Cpmult.ones(rows=Cp.rows)  # I is equal to the elements from diagonal of Cpmult
        XX = I + Cpmult
        X = D * XX
        matr = X - v
        norm = math.sqrt((sum((x[0]) ** 2 for x in matr.numbers)))
        print(X)
        print(norm, "\n")
        if norm <= apac:
            break

    print("A vector of decision variables x* for alpha = ", alpha, ": \n", X, "\n")
