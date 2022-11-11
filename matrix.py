print("mat.py imported.")

class Matrix():
    
    '''
        rows -- a list of rows for the matrix, where each row is a list
    '''
    def __init__(self, rows, precision=1e-6):
        self.matrix = rows;
        self.size = [len(rows), len(rows[0])];
        self.row_len = len(rows[0])
        self.precision = precision
    
    # checks if row n is all zeroes    
    def isZeroRow(self, n):
        for i in range(0, self.row_len):
            if self.matrix[n][i] != 0:
                return False
        return True
        
    # scales row row by a factor of n
    def scale(self, row, n):
        for i in range(0, self.row_len):
            self.matrix[row][i] = self.matrix[row][i] * n;
            
    # swaps row row1 with row row2
    def swap(self, row1, row2):
        a = self.matrix[row1][:]
        b = self.matrix[row2][:]
        self.matrix[row1] = b;
        self.matrix[row2] = a;
    
    # adds the entries from row r1 into row r2, and stores them into row r2    
    def replace(self, r1, r2):
        row1 = self.matrix[r1];
        row2 = self.matrix[r2];
        for i in range(0, self.row_len):
            s = row2[i] + row1[i];
            row2[i] = s if (abs(s) > self.precision) else 0
        self.matrix[r2] = row2;

    # creates a copy of the matrix
    def copy(self):
        a = []
        for i in range(0, self.size[0]):
            b = [];
            for j in range(0, self.size[1]):
                b.append(self.matrix[i][j]);
            a.append(b)
        return Matrix(a)
        
    def __str__(self):
        s = '\n';
        for i in self.matrix:
            s += str(i) + '\n';
        return s
            
    def __repr__(self):
        s = '\n';
        for i in self.matrix:
            s += str(i) + '\n';
        return s

