"""
Write a program that does the following:
Asks the user to enter in 2 numbers that can be float values
Ask the user if one of the numbers is the hypotenuse of a right triangle
Calculates the length of the missing side and rounds it to 1 decimal place.
"""
import math

first_number = float(input("Enter a number:"))
second_number = float(input("Enter a second number:"))

hyp = input("Are one of the numbers a hyp?  (yes/no): ")

if hyp == "yes":
    if first_number >= second_number:
        missing_side = math.sqrt(first_number ** 2 - second_number ** 2)
    else:
        missing_side = math.sqrt(second_number ** 2 - first_number ** 2)

        mising_side = round(missing_side, 1)

    print("The missing side of the right triangle is:", missing_side)
else:
    print("One of the numbers is the real hypotenuse of the right triangle")