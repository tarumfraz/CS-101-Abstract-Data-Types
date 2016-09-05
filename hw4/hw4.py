# hw4.py
# CMPS 101
# Tarum Fraz - 1349796
# Andres Segundo
# Stack overflow, google, textbooks, and TA sessions helped to write this code



import numpy as np
import scipy
import timeit
import matplotlib.pyplot as plt

# Function that acts as a matrix multiplication calculator
def matmult(A, x): # Takes input numpy array size N x N, and a 1D numpy array
	
		n = A.shape[0] # Dim of matrix
		xlen = x.shape[0] # Dim of x
		if (xlen != n): # If column of A is not equal to the column of B
			return 0# The matricces are incompatible so return
		
		x = np.reshape(x,(xlen, -1)) # correct the dim of vector
		matrix = np.empty((n), dtype = int) # Initialize ill the empty array
		for i in range(n): # For loop to iterate through the array
			matrix[i] = 0
			for j in range(n):
				matrix[i] += int( A[i,j] * x[j,0]) # Multiply with appropriate value
		return matrix # Return Matrix vector product

	
def hadmat(k): # Function that produces a Hadamard Matrix

	matrix = np.empty([2**k,2**k]) # Initialize an empty numpy array or appropiate size
	n = 2**k #n is just the rows and columns
	x = 1 #also used to keep track of k,i, and j assignments
	i = 0
	j = 0
	matrix[0][0] = 1 # Set first element to 1
	while(x < n): # keep index in bounds
		for i in range(x):
			for j in range(x):
				matrix[i+x][j] = matrix[i][j] # Implements the correct positive values
				matrix[i][j+x] = matrix[i][j]
				matrix[i+x][j+x] = -(matrix[i][j]) # Implements the correct negative values
		x += x
	return matrix



def hadmatmult(H, x):

	n = len(H) # dim of Hamard Matrix
	xlen = len(x) # dim of vector
	if (xlen != n): # If column of A is not equal to the column of B
		return 0 # The matricces are incompatible so return

	if (n == 0): # The matrix is filled with zeros so solution is trivial
		return 0 

	if xlen== 2: # This is when the case is trivial
		H2 = np.empty(2, dtype = int)

		a = H[0][0] * x[0]
		b = H[0][0] * x[1]

		H2[0] = a + b
		H2[1] = a - b

		return H2

	x1 = x[0:(xlen//2)] # split the vector 
	x2 = x[(xlen//2):]
	H3 = H[0:n//2, 0:n//2] # Create a smaller Hadamard Matrix
	L = hadmatmult(H3, x1)  # Recurr to multiply
	R = hadmatmult(H3, x2)
	top = L + R # Use x1 + x2 recurisvely 
	bottom = L - R # Use x1 + x2 recurisvely 
	matrix = np.concatenate([top, bottom]) # Concatenate all of the vectors

	return matrix # Return matrix H_n*(x)
	


# Q5:

#if __name__ == '__main__': # Test Help

  
 #   counter1 = range(1, 13) # Set the range for the x axis
 #  counter2 = len(counter1) # Helps us with other ranges
 #   plotter = [2 ** k for k in counter1] # Helps us with plotting

   
 #   mm = np.empty(counter2) # Initialize two empty arrays for the graph
 #   hm= np.empty(counter2)

 #   matmultTimer = timeit.Timer(lambda: matmult(H, x)) # The timer objects
 #   hadmultTimer = timeit.Timer(lambda: hadmatmult(H, x))

 #   for k in counter1: # Helps us gett the k value for input and n=2^k
        
        # Create hadamard matrix and random vector inputs
 #       H = hadmat(k) # Call to create matrix
 #      x = np.random.randint(-5, 50, 2 ** k) # Create random vector to multiply with 

 #       mm[k - 1] = matmultTimer.timeit(number=1) # Keep track of all of the running times
 #       hm[k - 1] = hadmultTimer.timeit(number=1)

   
 #   plt.figure() 
 #   plt.title('Matrix Multiplication VS Hadamard Multiplication') # Tile of the graph
 #   plt.xlabel('n') # x axis label
 #   plt.ylabel('time') # Y axis label
 #   plt.plot(plotter, mm, 'b-', plotter, hm, 'r') #plot lines
 #   plt.legend(['matmult', ''], loc = 'best') # legend
 #   plt.savefig('matmulttime.pdf') # save figure






