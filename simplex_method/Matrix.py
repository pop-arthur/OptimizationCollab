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
