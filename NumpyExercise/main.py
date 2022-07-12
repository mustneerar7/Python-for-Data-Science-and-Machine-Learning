# numpy_exercise

# import numpy library
import numpy as np

# create an array of 10 zeros
zeros = np.zeros(10)
print(zeros)

# create an array of 10 ones
ones = np.ones(10)
print(ones)

# create an array of 10 fives
fives = np.ones(10) * 5
print(fives)

# create an array of even integers 10-50
integers = np.arange(10, 51, 2)
print(integers)

# create 3x3 matrix ranging from 0 to 8
three_by_three = np.arange(0, 9).reshape(3, 3)
print(three_by_three)

# create 3x3 identity matrix
i_three = np.eye(3)
print(i_three)

# create a random number between 0 and 1
random_number = np.random.random(1)
print(random_number)

# use numpy to generate an array of
# 25 random numbers sampled from a
# standard normal distribution
random_matrix = np.random.randn(25)
print(random_matrix)

# create linearly spaced points between 0.01 and 1
linearly_spaced = np.linspace(0.01, 1, 100)
print(linearly_spaced.reshape(10, 10))

# create 20 linearly spaced points between 0 and 1
spaced = np.linspace(0, 1, 20)
print(spaced.reshape(4, 5))

# replicate given matrix outputs
mat = np.arange(1, 26).reshape(5, 5)

print(mat)
print(mat[2:, 1:])
print(mat[3, 4])

sub_matrix = np.arange(0, 3).reshape(3, 1)
sub_matrix[0, 0] = mat[0, 1]
sub_matrix[1, 0] = mat[1, 1]
sub_matrix[2, 0] = mat[2, 1]

print(sub_matrix)

# alternate way for printing 2D matrix out of slice
print(mat[:3, 1:2])

last_row = mat[4:5]
print(last_row[0])

last_two = mat[3:5, 0:5]
print(last_two)

# get sum of all values in mat
print(np.sum(mat))

# get standard deviation
print(np.std(mat))

# alternate methods
mat.sum()
mat.std()

# get sum of all columns in mat
col_sum = mat[0:5][0] + mat[0:5][1] + mat[0:5][2] + mat[0:5][3] + mat[0:5][4]
print(col_sum)

# alternate way sum of all columns
mat.sum(axis=0)


