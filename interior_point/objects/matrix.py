from typing import Optional


class Matrix:
    """
    Class of matrix
    """

    def __init__(self, matrix: Optional['Matrix'] = None):
        """
        initialisation of matrix

        :param matrix: Known matrix to be equal with new matrix
        """
        if matrix is None:
            self.matrix = []
        else:
            self.matrix = matrix
        self.numb_of_rows = len(self.matrix)
        self.numb_of_columns = len(self.matrix[0]) if self.numb_of_rows > 0 else 0


    def input(self) -> 'Matrix':
        """
        Function to get user input and handle it. Parse input by itself
        :return: Matrix with user input
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
    

    def transpose(self) -> 'Matrix':
        """
        Function to transpose matrix

        :return: Transpose of matrix
        """
        result = Matrix(self.columns, self.rows)
        for i in range(self.rows):
            for j in range(self.columns):
                result.numbers[j][i] = self.numbers[i][j]
        return result
    

    def inverse(self):
        #TODO write
        pass


    def __add__(self, other: 'Matrix') ->  'Matrix':
        """
        Adds two matrices and returns a new Matrix object.
        
        :param other: Another matrix to add to this one.
        :return: A new matrix containing the sum of both matrices.
        """
        if self.rows == other.rows and self.columns == other.columns:
            result = Matrix(self.rows, self.columns)
            for i in range(self.rows):
                for j in range(self.columns):
                    result.numbers[i][j] = self.numbers[i][j] + other.numbers[i][j]
            return result
        else:
            raise ValueError("Error: the dimensional problem occurred")
    

    def __sub__(self, other):
        if self.rows == other.rows and self.columns == other.columns:
            result = Matrix(self.rows, self.columns)
            for i in range(self.rows):
                for j in range(self.columns):
                    result.numbers[i][j] = self.numbers[i][j] - other.numbers[i][j]
            return result
        else:
            raise ValueError("Error: the dimensional problem occurred")

    
    def __mul__(self, other):
        if self.columns == other.rows:
            result = Matrix(self.rows, other.columns)
            for i in range(self.rows):
                for j in range(other.columns):
                    result.numbers[i][j] = sum(self.numbers[i][k] * other.numbers[k][j] for k in range(self.columns))
            return result
        else:
            raise ValueError("Error: the dimensional problem occurred")
        
    
    def diag(self) -> 'Matrix': 
        """
        Function to get diagonal of matrix.

        :return: A new matrix with elements only on the diagonal
        """
        res = []
        for i in range(self.numb_of_columns):
            row  = []
            for  j  in range(self.numb_of_rows):
                if (i==j):
                    row.append(self.matrix[i][j])
                else:
                    row.append(0)
            res.append(row)
        return Matrix(res)
    

    def det(self):
        if (self.numb_of_columns != self.numb_of_rows):
            raise ValueError("Matrix must be squared to find determinant")
        temp = [row[:] for row in self.numbers]
        n = len(temp)
        det = 1
        for i in range(n):
            pivot = i
            for j in range(i + 1, n):
                if abs(temp[j][i]) > abs(temp[pivot][i]):
                    pivot = j
            if pivot != i:
                temp[i], temp[pivot] = temp[pivot], temp[i]
                det *= -1

            if temp[i][i] == 0:
                return 0

            for j in range(i + 1, n):
                factor = temp[j][i] / temp[i][i]
                for k in range(i, n):
                    temp[j][k] -= factor * temp[i][k]

        for i in range(n):
            det *= temp[i][i]
        return det

    def __repr__(self) -> str:
        """
        Function to make string output from data in instance of class

        :return: string with data and formating
        """
        return f"{self.matrix}"


    @staticmethod
    def identity(size:int) -> 'Matrix':
        """
        Function to return identity matrix of needed size.

        :param size: Size of identity matrix
        :return: A new identity matrix
        """
        res = []
        for i in range(size):
            row  = []
            for  j  in range(size):
                if (i==j):
                    row.append(1)
                else:
                    row.append(0)
            res.append(row)
        return Matrix(res)