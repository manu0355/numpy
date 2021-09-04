import numpy as np
#0D array
a = np.array('55')
print(a)
print(a.shape)
print(a.size)
print(a.ndim)
#1d and 2d , and 3d
a1 = np.array([1,2,3,4,5])
print(a1)
print(a1.ndim)

a2 = np.array([[1,2,3], [4,5,6]])
print(a2)
print(a2.ndim)

a3 = np.array([[[1,2],[3,4]],[[5,6],[7,8]]])
print(a3)
print(a3.ndim)

#functions
"""arange function is just like a range in python"""
ran = np.arange(10)
print(ran)

"""zeros : it is filled with zeros.syntax : (shape, dtype, order)"""
zero = np.zeros((5,5), dtype=int, order= 'C')
print(zero)

"""ones: it is filled with ones """
one = np.ones((5,5), dtype=int)
print(one)

"""linspace: creates array filled with evenly spaced values.syntax:start,stop,num"""
lin = np.linspace(5,53, num=5, dtype=int)
print(lin)

"""eye: means diagonal value equal to 1 and remaining value equalto 0"""
e = np.eye((5),k= -1, dtype = int)
print(e)

"""random: in random there are some ranodm compatibility functions
rand --> uniformly distributed values
randn--> normarlly distributed values
ranf --> uniformly distributed floating point values
randint--> uniformly distributed integer values"""

r1 = np.random.rand(5)
print(r1)
r2 = np.random.randn(5)
print(r2)
r3 = np.random.ranf(5)
print(r3)
r4 = np.random.randint(5)
print(r4)