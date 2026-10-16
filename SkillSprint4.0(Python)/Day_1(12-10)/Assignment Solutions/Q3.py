'''
    Question 3: Find the Hidden Logical Error

    A college determines whether a student passes using these rules:
        - Marks must be at least 40.
        - Attendance must be at least 75%.
        - If marks are at least 90, attendance is not required.
    A student writes the following program:
    
        marks = int(input("Enter marks: "))
        attendance = float(input("Enter attendance: "))
        if marks >= 40 and attendance >= 75 or marks >= 90:
            print("Pass")
        else:
            print("Fail")

        Task: Is the program logically correct? If not, identify the issue, correct the program, and demonstrate
        a test case that exposes the error.
'''
#Solution:

'''
    1. Is the program logically correct?
    Strictly speaking, the computer executes it without crashing, but the logic is poorly structured and risky.
    Because there are no brackets (parentheses) separating the and and or conditions, it relies entirely on Python's hidden operator precedence rules (where and is checked before or). This makes the code confusing to read and prone to logical mistakes.
'''

'''
    2. What is the Issue?
    Lack of Grouping: When mixing and and or in a single line without parentheses, it is hard for a human reader to tell what condition overrides what.
    Intended vs. Actual Logic: The rule says: "Marks must be at least 40 AND attendance at least 75%, OR if marks are at least 90, attendance doesn't matter."
    To make this rule crystal clear and foolproof, the conditions must be grouped using parentheses ( ) so the computer checks them in the exact order we want.
'''

'''Correct Program'''
marks = int(input("Enter marks: "))
attendance = float(input("Enter attendance: "))

if (marks >= 40 and attendance >= 75) or (marks >= 90):
    print("Pass")
else:
    print("Fail")

'''
4. Demonstrating a Test Case
    Let’s test the program with a student who has high marks but low attendance:
    Input Test Case:
    marks = 95
    attendance = 50 (which is less than 75%)

    How the Corrected Program Evaluates It:
    First bracket (marks >= 40 and attendance >= 75): 95 >= 40 is True, but 50 >= 75 is False. So this whole bracket is False.
    Second bracket (marks >= 90): 95 >= 90 is True.
    The or operator checks: False or True, which results in True.

    Output: Pass (because getting 90+ marks waives the attendance requirement!).
'''
