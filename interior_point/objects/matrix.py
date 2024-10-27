from typing import Union


class Matrix:
    """
    An ultimate solution for linear algebra problems.\n
    Class of matrices where you can perform operations like addition, subtraction, multiplication, transpose, find the determinant, inverse, etc.
    """


    def __init__(self, rows:int=0, cols:int=0, numbers=None):
        """
        Initializes a matrix with the given dimensions and values.
        """
        self.rows = rows
        self.columns = cols
        if numbers:
            self.numbers = numbers
        else:
            self.numbers = [[0 for _ in range(cols)] for _ in range(rows)]


    def __sub__(self, other:'Matrix') -> 'Matrix':
        """
        Subtracts another matrix from this matrix.
        """
        if self.rows == other.rows and self.columns == other.columns:
            result = Matrix(self.rows, self.columns)
            for i in range(self.rows):
                for j in range(self.columns):
                    result.numbers[i][j] = self.numbers[i][j] - other.numbers[i][j]
            return result
        else:
            raise Exception("Error: the dimensional problem occurred")


    def __add__(self, other: 'Matrix') -> 'Matrix':
        """
        Adds this matrix with another matrix.
        """
        if self.rows == other.rows and self.columns == other.columns:
            result = Matrix(self.rows, self.columns)
            for i in range(self.rows):
                for j in range(self.columns):
                    result.numbers[i][j] = self.numbers[i][j] + other.numbers[i][j]
            return result
        else:
            raise Exception("Error: the dimensional problem occurred")
    

    def __mul__(self, other: Union['Matrix', int, float]) -> 'Matrix':
        """
        Multiplies this matrix with another matrix or a scalar.
        """
        if (isinstance(other, Matrix)):
            if self.columns == other.rows:
                result = Matrix(self.rows, other.columns)
                for i in range(self.rows):
                    for j in range(other.columns):
                        result.numbers[i][j] = sum(self.numbers[i][k] * other.numbers[k][j] for k in range(self.columns))
                return result
            else:
                print("\n \n\ n")
                print("Matrix dimensions are not compatible for multiplication: ")
                print(self, '\n___\n', other)
                print(self.columns, other.rows, "Cannot multiply these matrices" )
                raise Exception("Error: the dimensional problem occurred")
        elif (isinstance(other, int) or isinstance(other, float)):
            result = Matrix(self.rows, self.columns)
            for i in range(self.rows):
                for j in range(self.columns):
                    result.numbers[i][j] = self.numbers[i][j] * other
            return result
        else:
            raise Exception("Error: trying to multiply a matrix with a wrong type")


    def __rmul__(self, other: Union[int, float]) -> 'Matrix':
        if (isinstance(other, int) or isinstance(other, float)):
            result = Matrix(self.rows, self.columns)
            for i in range(self.rows):
                for j in range(self.columns):
                    result.numbers[i][j] = self.numbers[i][j] * other
            return result
        else:
            raise Exception("Error: trying to multiply a matrix with a wrong type")


    def transpose(self) -> 'Matrix':
        """
        Returns the transpose of this matrix.
        """
        result = Matrix(self.columns, self.rows)
        for i in range(self.rows):
            for j in range(self.columns):
                result.numbers[j][i] = self.numbers[i][j]
        return result


    def determinant(self) -> float:
        """
        Returns the determinant of this matrix.
        """
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


    def identity(self) -> 'Matrix':
        """
        Returns an identity matrix of the same size as this matrix.
        """
        if self.rows != self.columns:
            raise Exception("Error: Identity matrix must be square.")
        identity_matrix = Matrix(self.rows, self.rows)
        for i in range(self.rows):
            identity_matrix.numbers[i][i] = 1
        return identity_matrix


    @staticmethod
    def identity(rows:int, columns:int) -> 'Matrix':
        """
        Returns an identity matrix of the same size as this matrix.
        """
        if rows != columns:
            raise Exception("Error: Identity matrix must be square.")
        identity_matrix = Matrix(rows, rows)
        for i in range(rows):
            identity_matrix.numbers[i][i] = 1
        return identity_matrix
    

    def nullify(self, row:int, col:int, row_to_start:int) -> None:
        """
        Nullifies the specified row and column in this matrix.
        """
        row -= 1
        col -= 1
        for j in range(row_to_start, self.rows):
            if j != row:
                if self.numbers[row][col] != 0 and self.numbers[j][col] != 0:
                    multiplier = self.numbers[row][col] / self.numbers[j][col]
                    for i in range(self.columns):
                        self.numbers[row][i] -= self.numbers[j][i] * multiplier


    def exchange(self, i1:int, i2:int) -> None:
        """
        Exchanges the rows at the specified indices in this matrix.
        """
        i1 -= 1
        i2 -= 1
        if i1 < self.rows and i2 < self.rows:
            self.numbers[i1], self.numbers[i2] = self.numbers[i2], self.numbers[i1]
        else:
            raise Exception("Error: Index out of bounds.")


    def inverse(self) -> 'Matrix':
        """
        Returns the inverse of this matrix.
        """
        if self.rows != self.columns:
            raise Exception("Error: Matrix must be square for inversion.")

        temp = Matrix(self.rows, self.columns, [row[:] for row in self.numbers])
        identity_matrix = self.identity()
        n = temp.rows

        for i in range(n):
            pivot = i
            for j in range(i + 1, n):
                if abs(temp.numbers[j][i]) > abs(temp.numbers[pivot][i]):
                    pivot = j

            if pivot != i:
                temp.exchange(i + 1, pivot + 1)
                identity_matrix.exchange(i + 1, pivot + 1)

            for j in range(i + 1, n):
                if temp.numbers[j][i] != 0:
                    factor = temp.numbers[j][i] / temp.numbers[i][i]
                    for k in range(n):
                        temp.numbers[j][k] -= factor * temp.numbers[i][k]
                        identity_matrix.numbers[j][k] -= factor * identity_matrix.numbers[i][k]

        for i in range(n - 1, -1, -1):
            for j in range(i - 1, -1, -1):
                if temp.numbers[j][i] != 0:
                    factor = temp.numbers[j][i] / temp.numbers[i][i]
                    for k in range(n):
                        temp.numbers[j][k] -= factor * temp.numbers[i][k]
                        identity_matrix.numbers[j][k] -= factor * identity_matrix.numbers[i][k]

        for i in range(n):
            div = temp.numbers[i][i]
            for j in range(n):
                temp.numbers[i][j] /= div
                identity_matrix.numbers[i][j] /= div

        return identity_matrix


    def diag(self) -> 'Matrix':
        """
        Returns a new matrix with the elements from vector on diagonal. Or vector with elements from diagonal of matrix.
        """
        if (self.rows > self.columns and self.columns == 1):
            new_matrix = Matrix(self.rows, self.rows)
            for i in range(self.rows):
                new_matrix.numbers[i][i] = self.numbers[i][0]
            return new_matrix
        elif (self.rows < self.columns and self.columns == 1):
            new_matrix = Matrix(self.columns, self.columns)
            for i in range(self.columns):
                new_matrix.numbers[i][i] = self.numbers[0][i]
            return new_matrix
        elif self.rows == self.columns and self.rows == 1:
            return Matrix(1, 1, [self.numbers[0][0]])
        elif self.rows == self.columns:
            new_matrix = Matrix(self.rows, 1)
            for i in range(self.rows):
                new_matrix.numbers[0][i] = self.numbers[i][i]
            return new_matrix


    @staticmethod
    def ones(cols: int, rows:int = 1, number:Union[int, float] = 1) -> 'Matrix':
        """
        Returns a new matrix with all elements set to number (default 1).
        params: cols: Number of columns in the matrix
        params: rows: Number of rows in the matrix (default 1)
        params: number: Number to fill in the matrix (default 1)
        """
        return Matrix(rows, number, [[number for _ in range(number)] for _ in range(rows)])


    def __str__(self) -> str:
        """
        Returns a string representation of this matrix.
        """
        matrix_str = ''
        for row in self.numbers:
            matrix_str += ' '.join(f"{x:.2f}" for x in row) + '\n'
        return matrix_str.strip()


    def input(self, vector_input:bool=False) -> 'Matrix':
        """
        Function to get user input and populate the matrix dynamically.
        Parses input row by row and updates matrix dimensions accordingly.
        """
        self.numbers = []
        iter:int = 0
        while True:
            if vector_input and iter != 0:
                break
            temp = input()
            if temp == "":  # Stop input when user presses Enter twice
                break
            row = list(map(float, temp.split()))  # Convert input row to list of floats

            # Check if all rows have the same number of columns
            if self.numbers and len(row) != len(self.numbers[0]):
                print(f"Row length mismatch. Expected {len(self.numbers[0])} values.")
                continue

            self.numbers.append(row)
            iter += 1

        # Update rows and columns based on input
        self.rows = len(self.numbers)
        self.columns = len(self.numbers[0]) if self.rows > 0 else 0
        if vector_input:
            return self.transpose()
        return self
    

if __name__ == "__main__":
    # Example usage
    v = Matrix().input(True)
    print(v)
    print("Transposed:")
    print(v.transpose())
    print("Diagonal matrix:")
    print(v.diag())
    print(Matrix(2, 4)*Matrix(4, 2))
    print(Matrix(4, 4).identity()*3)
    print(3 * Matrix(4, 4).identity())
    print(Matrix.ones(4))
    print(Matrix.ones(4,4))
