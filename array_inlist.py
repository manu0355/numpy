import numpy as np

my_list = [1,2,3,4,5,6]
arr = np.array(my_list)
for ele in arr:
    print(ele, end= " ")

my_list = [[1,2,3], [4,5,6]]
matrix = np.array(my_list)
for ele in matrix:
    for row in ele:
        print(row, end=" ")

"""submatrix from matrix using slicing
slicing syntax: [row_lower:row_upper, col_lower:col_upper]"""
list1 = [[10,20,30], [40,50,60], [70,80,90]]
matrix = np.array(list1)
print(matrix[0,1])

"""creating one dimensions array"""
n = int(input("enter n value:"))
arr = np.ndarray(shape = (n), dtype = int)
for i in range(n):
    arr[i] = int(input())
print(arr)