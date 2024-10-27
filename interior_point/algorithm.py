from objects.matrix import *

def intpoint(C, A, X, b, apac, alpha):
    i = 1
    while True:
        D = X.diag()
        AA = A * D
        CC = D * C
        F = AA * (AA.transpose())
        FI = F.inverse()
        H = (AA.transpose() * FI) * AA
        I = Matrix(H.columns, H.columns).identity()
        P = I - H
        Cp = P * CC
        nu = abs(min(Cp.numbers[0]))
        Cpmult = Cp
        coeff=(alpha / nu)
        for i in range (Cp.rows):
            for j in range(Cp.columns):
                Cpmult.numbers[i][j]=Cpmult.numbers[i][j]*coeff

        print(Cpmult)
        I = Cpmult.ones(Cp.rows, 1)
        print(I)
        XX = I + Cpmult
        X = D * XX

        # check if the algorithm is complete
        ind = 0
        for i in X:
            if i < 0:
                ind += 1
        if i == 0:
            break

    print("A vector of decision variables x* for alpha = ", alpha, ": ", X, "\n")
