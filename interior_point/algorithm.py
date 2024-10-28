import math

from objects.matrix import *


def intpoint(C, A, X, b, apac, alpha):
    while True:
        v = X.copy()
        D = X.diag()
        AA = A * D
        CC = D * C
        F = AA * (AA.transpose())
        FI = F.inverse()
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
