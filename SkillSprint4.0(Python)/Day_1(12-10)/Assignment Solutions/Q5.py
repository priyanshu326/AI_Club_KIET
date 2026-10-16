# Question 5: Variable Reassignment and Type Conversion
# Predict the output.

a = 4
b = "3"
a = a + int(b)
b = str(a) + b
print(a)        #Output is 7
print(b)        #Output is 73
print(type(a))      #Output is <class 'int'>
print(type(b))      #Output is <class 'str'>