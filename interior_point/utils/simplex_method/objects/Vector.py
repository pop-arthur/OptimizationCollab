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
    
    # @property
    # def numb_of_columns(self):
    #     return len(self.row)
    
    # @numb_of_columns.setter
    # def numb_of_columns(self, value):
    #     self.numb_of_columns = value

    def input(self):
        """
        Function to get user input and handle it. Parse input by itself
        """
        temp = input("Enter the vector (space-separated values): ")
        self.row = list(map(float, temp.split()))  # Convert input to list of floats
        self.numb_of_columns = len(self.row)
        return self

    def __getitem__(self, item):
        # print(item, len(self.row)) #For debugging purposes only
        # print(f"Getting item {item} from vector {self.row}") #For debugging purposes only
        return self.row[item]

    def multiply_by(self, coefficient):
        for i in range(len(self.row)):
            self.row[i] = self.row[i] * coefficient
