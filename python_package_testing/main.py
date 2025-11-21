# from my_calculator import adddition, subtraction

# print(adddition.add(5, 3))
# print(subtraction.substract(10, 4))

# we have to use package name here
# import my_calculator.addition 
# import my_calculator.substraction

# we have to use module name here
# from my_calculator import add
# from my_calculator import substract

# only we can use function name here
# from my_calculator.addition import add
# from my_calculator.substraction import substract

# we have defined the module names in init.py
from my_calculator import add , substract

sum = add(10,2)
difference = substract(10,2)

print(f"sum of numbers is {sum} difference of number is {difference}")