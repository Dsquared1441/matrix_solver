'''
	OK, so I fixed it and it works properly, now
	
	Additional improvement to make (DONE):
	- solving matrix gives really wierd float numbers -- like 4e-28 when it is supposed to be 0 and 1.000000000000000000000 for 1
		- used floating point precision of 1e-6 to solve round-off errors when adding numbers
'''

from matrix import Matrix

# finds the pivot col of a 
def findPivot(row):
    for (i, x) in enumerate(row):
        if x != 0:
            return i

# zeroes out cols by finding nonzero entries below pivot, scaling it, and adding it           
def zeroOutLowerCols(mat, row, col):
    rowmax = mat.size[0];
    for r in range(row+1, rowmax):
        if mat.matrix[r][col] != 0:
            target = mat.matrix[r][col];
            mat.scale(r, 1/target);
            mat.replace(row, r);

# does same thing as zeroOutLowerCols(), but does it for upper cols
def zeroOutUpperCols(mat, row, col):
    for r in range(row-1, -1, -1):
        if mat.matrix[r][col] != 0:
            target = mat.matrix[r][col];
            mat.scale(r, -1/target);
            mat.replace(row, r);
            mat.scale(r, -target);

# checks if matrix is all zeroes
def isZeroMatrix(lists):
    for i in lists:
        for j in i:
            if j != 0:
                return False
    return True

# solves a matrix in RREF
def solve(matrix):
    # copy matrix
    mat = matrix.copy();
    if isZeroMatrix(mat.matrix[:]):
        return 'Zero matrix'
    
    # init vars
    row = 0;
    row_max = mat.size[0];
    
    while (row < row_max):
        # find pivot coordinates (check if zero row first)
        
        # if zero row, push list to bottom and pull other lists up
        if mat.isZeroRow(row):
            mat.matrix.append(mat.matrix[row])
            mat.matrix.pop(row)
            if isZeroMatrix(mat.matrix[row:]):
                print('Free solution detected...')
                break
            continue
        else:
            piv_row = row;
            piv_col = findPivot(mat.matrix[row]);
        
        # scale pivot coordinates
        pivot = mat.matrix[piv_row][piv_col];
        mat.scale(piv_row, -1/pivot);
        
        # make col all zeroes
        zeroOutLowerCols(mat, piv_row, piv_col);

        mat.scale(row, -1);
        
        # increment row counter
        row += 1;
        
    row = row_max - 1;
    
    # now find most recent pivot and make all upper cols zero
    while (row > -1):
        
        # reverse find pivot (check if zero first)
        
        if mat.isZeroRow(row):
            row -= 1;
            continue
        
        piv_row = row;
        piv_col = findPivot(mat.matrix[row]);
        
        # zero out upper col
        zeroOutUpperCols(mat, piv_row, piv_col);
        
        row -= 1;
        
    print(mat)


    
