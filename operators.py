#arithmetic operators
print(10+3)
print(10/3)

# for ineteger
print(10//3)

#modulus
print(10%3)

#exponent
print(10**2)

x=10
x=x+3
print(x)

#augmented assignment opeartor
x+=3
print(x)



#OPERATor precedence
x=10+3*2**2
print(x)
#parenthesis - highest precendence
x=(10+3)*2**2
print(x)

#math functions
x=2.8
# round off value
print(round(x))
#absolute value
print(abs(-2.9))





#logical operator
A=False
B=False

if A  and B:
 print('c')
if A or B:
 print('d')

 #example 
has_good_manner=True
smokes=False
if has_good_manner and not smokes:
 print("good man")





#Comparison operator
#example 1
 temperature=35

 if temperature > 30:
  print("its  hot day")
 else:
  print("its not a hot day")

  #example 2
name ='pragya'
if len(name) < 3:
   print("name must be at least3 cahracter")
elif len(name) > 50:
   print("name must be a maximum of 50 character")
else:
   print("name look good")