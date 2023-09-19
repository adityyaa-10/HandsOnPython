a = 5
b = 3 

print(a+b)  # 8 
print(a-b)  # 2
print(a*b)  # 15 
print(a/b)  # 1.666666667
print(a%b)  # 2
print(a//b) # 1 5 divided by 3 with only integer parts
print(a**b) # 125 --> 5 raised to the power 3

"""
This is a multi line comment
"""

"""
It's worth noting that while these docstrings are a common way to create multi-line comments,
they are not true comments in the sense that they won't be optimized away by the Python interpreter.
They will be stored as strings in memory if not used as docstrings. If you want to include comments for documentation purposes,
it's better to use them as docstrings. If you want to add comments that wont
be included in the documentation and will be optimized away, you should stick to single-line 
# comments.
"""

# Arithmetic Operators -> +,-,*,...
# Assignment Operators -> =,/=,*=,+= ....
# Comparison Operators -> ==, <=, >=, >, < ....
# Logical Operators --> and, or, not ... 