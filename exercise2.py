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