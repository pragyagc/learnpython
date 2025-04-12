#importing entire module
import converters
print(converters.kg_to_lbs(70))

#importing specific function
import converters
from converters import kg_to_lbs

print(converters.kg_to_lbs(70))

#to find largest number in a list
from converters import find_max

numbers=[2,4,6,1,8,9,3]
max=find_max(numbers)
print(max)

# #import entire module
# import ecommerce.shipping
# ecommerce.shipping.calc_shipping()

# from ecommerce import shipping
# shipping.calc_shipping()

from ecommerce.shipping import calc_shipping
calc_shipping() 
