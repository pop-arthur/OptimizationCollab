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
