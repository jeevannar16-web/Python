# =====================================================================
# 1. BASIC ARITHMETIC CALCULATOR FUNCTIONS
# =====================================================================

def add(a, b):
    """Returns the sum of two numbers."""
    return a + b  

def subtract(a, b):
    """Returns the difference of two numbers."""
    return a - b

def multiply(a, b):
    """Returns the product of two numbers."""
    return a * b    

def divide(a, b):
    """Returns the quotient of two numbers. Safe handles division by zero."""
    if b != 0:
        return a / b
    else:
        return "Error: Division by zero"

# Testing Calculator Functions
print("--- Calculator Tests ---")
print("Add (5 + 3):", add(5, 3))          # Output: 8
print("Subtract (5 - 3):", subtract(5, 3)) # Output: 2
print("Multiply (5 * 3):", multiply(5, 3)) # Output: 15
print("Divide (5 / 3):", divide(5, 3))     # Output: 1.6666666666666667
print("Divide (5 / 0):", divide(5, 0))     # Output: Error: Division by zero
print("\n")


# =====================================================================
# 2. STUDENT GRADING FUNCTION
# =====================================================================

def student_result(marks):
    """Evaluates numeric marks and returns the corresponding letter grade."""
    if marks >= 90:
        return "Grade: A"
    elif marks >= 80:
        return "Grade: B"
    elif marks >= 70:
        return "Grade: C"
    elif marks >= 60:
        return "Grade: D"
    else:
        return "Grade: F"

# Testing Grading Function
print("--- Grading Tests ---")
print("Marks = 85:", student_result(85))  # Output: Grade: B
print("Marks = 55:", student_result(55))  # Output: Grade: F
print("\n")


# =====================================================================
# 3. GREATEST OF THREE NUMBERS FUNCTIONS
# =====================================================================

def greatest_of_three(a, b, c):
    """Finds the greatest number using standard comparison logic."""
    if (a >= b) and (a >= c):
        return a
    elif (b >= a) and (b >= c):
        return b
    else:
        return c

def greatest_of_three_user(a, b, c):
    """An alternative variation to calculate the greatest of three numbers."""
    if a >= b and a >= c:
        return a
    elif b >= a and b >= c:
        return b
    else:
        return c

# Testing Comparison Functions with hardcoded values
print("--- Comparison Tests ---")
print("Greatest of (10, 25, 15):", greatest_of_three(10, 25, 15))        # Output: 25
print("Greatest of (100, 45, 87):", greatest_of_three_user(100, 45, 87)) # Output: 100