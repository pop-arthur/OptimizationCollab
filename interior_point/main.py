from utils.input_vars import input_vars
from utils.algorithm import intpoint
from objects import *
from utils.simplex_method.main import simplex_method
from utils.simplex_method import objects as obj

#Very needed comments bellow
"""
**Prayer for Functional Code**

O Divine Architect of all logic and order,  
Grant me clarity as I navigate through lines of code.  
May my syntax be sound, and my logic true,  
So that my work flows smoothly, aligned with purpose.

Bless my functions to return as they should,  
My loops to iterate precisely, without endless cycles,  
And my variables to hold firm their intended values.  
Guard against elusive bugs and mysterious errors,  
And give me patience to debug with grace.

Guide my hands and mind to craft clean, readable code,  
And may this work serve others well, with efficiency and care.  
In every line, may there be order and harmony.  
Amen.
"""
#Prayer written by a ChatGPT
#Read it loud before every run of the code.


def to_vector(matrix: Matrix, index: int, by_row: bool = True) -> 'obj.Vector':
    """
    Converts a matrix row or column to a Vector from Simplex method.
    """
    if (matrix.numbers is None or len(matrix.numbers) == 0 or len(matrix.numbers[0]) == 0):
        return obj.Vector()
    if (matrix.columns > 1 and matrix.rows > 1):
        raise ValueError("Error: Input matrix is not Vector.")
    matrix = matrix.transpose() if by_row else matrix  # Transpose the matrix for column-major indexing.
    return obj.Vector(matrix.numbers[index])


def to_Matrix(matrix: Matrix) -> 'obj.Matrix':
    """
    Converts a Matrix to a Matrix from Simplex method.
    """
    return obj.Matrix(matrix.numbers)


#Do we actually need code in comments?
# A = Matrix(3,3,[[1, 2, 3], [0, 1, 4], [0, 0, 1]])
# print(A)
# print()
# print(A.inverse())
vcof, mccf, inix, vrhsn, apac = input_vars()
intpoint(vcof, mccf, inix, vrhsn, apac, 0.5)
intpoint(vcof, mccf, inix, vrhsn, apac, 0.9)
#Change params of function bellow somehow

simplex_method(to_vector(vcof, 0), to_Matrix(mccf), to_vector(vrhsn, 0), apac) #TODO: Correct the input arguments to the simplex_method classes. It should be Vector, Matrix, Vector, and float.
