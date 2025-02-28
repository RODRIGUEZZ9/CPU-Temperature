# CS517 - Graduate Project in Computational Programming

## Python Version  
**Python 3.8.9**

## Project Structure  
The ZIP folder consists of the following files:

### 1. Python Script
- `517SemesterProject.py`

### 2. Input Files
- `temperatureinput.txt` (Input file with labels)
- `temperatureinputnolabels.txt` (Input file without labels)

### 3. Output Files
The program generates 8 output files:
- **4 output files for each core** (when input is provided with labels).
- **4 output files for each core** (when input is provided without labels).

---

## 📌 Program Description  
This program processes temperature readings from an input file and performs the following operations for each core:

1. **Global Linear Least-Squares Approximation**  
2. **Piecewise Linear Interpolation**

---

## 🛠 Instructions to Execute the Program  

### Step 1: Open Command Prompt  
Navigate to the directory containing the script.

### Step 2: Run the Program  
You can use either of the following commands:

```sh
python 517SemesterProject.py temperatureinputnolabels.txt  # Input file without labels
python 517SemesterProject.py temperatureinput.txt          # Input file with labels
```

### Step 3: Output Files  
For each core, the program generates files in the format:
- `temperatureinputs-core-<core_number>.txt`
- `temperatureinput-no-labels-core-<core_number>.txt`

---

## 📝 Sample Execution  

### Sample Command
```sh
python 517SemesterProject.py temperatureinputnolabels.txt
python 517SemesterProject.py temperatureinput.txt
```

### Sample Output  
```sh
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
```

---

## 🏗 Functions Used  

| Function Name                     | Description |
|------------------------------------|-------------|
| **`matrix_create`**               | Creates a 2D matrix using nested lists. |
| **`matrix_print`**                | Prints the nested lists in matrix form. |
| **`matrix_transpose`**            | Transposes the 2D matrix. |
| **`multiply`**                    | Multiplies two matrices. |
| **`leastsquares_approximation`**  | Fits the data using global least squares. |
| **`piecewiselinear_interpolation`** | Fits the data using linear piecewise interpolation functions. |
| **`gaussian_eliminate`**          | Solves the system of equations Ax = b using Gaussian elimination. Calls functions `rows_S` and `sol_b`. |
| **`sol_b`**                        | Solves for matrix x in the system of equations Ax = b. |
| **`read_data`**                    | Reads data from the file provided at the command prompt. |
| **`line_C`**                       | Creates a line in the format `xk <= x < xk+1 ; yi = c0 + c1x`. |
| **`main`**                         | The main function that:  
  - Reads input data from the command prompt.  
  - Calls all required functions.  
  - Ensures the required number of inputs are provided.  
  - Writes interpolated data to `{basename}-interop-data.txt`. |

---

## 📌 Notes  
- Ensure that all input files are in the same directory as the script before running.  
- The program automatically generates output files per core and applies different numerical techniques.  

---

**🚀 Happy Coding!**
