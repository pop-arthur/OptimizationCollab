from typing import Tuple


class Vector: 
    """
    Class of vectors
    """
    def __init__(self, row=None):
        """
        You may initialise vector with known numbers - row, or without them
        """
        if row is None:
            self.row = []
        else:
            self.row = row
        self.numb_of_columns = len(self.row)

    def input(self):
        """
        Function to get user input and handle it. Parse input by itself
        """
        temp = input("Enter the vector (space-separated values): ")
        self.row = list(map(float, temp.split()))  # Convert input to list of floats
        self.numb_of_columns = len(self.row)
        return self

class Matrix:
    """
    Class of matrix
    """
    def __init__(self, matrix=None):
        """
        You may initialise vector with known numbers - matrix, or without them
        """
        if matrix is None:
            self.matrix = []
        else:
            self.matrix = matrix
        self.numb_of_rows = len(self.matrix)
        self.numb_of_columns = len(self.matrix[0]) if self.numb_of_rows > 0 else 0

    def input(self):
        """
        Function to get user input and handle it. Parse input by itself
        """
        print("Enter the matrix row by row (press Enter twice to stop):")
        matrix = []
        while True:
            temp = input()
            if temp == "":  # Stop input when user presses enter twice
                break
            row = list(map(float, temp.split()))  # Convert input row to list of floats
            matrix.append(row)
        self.matrix = matrix
        self.numb_of_rows = len(matrix)
        self.numb_of_columns = len(matrix[0]) if self.numb_of_rows > 0 else 0
        return self

def input_variables() -> Tuple[Vector, Matrix, Vector, float]:
    """
    Function to get all user input. Return all of data in classes and one - in float
    """
    print('First, enter a vector of coefficients for the objective function:')
    vcof = Vector().input()

    print('Now, enter a matrix of coefficients for the constraint function:')
    mccf = Matrix().input()

    print('Next, enter a vector of right-hand side numbers:')
    vrhsn = Vector().input()

    print('Lastly, enter the approximation accuracy:')
    apac = float(input())
    #for dev purpouse only. Delete before prod.
    print("Objective Function Coefficients:", vcof.row)
    print("Constraint Matrix:")
    for row in mccf.matrix:
        print(row)
    print("Right-Hand Side Vector:", vrhsn.row)
    print("Approximation Accuracy:", apac)
    #end of block to be deleted
    return vcof, mccf, vrhsn, apac

if __name__ == '__main__':
    input_variables()
    print("Welcome to Hell!")
