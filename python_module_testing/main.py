import my_module as md
from math import factorial , sqrt
# from math import *

# module name eka attached krmnn one na apita.. function eka import krgnna puluwn
from my_module import add
result = add(10,20)

result = md.add(10,20)
print(f"sum is {result}")

x = 10
factorial= factorial(x)
sqrt = sqrt(x)
print(f"factorial of x is {factorial} and square root of x is {sqrt}")