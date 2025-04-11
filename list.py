names=['pragya','bob','mary','god','live'] 
print(names[2]) 
print(names[1:]) 

#replace
names[1]='bib'

print(names) 

#print largest no of list
numbers=[1,2,3,9,5,6] 
largest = numbers[0]


for x in numbers:
  if x > largest: 
    largest=x 
    print(f'largest number:{largest}') 
    
    
    
#2D LIST
matrix=[[1,2,3],[4,5,6],[7,8,9]]
print(matrix[1][2])

for row in matrix:
  for item in row:
    print(item)

#list methods
numbers=[5,2,1,7,4]
numbers.append(10)  #for appending value in list
numbers.insert(0,6) # for inserting with certain index
numbers.remove(5)   # for removing
#numbers.clear()     # to remove every  elements of list
numbers.pop()       # to pop out last element of list
print(numbers)
print(numbers.index(2))  # to find out index of given number

#check existence of item
print(7 in numbers)

#to show count of given numbers
numbers.append(7)
print(numbers.count(0))

numbers.sort()
print(numbers)

#for descending order
numbers.reverse()
print(numbers)

#copy of a list
numbes2=numbers.copy()
print(numbes2)

#program to remove the duplicates in a list
list1=[1,2,3,1,4,5,4]
uniques=[]
for number in list1:
  if number not in uniques:
    uniques.append(number)
print(uniques)


#tuple
numbers=(1,2,3)
# note - tuples are immutable

#unpacking
coordinates=(1,2,3)
# x=coordinates[0]
# y=coordinates[1]
# z=coordinates[2]
#similar way
x,y,z =coordinates
print(y)