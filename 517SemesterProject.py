"""CS 517 - Computational Methods and Software 

CPU Temperature Semester Project

Description: The below program takes the CPU temperature readings from the file which we should provide 
at the command prompt. The input files can be given either with labels or without labels. After we give the input,
the program generates the following:

    1) A global linear least-squares approximation.
    2) A piecewise linear interpolation.

No python packages are used.

The functions used are listed below:    
    1) matrix_create: used to create a 2d matrix using nested lists
    2) matrix_print : used to print the nested lists in matrix form
    3) matrix_transpose : used to transpose the 2d matrix
    4) multiply : used to multiply two matrices
    5) leastsquares_approximation : Fits the data using global least squares
    6) piecewiselinear_interpolation : Fits the data using linear piecewise interpolation functions.    
    7) gaussian_eliminate : Solves the system of equations Ax=b using gaussian eliminations. It calls
      functions rows_S, sol_b.
    8) sol_b : Solves for matrix x in the system of equations Ax=b.  
    9) read_data : Used to read the data from the file provided at the command prompt
    10) line_C : Creates a line in the format xk<=x<xk+1; yi=c0+c1x ; type
    11) main : #This is the main function which reads all the input data provided at command prompt and calls all required functions. 
	It also checks whether required number of inputs are provided at the command prompt. It also writes the interpolated data to the file {basename}-interop-data.{txt}
"""
import sys
import os

def matrix_create(jrows: int, jcolumns: int) -> list: 
    
    """This function is utilized to create a 2d matrix using nested lists
        Parameters:
        jrows : to calculate number of rows
        jcolumns : to calculate number of columns
    
        Yields:
        mat: This returns 2d matrix in a nested list
    """
    mat = []
    i =0
    while(i<jrows):
        z = []
        for j in range(0, jcolumns):
            z.append(0.0)
        mat.append(z)
        i+=1
    return mat

def matrix_print(X: list, MAX_DIG: int = 8) -> None: 
    
    """This function prints the matrix stores in the nested loop as a matrix format.
        Parameters:
        X : It is a nested list containing the 2D matrix that needs to be printed.
        MAX_DIG : Controls the spacing between elements of the matrix.
    
        Yields:
        This prints the matrix in nested list as a matrix format
    """
    
    for i in range(0, len(X)):
        z_str = "|"
        for j in range(0, len(X[0])):

            z = float("{}".format(round(float(X[i][j]), MAX_DIG)))
            z_str = z_str + str(z).center(MAX_DIG+2, ' ')

        z_str = z_str + "|"
        print(z_str)

def matrix_transpose(X: list) -> list: 
    
    """This function is used to create a transpose matrix XT
        Functions called: matrix_create

        Parameters:
        X: It is a list containing 2D matrix that needs to be transposed

        Yields:
        XT: This transposes the matrix.
    """    
    jrows = len(X)
    jcolumns = len(X[0])
    XT = matrix_create(jcolumns, jrows)

    for j in range(0, jcolumns):
        for i in range(0, jrows):
            XT[j][i] = X[i][j]

    return XT

def multiply(X: list, Y: list) -> list: 
    
    """ This function is used to multiply matrices X and Y
        Functions called: matrix_create

        Parameters:
        X,Y : These are matrices that need to be multiplied

        Yields:
        XY : This returns product of matrices X and Y
    """
    
    jrows_X = len(X)
    jcolumns_X = len(X[0])

    jrows_Y = len(Y)
    jcolumns_Y = len(Y[0])

    if jcolumns_X != jrows_Y:
        print("Columns of X is != rows of Y")
        sys.exit()

    XY = matrix_create(jrows_X, jcolumns_Y)
    for i in range(0, jrows_X):
        for k in range(0, jcolumns_Y):
            for j in range(0, jcolumns_X):
                XY[i][k] = XY[i][k]+X[i][j]*Y[j][k]

    return XY


