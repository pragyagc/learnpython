#Create a dictionary with keys as the names of three countries and values as their capitals. Print the capital of a specific country.
countries = {
    'Nepal':'Kathmandu',
    'Australia':'Canberra',
    'USA':'Washington D.C.'
}

#Concatenate the strings `"Hello, "` and `"World!"` and print the result.
print("Hello, " + "World!")

#Create a string `sentence` with the value `"Python programming is fun!"`. Replace the word `"fun"` with `"awesome"` and print the result.
sentence = "Python programming is fun!"
sentence = sentence.replace("fun","awesome")
print(sentence)

#Use a for loop to iterate over a dictionary and print each key and value.
for country,capital in countries.items():
    print(f'{country} : {capital}')


#Write a while loop that prints the squares of numbers from 1 to 5.
num = 1
while num <=5:
    print(num * num)
    num = num + 1

#Write a function `sum_list` that takes a list of numbers as an argument and returns their sum.
numbers = [1,2,3,4,5]
def sum_list(nums):
    sum = 0
    for num in nums:
        sum = sum + num
    return sum
   
print(sum_list(numbers))

#Create a function `is_prime` that takes a number as an argument and returns `True` if the number is prime and `False` otherwise.
def is_prime(num):
    prime = True
    for i in range(2,num//2):
        if num % i == 0:
            prime = False
            break
    return prime

is_prime(4)

#Define a class `Student` with attributes `name` and `grade`. Include a method `display_info` that prints the student's name and grade.
class Student:
    def __init__(self,name,grade):
        self.name = name
        self.grade = grade

    def display_info(self):
        print(f'Name:{self.name}, grade:{self.grade}')

#Create an instance of the `Student` class and update the student's grade. Call the `display_info` method to display the updated information.
s = Student('Ujjwal','A+')
s.display_info()


#Create a set with the numbers 1, 2, 3, 4, and 5. Add the number 6 to the set and print the updated set.
s = {1,2,3,4,5}
s.add(6)
print(s)



#Create another set with the numbers 4, 5, 6, 7, and 8. Find the intersection of the two sets and print the result.
s2 = set((4, 5, 6, 7, 8))
s.intersection(s2)