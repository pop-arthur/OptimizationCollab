from input_vars import input_vars
from algorithm import intpoint
from objects import *
from utils.simplex_method.main import simplex_method
from simplex_method.objects import Vector, Matrix
#Do we actually need code in comments?
# A = Matrix(3,3,[[1, 2, 3], [0, 1, 4], [0, 0, 1]])
# print(A)
# print()
# print(A.inverse())
vcof, mccf, inix, vrhsn, apac = input_vars()
intpoint(vcof, mccf, inix, vrhsn, apac, 0.5)
intpoint(vcof, mccf, inix, vrhsn, apac, 0.9)
#Change params of function bellow somehow
simplex_method(vcof.to_vector(), mccf, vrhsn.to_vector(), apac) #TODO: Correct the input arguments to the simplex_method classes. It should be Vector, Matrix, Vector, and float.
