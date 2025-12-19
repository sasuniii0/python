#print(10/0)
# ZeroDivisionError: division by zero

#========================================================================

#print(my_variable)
# NameError: name 'my_variable' is not defined

#========================================================================

# import pdb;

# print('started')
# x = 5

# pdb.set_trace()

# y = 0

# z = x/y
# print('finished')

#========================================================================

print('start')
x = 5

breakpoint()

y=0

z = x/y
print('finish')