from input_vars import input_vars
from algorithm import intpoint
from objects import *
from simplex_method.main import simplex_method

#Do we actually need code in comments?
# A = Matrix(3,3,[[1, 2, 3], [0, 1, 4], [0, 0, 1]])
# print(A)
# print()
# print(A.inverse())
vcof, mccf, inix, vrhsn, apac = input_vars()
intpoint(vcof, mccf, inix, vrhsn, apac, 0.5)
intpoint(vcof, mccf, inix, vrhsn, apac, 0.9)
simplex_method(vcof, mccf, vrhsn, apac)
