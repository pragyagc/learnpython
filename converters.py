def kg_to_lbs(kg):
    return kg*2.20462

def lbs_to_kg(lbs):
    return lbs/2.20462

def find_max(numbers):
 largest = numbers[0]
 for x in numbers:
  if x > largest: 
    largest=x 
 return largest

#max- built in function
numbers=[10,3,4,5]
print(max(numbers))

#note- max has been already defined in line 20 ..in line 21 it wont call built in function
numbers=[10,3,11,5]
max=find_max(numbers)
print(max)