class Point:
    def __init__(self,x,y):
        self.x=x
        self.y=y
    def move(self):
        print('move')

    def draw(self):
        print('draw')

point1 = Point()
point1.x=10
print(point1.x)
point1.draw()

#constructors
point=Point(10,20)
point.x=11
print(point.x)


#Exercise
class Person:
    def __init__(self,name):
        self.name=name
    def talk(self):
        print(f'hi,i am {self.name}')

person1=Person("john smith")
person1.talk()
print(person1.name)


#INHERITANCE
class Mammal:
    def walk(self):
         print('walk')
class Dog(Mammal):
    def bark(self):
        print('bark')

# # for no overriding
# class Cat(Mammal):
#     pass
 
class Cat(Mammal):
    def sound(self):
        print('meow')
dog1=Dog()
dog1.walk()
dog1.bark()
cat1=Cat()
cat1.sound()




