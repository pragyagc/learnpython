import numpy as np
a= np.array([[1,2,3,4,5],[6,7,8,9,10]])
print(a[0][0])

#initializing diffrent types of array
#all 0s matrix
a=np.zeros(5)
print(a)

c=np.zeros((2,3))
print(c)

#for all 1
b=np.ones((4,2,2))
print(b)

a=np.full((1,1),99) # all matrix element will be 99
print(a)

#any other numbr(full_like)
d=np.array([1,2,3,4])
print(np.full_like(d,4)) #this wont alter array d
print(d)
#or 
print(np.full(d.shape,4))

#matrix of random decimal numbers
s=np.random.rand(4,2)
print(s)

#for a shape of an array
print(np.random.random_sample(a.shape))

#random integer values
print(np.random.randint(7,size=(3,3))) #with integer 0-7 
#or
print(np.random.randint(0,7,size=(3,3)))

a=np.identity(5)
print(a)
arr=np.array([1,2,3])
r1=np.repeat(arr,3)
print(r1)

arr=np.array([[1,2,3]])
r1=np.repeat(arr,3,axis=0)
print(r1)


output=np.ones((5,5))
print(output)
z=np.zeros((3,3))
z[1,1]=9
print(z)
output[1:4,1:4]=z
print(output)




########
import numpy as np

b = np.array([[1.0,2.0,3.0],[3.0,4.0,5.0]])
print(b)


a = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])

print(np.full_like(a, 100))

#all zeros matrix
a = np.zeros((3, 4))
print(a)

#all ones matrix
a = np.ones((3, 4))
print(a)

#all 1s matrix
n = np.ones((3,2,2))
print(n)

#any other number matrix
a = np.full((3, 4), 5, dtype=float)
print(a)

 #random matrix
a = np.random.rand(3, 4)
print(a)

#random integer matrix
a = np.random.randint(10, size=(3, 4))
print(a)

i=np.ones((5,5))
j=np.zeros((3,3))
j[1,1]=9
i[1:-1, 1:-1] = j
print(i)


output = np.zeros((7,7))
z = np.ones((5, 5))
z[1, 1] = 5
output[1:-1, 1:-1] = z
print(output)


a = np.array([1, 2, 3, 4, 5])
b = a
b[2] = 20
print(b)  # a is also changed because b is a reference to a

c = np.array(([1, 2, 3, 4, 5], [6, 7, 8, 9, 10]))
d = np.max(c, axis=1).sum()
print(d)  # 5 because a is a 1D array, axis=1 is not valid for 1D arrays


a = np.ones((2, 4))
b = a.reshape((4, 2))
print(b)

a = np.ones((2, 4))
b = a.reshape((2, 4))
print(b)


a = np.ones((2, 4))
b = a.reshape((8, 1))
print(b)




#exercise
a = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])
print(np.full_like(a, 100))

output = np.zeros((7,7))

z = np.ones((5, 5))
z[2, 2] = 5

output[1:-1, 1:-1] = z
print(output)

a = np.array([1, 2, 3, 4, 5])
b = a
b[2] = 20
print(b)  # a is also changed because b is a reference to a

c = np.array(([1, 2, 3, 4, 5], [6, 7, 8, 9, 10]))
d = np.max(c, axis=1).sum()
print(d)  # 5 because a is a 1D array, axis=1 is not valid for 1D arrays


a = np.ones((2, 4))
b = a.reshape((4, 2))
print(b)

a = np.ones((2, 4))
b = a.reshape((2, 4))
print(b)


a = np.ones((2, 4))
b = a.reshape((8, 1))
print(b)