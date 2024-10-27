from objects.matrix import *

def intpoint(C, A, X, b, apac, alpha):
    i = 1
    while True:
        D = X.diag()
        print('D: ', D)
        AA = A * D
        print('AA: ', AA)
        CC = D * C
        I = Matrix(X.columns, X.columns).identity()
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
