class Dress:
    def __init__(self, color, style, size):
        self.color = color
        self.style = style
        self.size = size
    
    def change_color(self, new_color):
        self.color = new_color
        print(f"The dress color has been changed to {self.color}.")
    
    def change_style(self, new_style):
        self.style = new_style
        print(f"The dress style has been changed to {self.style}.")
    
    def change_size(self, new_size):
        self.size = new_size
        print(f"The dress size has been changed to {self.size}.")
    
    def describe(self):
        print(f"This dress is {self.color}, {self.style} style, and size {self.size}.")
        
if __name__ == "__main__":
    dress1 = Dress("blue", "A-line", "M")
    dress1.describe()

    dress1.change_color("red") 
    dress1.change_style("maxi")  
    dress1.change_size("L")  

    dress1.describe() 
    
    
    
"""
OUTPUT:

This dress is blue, A-line style, and size M.
The dress color has been changed to red.
The dress style has been changed to maxi.
The dress size has been changed to L.
This dress is red, maxi style, and size L.
"""




class Dress:
    def __init__(self, color, style, size):
        self.color = color
        self.style = style
        self.size = size
    
    def is_formal(self):
        if self.style.lower() in ['gown', 'suit']:
            return True
        else:
            return False
    
    def is_colorful(self):
        if len(self.color) > 5:
            return True
        else:
            return False
    
    def increase_size(self):
        if self.size.isnumeric():
            self.size = str(int(self.size) + 1)
    
    def print_color_letters(self):
        for letter in self.color:
            print(letter)

if __name__ == "__main__":
    dress1 = Dress("blue", "A-line", "M")
    print(f"Is dress formal? {dress1.is_formal()}")  
    print(f"Is dress colorful? {dress1.is_colorful()}")  
    dress1.increase_size()
    print(f"Dress size after increase: {dress1.size}") 
    print("Letters in dress color:")
    dress1.print_color_letters()  
    

""" 
OUTPUT:
Is dress formal? False
Is dress colorful? False
Dress size after increase: M
Letters in dress color:
b
l
u
e
"""   


import math
import datetime
import random

print(math.sqrt(25))  
print(datetime.datetime.now()) 
print(random.randint(1, 10)) 

""" 
OUTPUT:
5.0
2024-04-18 13:44:27.324876
2
"""


