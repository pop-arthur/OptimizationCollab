class Matrix:
    def __init__(self, rows, cols, numbers=None):
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

    def __str__(self):
        matrix_str = ''
        for row in self.numbers:
            matrix_str += ' '.join(f"{x:.2f}" for x in row) + '\n'
        return matrix_str.strip()

