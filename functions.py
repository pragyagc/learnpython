# def greet_user():
#     print('hi there')
#     print('welcome aboard')

# print('start')
# greet_user()
# print("finish")

# def greet_user(name):
#     print(f'hi {name}')
#     print('welcome aboard')
# greet_user("pragya")

# #passing multiple parameters
# def greet_user(firstname,lastname):
#     print(f'hi {firstname}  {lastname}')
#     print('welcome aboard')
# greet_user("pragya","gc")

# #keyword argument
# greet_user(lastname="gc",firstname="pragya") #doesnt concern the position of the parameter
# #calc_cost( total =50, shipping=5, discount=0.1) #improve realability of code

# #Note  -we should use positional agruments before keyword arguments
# # greet_user(firstname="pragya","gc") error
# greet_user("pragya",lastname="gc")  #correct




# #RETURN STATEMENT

# def square(number):
#    return number*number
# result=square(4)
# print(result)

#nOTE- by default python return none
def emoji_converter(message):
 words=message.split(' ')
 print(words)
 emojis={
    ":)":"😊",
     ":(":"😔",

 }
 output=""
 for word in words:
   output+= emojis.get(word,word) +" "
 return output

message=input(">")
print(emoji_converter(message))