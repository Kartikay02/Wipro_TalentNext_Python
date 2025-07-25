# ============================================================================
# DICTIONARY OPERATIONS PROGRAM
# ============================================================================

# Question 1: Write a program to add a key and value to a dictionary.
# Sample Dictionary: {0: 10, 1: 20}
# Expected Result: {0: 10, 1: 20, 2: 30}
print("=" * 60)
print("QUESTION 1: Add a key and value to a dictionary")
print("=" * 60)

# Original dictionary
sample_dict = {0: 10, 1: 20}
print(f"Original dictionary: {sample_dict}")

# Method 1: Using square bracket notation
sample_dict[2] = 30
print(f"After adding key 2 with value 30: {sample_dict}")

# Method 2: Using update() method (alternative approach)
sample_dict_alt = {0: 10, 1: 20}
sample_dict_alt.update({2: 30})
print(f"Using update() method: {sample_dict_alt}")

# ============================================================================
# Question 2: Write a program to concatenate dictionaries to create a new one.
# Sample Dictionary: {1: 10, 2: 20} and {3: 30, 4: 40} and {5: 50, 6: 60}
# Expected Result: {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}
print("\n" + "=" * 60)
print("QUESTION 2: Concatenate dictionaries to create a new one")
print("=" * 60)

dict1 = {1: 10, 2: 20}
dict2 = {3: 30, 4: 40}
dict3 = {5: 50, 6: 60}

print(f"Dictionary 1: {dict1}")
print(f"Dictionary 2: {dict2}")
print(f"Dictionary 3: {dict3}")

# Method 1: Using unpacking operator (**)
concatenated_dict = {**dict1, **dict2, **dict3}
print(f"Concatenated dictionary (using **): {concatenated_dict}")

# Method 2: Using update() method
result_dict = {}
result_dict.update(dict1)
result_dict.update(dict2)
result_dict.update(dict3)
print(f"Concatenated dictionary (using update): {result_dict}")

# ============================================================================
# Question 3: Write a program to check if a given key already exists in a dictionary.
print("\n" + "=" * 60)
print("QUESTION 3: Check if a given key exists in a dictionary")
print("=" * 60)

test_dict = {'a': 100, 'b': 200, 'c': 300}
print(f"Test dictionary: {test_dict}")

# Method 1: Using 'in' operator
key_to_check = 'b'
if key_to_check in test_dict:
    print(f"Key '{key_to_check}' exists with value: {test_dict[key_to_check]}")
else:
    print(f"Key '{key_to_check}' does not exist")

# Method 2: Using get() method
key_to_check2 = 'z'
if test_dict.get(key_to_check2) is not None:
    print(f"Key '{key_to_check2}' exists with value: {test_dict[key_to_check2]}")
else:
    print(f"Key '{key_to_check2}' does not exist")

# Method 3: Using keys() method
key_to_check3 = 'c'
if key_to_check3 in test_dict.keys():
    print(f"Key '{key_to_check3}' exists with value: {test_dict[key_to_check3]}")
else:
    print(f"Key '{key_to_check3}' does not exist")

# ============================================================================
# Question 4: Write a program to iterate over a dictionary using for loop and print:
# - keys alone
# - values alone  
# - both keys and values
print("\n" + "=" * 60)
print("QUESTION 4: Iterate over dictionary - keys, values, and both")
print("=" * 60)

iteration_dict = {'name': 'Python', 'version': 3.9, 'type': 'language', 'year': 1991}
print(f"Dictionary for iteration: {iteration_dict}")

# Print keys alone
print("\nKeys alone:")
for key in iteration_dict.keys():
    print(f"Key: {key}")

# Alternative way to print keys
print("\nKeys alone (alternative method):")
for key in iteration_dict:
    print(f"Key: {key}")

# Print values alone
print("\nValues alone:")
for value in iteration_dict.values():
    print(f"Value: {value}")

# Print both keys and values
print("\nBoth keys and values:")
for key, value in iteration_dict.items():
    print(f"Key: {key}, Value: {value}")

# ============================================================================
# Question 5: Write a program to prepare a dictionary where the keys are numbers 
# between 1 and 15 (both included) and the values are square of the keys.
print("\n" + "=" * 60)
print("QUESTION 5: Dictionary with keys 1-15 and values as squares")
print("=" * 60)

# Method 1: Using for loop
squares_dict = {}
for num in range(1, 16):
    squares_dict[num] = num ** 2

print(f"Dictionary with squares (using loop): {squares_dict}")

# Method 2: Using dictionary comprehension
squares_dict_comp = {x: x**2 for x in range(1, 16)}
print(f"Dictionary with squares (using comprehension): {squares_dict_comp}")

# ============================================================================
# Question 6: Write a program to sum all the values in a dictionary, 
# considering the values will be of int type.
print("\n" + "=" * 60)
print("QUESTION 6: Sum all values in a dictionary")
print("=" * 60)

# Sample dictionary with integer values
sum_dict = {'a': 10, 'b': 20, 'c': 30, 'd': 40, 'e': 50}
print(f"Dictionary for sum calculation: {sum_dict}")

# Method 1: Using sum() and values()
total_sum = sum(sum_dict.values())
print(f"Sum of all values (using sum()): {total_sum}")

# Method 2: Using for loop
total_sum_loop = 0
for value in sum_dict.values():
    total_sum_loop += value
print(f"Sum of all values (using loop): {total_sum_loop}")

# Method 3: Using items() to show key-value pairs while summing
total_sum_items = 0
print("Adding values step by step:")
for key, value in sum_dict.items():
    total_sum_items += value
    print(f"Adding {key}: {value}, Running total: {total_sum_items}")

print(f"Final sum: {total_sum_items}")

# ============================================================================
print("\n" + "=" * 60)
print("PROGRAM COMPLETED SUCCESSFULLY!")
print("=" * 60)
