x = 10
y = x
x = "20"
z = int(x)
result = str(y) + x
final_result = int(result) + z
print(x)        #20  
print(y)        #10
print(z)        #20
print(result)       #1020
print(final_result)     #1040

# Also answer:
# 1. Why does the value of y remain unchanged when x is reassigned?
'''
    solution
    In Python, integers and strings are immutable (cannot be changed in place). When you write y = x, y points directly to the integer object 10 that x was pointing to.
    When you later reassign x = "20", you are not altering the number 10 itself. Instead, you are breaking x's old link and forcing it to point to a completely new string object ("20"). y safely retains its original pointer to the integer 10.
'''

# 2. What would happen if x = "20.5" instead of x = "20"?
'''
    The program would crash with a ValueError at the line z = int(x).
    The int() function can convert a string to an integer only if the string contains a valid, whole base-10 number. Because "20.5" contains a decimal point, int() does not know how to parse it directly.
'''
