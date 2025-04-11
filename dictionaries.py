

customer={
    "name":"pragya gc",
    "age":21,
    "is_verified":True
}
print(customer["name"])
print(customer.get("name"))
 #for default values :
print(customer.get("birthyear"))
print(customer.get("birthyear","2003"))

customer["name"]="gangubai"
print(customer["name"])
customer["birthdate"]="nov 3 2003"
print(customer["birthdate"])

# #exercise to translte digit into word
# phone=input("phone number")
# mapping={
#     "1":"one",
#     "2": "two",
#     "3": "three",
#     "4": "four",
#     "5": "five",
#     "6": "six",
#     "7": "seven",
#     "8": "eight",
#     "9": "nine",
#     "0":"zero"

# }
# output=""
# for num in phone:
#    output+= mapping.get(num) +" "
# print(output)


#emoji converter
message=input(">")
words=message.split(' ')
print(words)
emojis={
    ":)":"😊",
     ":(":"😔",

}
output=""
for word in words:
   output+= emojis.get(word,word) +" "

print(output)