def leastsquares_approximation(data: list, fname: str) -> list: 
    
    """This function substitutes the values of temperature of each core of cpu into a global linear least squares apporximation
    function in the form y = c0 + c1*x. This function calls the function matrix_transpose and multiplies to form the matrix system XTX*C=XTy and gaus_elim function to solve the coefficients c0 and c1.
    Functions called: matrix_create, matrix_transpose, multiply, gaussian_Eliminate

        Parameters:
        data: This list contains the temperature data of computer cores
        fname: fname consists of the temperature data of CPU

        Yields:
        beta_dsi: This Returns list containing global coefficients list beta=[c0,c1] for each core stored  as
        [beta_list_core0,beta_list_core1,......]. It writes the coefficients of global least square approximation function in the format
        "xk<=x<xk+1; yk=c0+c1x ; least-squares" and returns the coefficient.

    """

    beta_dsi = []
    for icore in range(1, len(data[0])):

        print("initiating for core-", int(icore-1))

        X = matrix_create(len(data), 2)
        y = matrix_create(len(data), 1)

        for irow in range(0, len(data)):

            X[irow][0] = 1.0
            X[irow][1] = data[irow][0]

            y[irow][0] = data[irow][icore]

        XT = matrix_transpose(X)
        XTX = multiply(XT, X)
        XTy = multiply(XT, y)

        jrows_A = len(XTX)
        jcolumns_A = len(XTX[0])

        A = matrix_create(jrows_A, jcolumns_A+1)
        for irow in range(0, jrows_A):
            for icol in range(0, jcolumns_A):
                A[irow][icol] = XTX[irow][icol]
            A[irow][-1] = XTy[irow][0]

        beta = gaussian_eliminate(A)

        print_lines = line_C(data[0][0], data[-1][0], 0, beta, "least-squares")+"\n"
        filename = fname[:-4]+"-core-"+str(icore-1)+".txt"

        fout = open(filename, "a+")
        fout.write(print_lines)
        fout.close()

        beta_dsi.append(beta)

    return beta_dsi


def piecewiselinear_interpolation(data: list, fname: str) -> list: 
    
    """ This function substitutes the values of temperature of each core of cpu into a piecewise linear interpolation function y = c0 + c1*x.
     Functions called: line_C

    Parameters:
        data: This list contains the temperature data of computer cores
        fname: fname consists of the temperature data of CPU

    Yields:
        beta_all: This returns list containing coefficients [c0,c1] at every interval between data points
        of the piecewise linear interpolation function. It writes the coefficients of piecewise linear interpolation function in the format
        "xk<=x<xk+1; yi=c0+c1x ; interpolation" in each interval of the data points.
    """
    beta_dsi = []
    for icore in range(1, len(data[0])):

        print("initiating for core-", int(icore-1))

        print_lines = ""
        for irow in range(0, len(data)-1):

            x0 = data[irow][0]
            x1 = data[irow+1][0]
            f0 = data[irow][icore]
            f1 = data[irow+1][icore]
            c0 = f0-(f1-f0)/(x1-x0)*x0
            c1 = (f1-f0)/(x1-x0)

            beta = [[c0], [c1]]
            print_lines = print_lines + \
                line_C(data[irow][0], data[irow+1][0],
                            irow, beta, "interpolation")+"\n"

        filename = fname[:-4]+"-core-"+str(icore-1)+".txt"

        fout = open(filename, "a+")
        fout.write(print_lines)
        fout.close()

        beta_dsi.append(beta)

    return beta


def gaussian_eliminate(A: list) -> list: 
    
    """This function uses Gaussian elimination to solve the system of equations.
    Functions called: rows_S, sol_b

        Parameters:
        A : This is a Matrix [A,b]

        Yields:
        beta : This list contains the solution

    """
    jrows = len(A)
    jcolumns = len(A[0])

    for k in range(0, jrows):

        idx = k
        find_largest_col = A[idx][k]

        for i in range(k+1, jrows):
            if abs(A[i][k]) > find_largest_col:
                find_largest_col = A[i][k]
                idx = i

        if idx != k:
            rows_S(A, k, idx)

        for i in range(k+1, jrows):
            f = A[i][k]/A[k][k]
            for j in range(k+1, jrows+1):
                A[i][j] = A[i][j]-A[k][j]*f
            A[i][k] = 0

    beta = sol_b(A)

    return beta


