# #generate random values
# import random

# for i in range(5):
#  print(random.random())

# #to generate within a range

# for i in range(5):
#  print(random.randint(10,20))

# #randomly select a leader
# members=['john','bob','alice']
# leader=random.choice(members)
# print(leader)

# #Exercise
# class Dice:
  
#  def roll(self):   
#   first=random.randint(1,6)
#   second=random.randint(1,6)
#   return(first,second)
  
# dice1=Dice()
# print(dice1.roll())


#files and directories
#absolute path:c:\user\dell
#relative path

# from pathlib import Path
# path=Path('ecommerce')
# print(path.exists())        #boolean thst shows the existence of a path


# # to make a directory
# path=Path('ecommerce1')
# print(path.mkdir()) 

#to remove use rmdir()


from pathlib import Path
path1=Path()
print(path1.glob('*.py'))     #we can search for file and directories in current path
#*.xls   to find all spreadsheet
# *.py  to find all py files
# *.*  for all files


for file in path1.glob('*.py'):
        print(file)