from interior_point.input_vars import input_vars
from interior_point.algorithm import intpoint
from objects import *
# A = Matrix(3,3,[[1, 2, 3], [0, 1, 4], [0, 0, 1]])
# print(A)
# print()
# print(A.inverse())
vcof, mccf, inix, vrhsn, apac = input_vars()
intpoint(vcof, mccf, inix, vrhsn, apac, 0.5)
intpoint(vcof, mccf, inix, vrhsn, apac, 0.9)

