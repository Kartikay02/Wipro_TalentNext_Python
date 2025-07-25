# ============================================================================
# TUPLE OPERATIONS PROGRAM
# ============================================================================

# Question 1: Write a program to print the 4th element from first and 4th element from last in a tuple.
print("=" * 60)
print("QUESTION 1: Print 4th element from first and 4th from last in a tuple")
print("=" * 60)

sample_tuple = (10, 20, 30, 40, 50, 60, 70, 80, 90, 100)
print(f"Sample tuple: {sample_tuple}")

try:
    fourth_from_first = sample_tuple[3]  # index 3 = 4th element
    fourth_from_last = sample_tuple[-4]  # -4 index = 4th from last
    print(f"4th element from first: {fourth_from_first}")
    print(f"4th element from last: {fourth_from_last}")
except IndexError:
    print("Tuple doesn't have enough elements.")

# ============================================================================
# Question 2: Write a program to check whether an element exists in a tuple or not.
print("\n" + "=" * 60)
print("QUESTION 2: Check whether an element exists in a tuple")
print("=" * 60)

elements_tuple = ('apple', 'banana', 'cherry', 'date')
print(f"Tuple: {elements_tuple}")

element_to_check = 'banana'
if element_to_check in elements_tuple:
    print(f"Element '{element_to_check}' exists in the tuple.")
else:
    print(f"Element '{element_to_check}' does NOT exist in the tuple.")

element_to_check2 = 'mango'
if element_to_check2 in elements_tuple:
    print(f"Element '{element_to_check2}' exists in the tuple.")
else:
    print(f"Element '{element_to_check2}' does NOT exist in the tuple.")

# ============================================================================
# Question 3: Write a program to convert a list into a tuple.
print("\n" + "=" * 60)
print("QUESTION 3: Convert a list into a tuple")
print("=" * 60)

sample_list = [1, 2, 3, 4, 5]
print(f"Original list: {sample_list}")

converted_tuple = tuple(sample_list)
print(f"Converted tuple: {converted_tuple}")

# ============================================================================
# Question 4: Write a program to find the index of an item in a tuple.
print("\n" + "=" * 60)
print("QUESTION 4: Find the index of an item in a tuple")
print("=" * 60)

search_tuple = ('a', 'b', 'c', 'd', 'e', 'b')
print(f"Tuple: {search_tuple}")

item_to_find = 'b'
try:
    index_first = search_tuple.index(item_to_find)  # finds first occurrence
    print(f"Index of first occurrence of '{item_to_find}': {index_first}")
except ValueError:
    print(f"Item '{item_to_find}' not found in the tuple.")

item_to_find2 = 'z'
try:
    index_not_found = search_tuple.index(item_to_find2)
    print(f"Index of '{item_to_find2}': {index_not_found}")
except ValueError:
    print(f"Item '{item_to_find2}' not found in the tuple.")

# ============================================================================
# Question 5: Write a program to replace last value of tuples in a list to 100.
# Sample list:
# [(10, 20, 40), (40, 50, 60), (70, 80, 90)]
# Expected Output:
# [(10, 20, 100), (40, 50, 100), (70, 80, 100)]
print("\n" + "=" * 60)
print("QUESTION 5: Replace last value of tuples in a list to 100")
print("=" * 60)

tuple_list = [(10, 20, 40), (40, 50, 60), (70, 80, 90)]
print(f"Original list of tuples: {tuple_list}")

# Since tuples are immutable, create new tuples with last element replaced
modified_list = [t[:-1] + (100,) for t in tuple_list]

print(f"Modified list of tuples: {modified_list}")

# ============================================================================
print("\n" + "=" * 60)
print("PROGRAM COMPLETED SUCCESSFULLY!")
print("=" * 60)
