from interior_point.objects.matrix import *

def intpoint(C, A, X, b, apac, alpha):
    i = 1
    while True:
        emptyMatrix = Matrix(X.columns, X.columns)
        print(emptyMatrix)
        print(X.columns)
        print(X)
        D = emptyMatrix.identity() * X
        AA = A * D
        CC = D * C
        I = emptyMatrix.identity()
        F = AA * (AA.transpose())
        FI = F.inverse()
        H = (AA * FI) * AA
        P = I - H
        Cp = P * CC
        nu = abs(min(Cp.numbers[0]))
        XX = I + ((alpha / nu) * Cp)
        X = D * XX

        # check if the algorithm is complete
        ind = 0
        for i in X:
            if i < 0:
                ind += 1
        if i == 0:
            break

    print("A vector of decision variables x* for alpha = ", alpha, ": ", X, "\n")