def sol_b(A: list) -> list: 
    
    """This function back solves coefficients matrix 'x' in system of equations Ax=b.
    Functions called : matrix_create

        Parameters:
        A : This list contains matrix [A,b]

        Yields:
        coeff_matrix : This list contains coefficient matrix 'x' 

    """
    jrows = len(A)
    jcolumns = len(A[0])-1

    coeff_matrix = matrix_create(jrows, 1)

    for i in range(jrows-1, -1, -1):

        coeff_matrix[i][0] = A[i][jrows]

        for j in range(i+1, jrows):
            coeff_matrix[i][0] = coeff_matrix[i][0]-A[i][j]*coeff_matrix[j][0]

        coeff_matrix[i][0] = coeff_matrix[i][0]/A[i][i]

    return coeff_matrix


def rows_S(A: list, i: int, j: int) -> None: 
    
    """This function is used to swap row i with row j in matrix A

        Parameters:
        A : This list contains matrix [A,b]
        i,j : These are row numbers that need to be swapped

        Yields:
        This function Swaps rows i and j in matrix A 

    """
    jcolumns = len(A[0])

    k = 0
    while (k < jcolumns):
        x = A[i][k]
        A[i][k] = A[j][k]
        A[j][k] = x
        k+=1

def read_data(fname: str) -> list: 
    
    """This function is used to read the data from the input file provided at the command prompt
    Functions called: matrix_create

        Parameters:
        fname: fname consists of the temperature data of cpu

        Yields:
        A: This matrix contains the data starting from column 1. Column 0 consists of time in intervals of
        30 minutes
    """
    fout = open(fname, "r")
    data = fout.readlines()
    fout.close()

    jrows = len(data)
    jcolumns = len(data[0].split(" "))+1
    A = matrix_create(jrows, jcolumns)

    for i in range(0, jrows):
        A[i][0] = i*30.0
        for j in range(1, jcolumns):

            arg = data[i]
            z = ''
            for istr in arg:
                if ord(istr) > 47 and ord(istr) < 58:
                    z = z+istr
                if ord(istr) == 32 or ord(istr) == 43 or ord(istr) == 46:
                    z = z+istr

            A[i][j] = float(z.split(" ")[j-1])

    return A


def line_C(x0: float, x1: float, num: int, beta: list, eqtn_z: str) -> str: 
    
    """This function is used to create the format "xk<=x<xk+1; equation ; type" for the interpolation equation output
    Parameters:
        x0,x1 : These are time coordinates
        num : This is a solution number
        beta : These are Coefficients of approximation functions for the eqtn_z.

    Yields:
        print_line : String with equation between x0 and x1."""

    print_line = str(int(x0)).rjust(7, ' ')
    print_line = print_line+" <= x < "
    print_line = print_line+str(int(x1)).rjust(7, ' ')+"; "

    print_line = print_line+("y_"+str(num)).ljust(9, ' ')+"= "
    z = "{:.4f}".format(beta[0][0])
    print_line = print_line+z.rjust(12, ' ')+" + "
    z = "{:.4f}".format(beta[1][0])
    print_line = print_line+(z+"x").rjust(9, ' ')+"; "

    print_line = print_line+eqtn_z
    
    return print_line

def main(): 
    
    """This is the main function which reads all the input data provided at command prompt and calls all required functions. It also checks whether required number of inputs are provided at the command prompt.
    Functions called: read_data, piecewiselinear_interpolation, leastsquares_approximation.

    Yields:
        This function calls all the required functions.
    """
    if len(sys.argv) < 2:
        print("Number of inputs are wrong")
        sys.exit()

    if not os.path.isfile(sys.argv[1]):
        current = os.getcwd()
        print(sys.argv[1], " file does not exist in the working folder:", current)
        sys.exit()

    fname = sys.argv[1]

    data = read_data(fname)

    for icore in range(1, len(data[0])):

        filename = fname[:-4]+"-core-"+str(icore-1)+".txt"
        fout = open(filename, "w")
        fout.close()

    print("Global Least Squares Approximation")
    beta_LS = leastsquares_approximation(data, fname)

    print("Piecewise Linear Interpolation")
    beta_PL = piecewiselinear_interpolation(data, fname)


if __name__ == "__main__":
    main()
