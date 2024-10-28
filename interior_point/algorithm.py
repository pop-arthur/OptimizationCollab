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
        arr = []
        for i in Cp.numbers:
            arr.append(i[0])
        nu = abs(min(arr))
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
        if norm <= apac:
            break

    print("A vector of decision variables x* for alpha = ", alpha, ": \n", X, "\n")
    C.transpose()
    X.transpose()
    value=0
    for i in range (C.rows):
            value+=C.numbers[i][0]*X.numbers[i][0]
    print("Maximum/minimum value of the objective function for alpha = ", alpha, ": ", value, "\n")