from objects.matrix import *

def intpoint(C, A, X, b, apac, alpha):
    while True:
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
        Cpmult = Cp
        coeff=(alpha / nu)
        for i in range (Cp.rows):
            for j in range(Cp.columns):
                Cpmult.numbers[i][j]=Cpmult.numbers[i][j]*coeff

        print(Cpmult)
        I = Cpmult.ones(rows=Cp.rows) #I is equal to the elements from diagonal of Cpmult
        print(I)
        XX = I + Cpmult
        X = D * XX

        # check if the algorithm is complete
        ind = 0
        for i in X: #go through each row of X
            for j in i: #go through each element in the row
                if j < 0: 
                    ind += 1 #increment index if element is negative
        if ind == 0: # if no negative elements found, algorithm is complete
            break

    print("A vector of decision variables x* for alpha = ", alpha, ": ", X, "\n")
