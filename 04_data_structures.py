# lists and Disctionaries
# dictnory 3.7 before order was not preserved but after 3.7 order is preserved
# Defination of Dictionary:
# A dictionary is a collection of key-value pairs where each key is unique and maps to a value. It is an unordered, mutable data structure that allows for fast lookups based on keys.

marks = [85, 90, 78, 92, 88]
print("Marks:", marks)
print("First mark:", marks[0])
print("Last mark:", marks[-1])  

print("All marks:")
print("Higest mark:", max(marks))
print("Lowest mark:", min(marks))
print("Average mark:", sum(marks) / len(marks))


print(marks[1:4])


# Store Student data (dictionary)
student = {
    "name": "Alice",
    "age": 20,
    "marks": [85, 90, 78],
    "passed": True
}
print("Student Name:", student["name"])
print("Student Age:", student["age"])
print("Student Marks:", student["marks"])
print("Student Passed:", student["passed"]) 



# Multiple Students data (list of dictionaries)


# Key value pairs in a dictionary
students = [
# {"name": "Alice", "age": 20, "marks": [85, 90, 78], "passed": True},
# {"name": "Bob", "age": 22, "marks": [75, 80, 70], "passed": True},
# {"name": "Charlie", "age": 19, "marks": [60, 65, 55], "passed": False}
]

print("Students Data:")
# print(students)


for s in students:
    print(f"Name: {s['name']}, Age: {s['age']}, Marks: {s['marks']}, Passed: {s['passed']}")
    print(s['name'], s['age'], s['marks'], s['passed'])




# 1.list:Ordered, mutable, allows duplicates

# Defination of list: A list is an ordered collection of items that can be of different types. It is mutable, meaning you can change its contents after it has been created, and it allows for duplicate elements.

my_list = [1, 2, 3, 4, 5]
my_list.append(6)  # Adding an element
print(my_list)  # Output: [1, 2, 3, 4, 5, 6]



# 2.Tuple:Ordered, immutable, allows duplicates

# Defination of tuple: A tuple is an ordered collection of items that can be of different types. It is immutable, meaning you cannot change its contents after it has been created, and it allows for duplicate elements.

my_tuple = (1, 2, 3, 4, 5)
# my_tuple[0] = 10  # This will raise an error because tuples are immutable, commented for safety
print(my_tuple)  # Output: (1, 2, 3, 4, 5)



# 3.Set:Unordered, mutable, no duplicates

# Defination of set:

# A set is an unordered collection of unique items. It is mutable, meaning you can change its contents after it has been created, but it does not allow for duplicate elements. Sets are commonly used for storing unique values and performing operations like union, intersection, etc.
my_set = {1, 2, 3, 4, 5}
my_set.add(6)  # Adding an element
print(my_set)  # Output: {1, 2, 3, 4, 5, 6}
my_set.add(3)  # Adding a duplicate element (will not be added)
print(my_set)  # Output: {1, 2, 3, 4, 5, 6}
# use in storing unique values and performing  operations like union, intersection, etc.
# used in student age storing unique values and performing  operations like union, intersection, etc.



   

# Function for adding two numbers
