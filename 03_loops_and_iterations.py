# =====================================================================
# 1. BASIC FOR LOOPS & RANGE VARIATIONS
# =====================================================================

print("--- Range 1 to 10 (Inclusive) ---")
for i in range(1, 11):
    print(i, end=" ")
print("\n")

print("--- Range 0 to 9 (Default Start) ---")
for i in range(10):
    print(i, end=" ")
print("\n")

print("--- Range 1 to 10 with Step 2 (Odds Only) ---")
for i in range(1, 11, 2):
    print(i, end=" ")
print("\n")

print("--- Compact Horizontal String Join (1 to 10) ---")
print(" ".join(str(i) for i in range(1, 11)))
print("\n")


# =====================================================================
# 2. MATHEMATICAL ACUMULATORS & TABLES
# =====================================================================

# Sum of first 5 natural numbers (1 + 2 + 3 + 4 + 5)
total = 0
for i in range(1, 6):
    total += i
print(f"Sum of first 5 natural numbers: {total}")
print("\n")

# Multiplication Table Generation
num = 5  # Initialized value to prevent NameError
print(f"--- Multiplication Table of {num} ---")
for i in range(1, 11):
    print(f"{num} x {i} = {num * i}")   
print("\n")


# =====================================================================
# 3. NESTED LOOPS: PATTERN GENERATION
# =====================================================================

# Generates an 'X' shape matrix horizontally, vertically, and diagonally
size = 5
print(f"--- {size}x{size} Matrix X Pattern ---")
for i in range(size):
    for j in range(size):
        # i == j catches the main diagonal (\)
        # i + j == size - 1 catches the anti-diagonal (/)
        if i == j or i + j == size - 1:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()  # Moves to the next line after completing a row
print("\n")


# =====================================================================
# 4. REUSABLE FUNCTION MODALITIES
# =====================================================================

def print_multiplication_table(table_num):
    """Generates a clean multiplication matrix for any number passed into it."""
    print(f"--- Function Table for {table_num} ---")
    for i in range(1, 11):
        print(f"{table_num} x {i} = {table_num * i}")


def odd_even(check_num):
    """Evaluates an integer and returns its numeric parity classification."""
    if check_num % 2 == 0:
        return "Even"
    else:
        return "Odd"


# Testing the functions
print_multiplication_table(7)
print()
print(f"The number 42 is: {odd_even(42)}")
print(f"The number 71 is: {odd_even(71)}")