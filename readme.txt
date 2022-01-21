Python 3.8.9

A) The Zip folder consists of the following files:
	1) 517SemesterProject.py
	2) 2 inpufiles
		a)temperatureinput.txt
		b)temperatureinputnolabels.txt
	3) 8 Output files
		a)4 output files for each core (input given with labels)
		b)4 output files for each core (input given without labels)


B) Program Description
The program takes the values of temperature readings from the input file provided at the command 
prompt and generates the following for each core:
	1) A global linear least-squares approximation.
	2) A piecewise linear interpolation.
    
C) Instructions to execute the program 
1)Open command prompt and navigate to the respective directory.
2)You can run either of the following commands to execute the program.
    python 517SemesterProject.py temperatureinputnolabels.txt (Input file without labels)
    python 517SemesterProject.py temperatureinput.txt (Input file with labels)
3)The program generates files temperatureinputs-core-<core_number>, temperatureinput-no-labels-core-<core_number>.txt for each core.

#Sample inputs
python 517SemesterProject.py temperatureinputnolabels.txt
python 517SemesterProject.py temperatureinput.txt
 
#Sample output
Global Least Squares Approximation
initiating for core- 0
initiating for core- 1
initiating for core- 2
initiating for core- 3
Piecewise Linear Interpolation
initiating for core- 0
initiating for core- 1
initiating for core- 2
initiating for core- 3 	

The functions used are listed below:    
    1) matrix_create: used to create a 2d matrix using nested lists
    2) matrix_print : used to print the nested lists in matrix form
    3) matrix_transpose : used to transpose the 2d matrix
    4) multiply : used to multiply two matrices
    5) leastsquares_approximation : Fits the data using global least squares
    6) piecewiselinear_interpolation : Fits the data using linear piecewise interploation functions.    
    7) gaussian_eliminate : Solves the system of equations Ax=b using gaussian eliminations. It calls
      functions rows_S, sol_b.
    8) sol_b : Solves for matrix x in the system of equations Ax=b.  
    9) read_data : Used to read the data from the file provided at the command prompt
    10) line_C : Creates a line in the format xk<=x<xk+1; yi=c0+c1x ; type
    11) main : #This is the main function which reads all the input data provided at command prompt and calls all required functions. 
	It also checks whether required number of inputs are provided at the command prompt. It also writes the interpolated data to the file {basename}-interop-data.{txt}



