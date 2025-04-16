#Define a variable `age` and set it to your age.
age = 21

#Create a dictionary with your name, age, and favorite color. Print your favorite color from the dictionary.
profile = {
    'name':'Pragya G.C',
    'age':21,
    'favorite_color':'lavender'
}
#Write a script that checks if a number is positive, negative, or zero and prints an appropriate message.
number = 5
if number > 0:
    print('positive')
if number < 0:
    print('negative')
if number == 0:
    print('zero')

#Create a nested if-else statement that checks if a number is even or odd and then checks if it is greater than 10 or not.
number = 5
if number % 2 == 0:
    print('even number')
    if number > 10:
        print('greater than 10')
    else:
        print('less than 10')
else:
    print('odd number')
    if number > 10:
        print('greater than 10')
    else:
        print('less than 10')

#Write a function `greet` that takes a name as an argument and prints "Hello, [name]!".
def greet(name):
    print(f'Hello, {name}')

greet('pragya')


#Create a function `factorial` that takes a number as an argument and returns its factorial.
def factorial(num):
    product = 1
    for i in range(1,num+1):
        product = product * i
    return product

factorial(3)

#Define a class `Book` with attributes `title` and `author`. Include a method `display_info` that prints the book's title and author.
class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
    
    def display_info(self):
        print(f"Title: {self.title}, Author: {self.author}")


#Import Pandas and create a DataFrame from a dictionary where keys are column names and values are lists of column data.
import pandas as pd
profiles = {
    'name':['Ram','Hari','Shyam','Bibek','sambhu'],
    'age':[30,25,32,20,21],
    'salary':[100000,60000,50000,32000,30000]
}
df = pd.DataFrame(profiles)
print(df)