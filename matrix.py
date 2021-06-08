import math
from math import sqrt
import numbers

def zeroes(height, width):
        """
        Creates a matrix of zeroes.
        """
        g = [[0.0 for _ in range(width)] for __ in range(height)]
        return Matrix(g)

def identity(n):
        """
        Creates a n x n identity matrix.
        """
        I = zeroes(n, n)
        for i in range(n):
            I.g[i][i] = 1.0
        return I

class Matrix(object):

    # Constructor
    def __init__(self, grid):
        self.g = grid
        self.h = len(grid)
        self.w = len(grid[0])

    #
    # Primary matrix math methods
    #############################
 
    def determinant(self):
        """
        Calculates the determinant of a 1x1 or 2x2 matrix.
        """
        if not self.is_square():
            raise ValueError("Cannot calculate determinant of non-square matrix.")
        if self.h > 2:
            raise NotImplementedError("Calculating determinant not implemented for matrices largerer than 2x2.")
        
        # TODO - your code here

        elif self.h==2:

            detmatrix = ((self.g[0][0] * self.g[1][1]) - (self.g[0][1] * self.g[1][0]))
            if detmatrix == 0:
                raise ValueError('The matrix is irrevetible because its determinant is 0')
                
        else:
            detmatrix = self.g
        
        
        return detmatrix
    
    def trace(self):
        """
        Calculates the trace of a matrix (sum of diagonal entries).
        """
        if not self.is_square():
            raise ValueError("Cannot calculate the trace of a non-square matrix.")

        # TODO - your code here
        sum_diag = 0
        
        for i in range(self.w):
            for j in range(self.h):
                if i==j:
                    sum_diag += self.g[i][j]
        return sum_diag
    
    def inverse(self):
        """
        Calculates the inverse of a 1x1 or 2x2 Matrix.
        """
        if not self.is_square():
            raise ValueError("Non-square Matrix does not have an inverse.")
        if self.h > 2:
            raise NotImplementedError("inversion not implemented for matrices larger than 2x2.")

        # TODO - your code here
        inverse = []
        
        if self.h == 1:
            inverse = [[1/self.g[0][0]]]
        
        else:

            detmatrix = self.determinant()

            I = identity(self.h)

            trmatrix = self.trace()
            
            for i in range(self.h):
                row = []
                for j in range(self.w):
                    row.append(((trmatrix * I[i][j]) - self.g[i][j])/detmatrix)
                inverse.append(row)
        obj = Matrix(inverse)
        return obj
        
    def T(self):
        """
        Returns a transposed copy of this Matrix.
        """
        # TODO - your code here
        matrix_transpose = []
        # Loop through columns on outside loop
        for c in range(self.w):
            new_row = []
            # Loop through columns on inner loop
            for r in range(self.h):
                # Column values will be filled by what were each row before
                new_row.append(self.g[r][c])
            matrix_transpose.append(new_row)
        obj = Matrix(matrix_transpose)
        return obj

    def is_square(self):
        return self.h == self.w

    #
    # Begin Operator Overloading
    ############################
    def __getitem__(self,idx):
        """
        Defines the behavior of using square brackets [] on instances
        of this class.

        Example:

        > my_matrix = Matrix([ [1, 2], [3, 4] ])
        > my_matrix[0]
          [1, 2]

        > my_matrix[0][0]
          1
        """
        
        return self.g[idx]

    def __repr__(self):
        """
        Defines the behavior of calling print on an instance of this class.
        """
        s = ""
        for row in self.g:
            s += " ".join(["{} ".format(x) for x in row])
            s += "\n"
        return s

    def __add__(self,other):
        """
        Defines the behavior of the + operator
        """
        if self.h != other.h or self.w != other.w:
            raise ValueError("Matrices can only be added if the dimensions are the same") 
        #   
        # TODO - your code here
        #
        matrixSum = []
        for i in range(self.h):
            row = []
            for j in range(self.w):
                row.append(self.g[i][j] + other.g[i][j])
            matrixSum.append(row)    

        obj = Matrix(matrixSum)
        return obj
    
    def __neg__(self):
        """
        Defines the behavior of - operator (NOT subtraction)

        Example:

        > my_matrix = Matrix([ [1, 2], [3, 4] ])
        > negative  = -my_matrix
        > print(negative)
          -1.0  -2.0
          -3.0  -4.0
        """
        #   
        # TODO - your code here
        #
        neg_self = []
        for i in range(self.h):
            row = []
            for j in range(self.w):
                row.append(-1 * self.g[i][j])
            neg_self.append(row)
        obj = Matrix(neg_self)
        return obj


    def __sub__(self, other):
        """
        Defines the behavior of - operator (as subtraction)
        """
        if self.h != other.h or self.w != other.w:
            raise ValueError("Matrices can only be substracted if the dimensions are the same")         
        #   
        # TODO - your code here
        #
        matrixSub = []
        for i in range(self.h):
            row = []
            for j in range(self.w):
                row.append(self.g[i][j] - other.g[i][j])
            matrixSub.append(row)    

        obj = Matrix(matrixSub)
        return obj        

    def __mul__(self, other):
        """
        Defines the behavior of * operator (matrix multiplication)
        """
        #   
        # TODO - your code here
        #
        def dot_product(vector_one, vector_two):
            if len(vector_one) != len(vector_two):
                print("error! Vectors must have same length")

            result = 0
            for i in range(len(vector_one)):
                value_1 = vector_one[i]
                value_2 = vector_two[i]
                result += value_1 * value_2

            return result
        
        def get_column(matrix, column_number):
            column = []
            for i in range(len(matrix)):
                column.append(matrix[i][column_number])
                
            return column 
        
        def get_row(matrix, row):

            return matrix[row] 
        
        if self.w != other.h:
            raise ValueError('Matrices can only be multiplied if the no of column in 1st matrix and no of row in 2nd, are not the same')
    
        result = []
        for r in range(self.h):
            row_result = []
            row_vector = get_row(self.g, r)
            for c in range(other.w):
                column_vector = get_column(other.g, c)
                element = dot_product(row_vector, column_vector)
                row_result.append(element)
             
            result.append(row_result)
        
        obj = Matrix(result)
        return obj
        
    def __rmul__(self, other):
        """
        Called when the thing on the left of the * is not a matrix.

        Example:

        > identity = Matrix([ [1,0], [0,1] ])
        > doubled  = 2 * identity
        > print(doubled)
          2.0  0.0
          0.0  2.0
        """
        if isinstance(other, numbers.Number):
            
            #   
            # TODO - your code here
            #
            scaler_mu = []
            for i in range(self.h):
                row = []
                for j in range(self.w):
                    row.append(other *self.g[i][j])
                scaler_mu.append(row)
            
            obj = Matrix(scaler_mu)
            return obj 
  
                    
                    
                    