#Trevor Payne Basics 7 of 8 Files and User Input

print(dir()) #returns ['__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__']
from basics7phexercises import *
print(dir()) # returns ['__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__', 'printham']
printham() #returns ham
print("\n")

import basics7phexercises as f
print(f.test2())
f.printham()