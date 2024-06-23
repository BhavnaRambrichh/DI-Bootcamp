#Create a vector* of zeros with size 10 using np.zeros()

import numpy as np

vector_of_zeros = np.zeros(10)

print(vector_of_zeros)

#Compute the memory size* of any array. 
# Note: You can do this by multiplying the length of the array by 
# the size of one array element, which you can find using the .itemsize attribute.

#Example output: `80` (for an array of size 10 with elements of type float64)

import numpy as np

float_array = np.array([1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0, 9.0, 10.0])

# Find the size of one element in bytes
element_size = float_array.itemsize

# Find the number of elements in the array
num_elements = float_array.size

# Compute the total memory size
total_memory_size = num_elements * element_size

print(f"Memory size of the array: {total_memory_size} bytes")

#Retrieve the documentation of the numpy add function from the command line.
#Create a vector with values ranging from 10 to 49 using np.arange().
#Example output: [10 11 12 ... 47 48 49]

# Create a vector with values ranging from 10 to 49
help(np.add)

vector = np.arange(10, 50)
print(vector)

#Reverse a vector so the first element becomes last (Hint: Use slicing).
print(vector[::-1])

#Create a 3x3 matrix* with values ranging from 0 to 8 using np.reshape().

array = np.array([0,1,2,3,4,5,6,7,8])
matrix = np.reshape (array,(3,3))
print(matrix)

#Find indices of non-zero elements from [1,2,0,0,4,0] using np.nonzero().
indices = np.array([1, 2, 0, 0, 4, 0])
non_zero_indices = np.nonzero(indices)
print(non_zero_indices)


#Create a 3x3 identity matrix* using np.eye().
identity_matrix = np.eye(3)

print(identity_matrix)

#Create a 5x5 matrix with row values ranging from 0 to 4
#The output should be a matrix where each row is [0, 1, 2, 3, 4]

row_vector = np.tile(np.array([0, 1, 2, 3, 4]), (5, 1))

print(row_vector)

#Create a vector of size 10 with values ranging from 0 to 1, both excluded. 
# You can use np.linspace.

sequence = np.linspace(0, 1, 12)[1:-1]

print(sequence)

#Create a random vector of size 10 and sort it.
random_numbers = np.random.rand(10)

sorted_numbers = np.sort(random_numbers)

print(random_numbers)

#Print the minimum and maximum representable value for each numpy scalar type* (int8, int32, int64, float32, float64). 
# Use np.iinfo and np.finfo.


# Integer types
int_types = [np.int8, np.int32, np.int64]

print("Integer Types:")
for dtype in int_types:
    info = np.iinfo(dtype)
    print(f"{dtype.__name__}: min={info.min}, max={info.max}")

# Floating-point types
float_types = [np.float32, np.float64]

print("\nFloating-Point Types:")
for dtype in float_types:
    info = np.finfo(dtype)
    print(f"{dtype.__name__}: min={info.min}, max={info.max}")

#How to convert a float (32 bits) array into an integer (32 bits) in place? 
# Use np.ndarray.astype.

float_array = np.array([1.5, 2.3, 3.7, 4.1, 5.9], dtype=np.float32)

print("Original float array:", float_array)

float_array = float_array.astype(np.int32, copy=False)

print("Converted integer array:", float_array)

#Subtract the mean* of each row of a matrix. Use np.mean with axis=1.
matrix = np.array([[1, 2, 3],
                   [4, 5, 6],
                   [7, 8, 9]])

# Calculate the mean of each row
row_means = np.mean(matrix, axis=1, keepdims=True)

# Subtract the mean of each row from the original matrix
normalized_matrix = matrix - row_means

# Print the resulting normalized matrix
print(normalized_matrix)

#How to sort an array by the nth column? Use np.argsort.

array = np.array([[1, 4, 2],
                  [3, 1, 5],
                  [6, 2, 4]])

n = 1

sorted_indices = np.argsort(array[:, n])

sorted_array = array[sorted_indices]

print("Original array:\n", array)
print("\nSorted array by the", n+1, "th column:\n", sorted_array)

#How to swap two rows of an array? You can do this using array indexing.
array = np.array([[1, 4, 2],
                  [3, 1, 5]])
# Print the original array
print("Original array:\n", array)

# Swap rows (e.g., swap row 0 and row 1)
array[[0, 1]] = array[[1, 0]]

# Print the array after swapping rows
print("\nArray after swapping rows 0 and 1:\n", array)

#Given an array C that is a bincount*, how to produce an array A such that np.bincount(A) == C? 
# Use np.repeat.

# Given bincount array C
C = np.array([2, 0, 1, 1, 0, 1])

# Generate array A such that np.bincount(A) == C
A = np.repeat(np.arange(len(C)), C)

# Print array A
print("Array A:", A)

# Verify np.bincount(A) == C
print("np.bincount(A):", np.bincount(A))
