class Matrix:
    def __init__(self, matrix_string):
        self.matrix = [[int(x) for x in row.split(' ')] for row in matrix_string.split('\n')]
        # makes matrix: first make rows with .split('\n') then seperates the numbers in each row by .spilt(' ') and finally changes the type from string to int

    def row(self, index):
        return self.matrix[index - 1]

    def column(self, index):
        return [row[index - 1] for row in self.matrix]
