class Matrix:
    #TODO Add comments
    def __init__(self, rows=0, cols=0, numbers=None):
        self.rows = rows
        self.columns = cols
        if numbers:
            self.numbers = numbers
        else:
            self.numbers = [[0 for _ in range(cols)] for _ in range(rows)]

    def __sub__(self, other):
        if self.rows == other.rows and self.columns == other.columns:
            result = Matrix(self.rows, self.columns)
            for i in range(self.rows):
                for j in range(self.columns):
                    result.numbers[i][j] = self.numbers[i][j] - other.numbers[i][j]
            return result
        else:
            raise Exception("Error: the dimensional problem occurred")

    def __add__(self, other):
        if self.rows == other.rows and self.columns == other.columns:
            result = Matrix(self.rows, self.columns)
            for i in range(self.rows):
                for j in range(self.columns):
                    result.numbers[i][j] = self.numbers[i][j] + other.numbers[i][j]
            return result
        else:
            raise Exception("Error: the dimensional problem occurred")

    def __mul__(self, other):
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

    def transpose(self):
        result = Matrix(self.columns, self.rows)
        for i in range(self.rows):
            for j in range(self.columns):
                result.numbers[j][i] = self.numbers[i][j]
        return result

    def determinant(self):
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

    def identity(self):
        if self.rows != self.columns:
            raise Exception("Error: Identity matrix must be square.")
        identity_matrix = Matrix(self.rows, self.rows)
        for i in range(self.rows):
            identity_matrix.numbers[i][i] = 1
        return identity_matrix

    def nullify(self, row, col, row_to_start):
        row -= 1
        col -= 1
        for j in range(row_to_start, self.rows):
            if j != row:
                if self.numbers[row][col] != 0 and self.numbers[j][col] != 0:
                    multiplier = self.numbers[row][col] / self.numbers[j][col]
                    for i in range(self.columns):
                        self.numbers[row][i] -= self.numbers[j][i] * multiplier

    def exchange(self, i1, i2):
        i1 -= 1
        i2 -= 1
        if i1 < self.rows and i2 < self.rows:
            self.numbers[i1], self.numbers[i2] = self.numbers[i2], self.numbers[i1]
        else:
            raise Exception("Error: Index out of bounds.")

    def inverse(self):
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


    def __str__(self):
        matrix_str = ''
        for row in self.numbers:
            matrix_str += ' '.join(f"{x:.2f}" for x in row) + '\n'
        return matrix_str.strip()

    def input(self, vector_input:bool=False):
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