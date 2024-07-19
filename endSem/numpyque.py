# python 
import numpy as np 
# Creating an array from a list 
arr_list = [1, 2, 3] 
arr = np.array(arr_list)
print(arr) 
# Creating an array with zeros 
zeros_arr = np.zeros((3, 3)) 
print(zeros_arr)
# Creating an array with ones 
ones_arr = np.ones((2, 2))
print(ones_arr) 
# Creating an array with a range of values 
range_arr = np.arange(0, 10, 2) 
print(range_arr)
# Creating an array with evenly spaced values 
linspace_arr = np.linspace(0, 1, 5) 
print(linspace_arr)
# Creating a random array 
random_arr = np.random.rand(2, 2) 
print(random_arr)