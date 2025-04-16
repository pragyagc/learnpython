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