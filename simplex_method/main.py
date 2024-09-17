class Vector:
    row = []
    numb_of_rows = 0
    def __init__(self, row):
        self.row = row
        self.numb_of_columns = len(row)
    def input(self):
        temp = input()
        self.row = temp.split(' ')
        self.numb_of_rows = len(self.row)
    def __init__(self):
        self.row = []
        self.numb_of_rows = 0
    def input_rows(self, row):
        self.row = row.split(' ')
        self.numb_of_rows = len(row)
class Matrix:
    matrix = [Vector]
    numb_of_columns = 0
    numb_of_rows = 0
    def __init__(self, matrix):
        self.matrix = matrix
        self.numb_of_rows = len(matrix)
        self.numb_of_columns = len(matrix[0])
    def __init__(self):
        self.matrix = [[]]
        self.numb_of_rows = 0
        self.numb_of_columns = 0
    def input(self):
        list = [[]]
        temp = input()
        while temp != "":
            list.append(Vector.input_rows(Vector(), temp))
            temp = input()
        self.matrix = list
        self.numb_of_rows = len(list)
        self.numb_of_columns = len(list[0])
        
def input_variables():
    print('First of all write a vector of coefficients of objective function!')
    vcof = Vector().input()
    print('Now write a matrix of coefficients of constraint function')
    mccf = Matrix().input()
    print('After that write a vector of right-hand side numbers')
    vrhsn = Vector().input()
    print('Last one, write the approximation acuracy')
    apac = int(input()) 
    print(vcof.row, mccf, vrhsn, apac)
if __name__ == '__main__':
    input_variables()
    print("Welcome to Hell")