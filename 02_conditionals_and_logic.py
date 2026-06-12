# =====================================================================
# 1. CONDITIONAL GRADING SYSTEM
# =====================================================================

# Prompts user for score and evaluates the traditional letter grade
marks = int(input("Enter your marks: "))

if marks >= 90:
    print("Grade: A")
elif marks >= 80:
    print("Grade: B")
elif marks >= 70:
    print("Grade: C")
elif marks >= 60:   
    print("Grade: D")
else:   
    print("Grade: F")  


# =====================================================================
# 2. GREATEST OF THREE NUMBERS (SCRIPT APPROACH)
# =====================================================================

# Test Case 1: Hardcoded Values
a = 10
b = 25
c = 15

if (a >= b) and (a >= c):
    greatest = a
elif (b >= a) and (b >= c):
    greatest = b
else:
    greatest = c

print(f"The greatest number (hardcoded) is: {greatest}")


# Test Case 2: Dynamic User Inputs
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
num3 = int(input("Enter third number: "))

if (num1 >= num2) and (num1 >= num3):
    result = num1
elif (num2 >= num1) and (num2 >= num3):
    result = num2
else:
    result = num3

print(f"The greatest number (user input) is: {result}")


# =====================================================================
# 3. GREATEST OF THREE NUMBERS (FUNCTION-BASED APPROACH)
# =====================================================================

def greatest_of_three(x, y, z):
    """Evaluates three numbers and returns the largest value."""
    if (x >= y) and (x >= z):
        return x
    elif (y >= x) and (y >= z):
        return y
    else:
        return z

# Execution test using hardcoded values inside the function
print(f"The greatest number via function is: {greatest_of_three(10, 25, 15)}")


# Execution test using fresh user inputs passed to the function
user_a = int(input("Enter function first number: "))
user_b = int(input("Enter function second number: "))
user_c = int(input("Enter function third number: "))

final_greatest = greatest_of_three(user_a, user_b, user_c)
print(f"The greatest number from user function input is: {final_greatest}")


# =====================================================================
# 4. UTILITY FUNCTIONS
# =====================================================================

def multiplication_table(num):
    """Generates and prints a multiplication table up to 10 for any given integer."""
    for i in range(1, 11):
        print(f"{num} x {i} = {num * i}")