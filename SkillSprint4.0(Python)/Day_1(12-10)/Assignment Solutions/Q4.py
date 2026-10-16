'''
    Question 4: Debug a Type-Conversion and Eligibility Program

    A training institute offers admission if a student's marks are at least 60 and the student has paid a registration fee of at least Rs. 1,000. The following program is intended to implement the rule, but it contains mistakes.

    marks = input("Enter marks: ")
    fee = input("Enter registration fee: ")
    if marks >= 60 and fee >= 1000:
        print("Admission Granted")
    else:
        print("Admission Denied")

    Tasks:
    1. Identify why the program does not work as intended.
    2. Correct the program without changing the admission rules.
    3. Explain how the corrected program handles the inputs 60 and 1000.
'''

# Solution
'''
    1. Why the Program Does Not Work
    The main issue is a Type Error caused by input():
        In Python, whatever the user types using input() is always saved as text (a string), even if they type numbers.
        In the original code, the program tries to compare text with numbers (marks >= 60 and fee >= 1000). Python doesn't know how to compare text with a math number, so it crashes and gives a TypeError.
'''

'''Correct Program'''

marks = int(input("Enter marks: "))
fee = int(input("Enter registration fee: "))

if marks >= 60 and fee >= 1000:
    print("Admission Granted")
else:
    print("Admission Denied")
    
'''
    3. How the Corrected Program Handles Inputs 60 and 1000
    If a student enters 60 for marks and 1000 for the fee, here is step-by-step how the computer handles it:
        1.Conversion: int() changes the text "60" into the actual number 60, and "1000" into the number 1000.
        2.First Condition (marks >= 60): The computer checks 60 >= 60, which is True.
        3.Second Condition (fee >= 1000): The computer checks 1000 >= 1000, which is also True.
        4.Final Check (and operator): Since both conditions are True (True and True), the final result is True.
        5.Output: The program successfully prints "Admission Granted".
'''
