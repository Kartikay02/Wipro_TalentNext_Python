# ============================================================================
# SET OPERATIONS PROGRAM
# ============================================================================

# Question 1: Write a program to remove a given item from the set.
print("=" * 60)
print("QUESTION 1: Remove a given item from the set")
print("=" * 60)

# Original set
sample_set = {10, 20, 30, 40, 50}
print(f"Original set: {sample_set}")

item_to_remove = 30

# Method 1: Using discard() - doesn't raise error if item not found
sample_set_copy1 = sample_set.copy()
sample_set_copy1.discard(item_to_remove)
print(f"After removing {item_to_remove} using discard(): {sample_set_copy1}")

# Method 2: Using remove() - raises error if item not found
sample_set_copy2 = sample_set.copy()
try:
    sample_set_copy2.remove(item_to_remove)
    print(f"After removing {item_to_remove} using remove(): {sample_set_copy2}")
except KeyError:
    print(f"Item {item_to_remove} not found in the set")

# Demonstrating difference when item doesn't exist
item_not_exist = 99
print(f"\nTrying to remove non-existent item {item_not_exist}:")

# discard() won't raise error
sample_set_copy3 = sample_set.copy()
sample_set_copy3.discard(item_not_exist)
print(f"Using discard() on non-existent item: {sample_set_copy3}")

# remove() will raise error
sample_set_copy4 = sample_set.copy()
try:
    sample_set_copy4.remove(item_not_exist)
    print(f"Using remove() on non-existent item: {sample_set_copy4}")
except KeyError:
    print(f"KeyError: Item {item_not_exist} not found in the set")

# ============================================================================
# Question 2: Write a program to create an intersection of sets.
print("\n" + "=" * 60)
print("QUESTION 2: Create an intersection of sets")
print("=" * 60)

set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}
set3 = {5, 6, 9, 10}

print(f"Set 1: {set1}")
print(f"Set 2: {set2}")
print(f"Set 3: {set3}")

# Method 1: Using intersection() method
intersection_12 = set1.intersection(set2)
print(f"Intersection of set1 and set2: {intersection_12}")

# Method 2: Using & operator
intersection_12_alt = set1 & set2
print(f"Intersection using & operator: {intersection_12_alt}")

# Intersection of multiple sets
intersection_all = set1.intersection(set2, set3)
print(f"Intersection of all three sets: {intersection_all}")

# ============================================================================
# Question 3: Write a program to create a union of sets.
print("\n" + "=" * 60)
print("QUESTION 3: Create a union of sets")
print("=" * 60)

setA = {1, 2, 3}
setB = {3, 4, 5}
setC = {5, 6, 7}

print(f"Set A: {setA}")
print(f"Set B: {setB}")
print(f"Set C: {setC}")

# Method 1: Using union() method
union_AB = setA.union(setB)
print(f"Union of setA and setB: {union_AB}")

# Method 2: Using | operator
union_AB_alt = setA | setB
print(f"Union using | operator: {union_AB_alt}")

# Union of multiple sets
union_all = setA.union(setB, setC)
print(f"Union of all three sets: {union_all}")

# Method 3: Using update() to modify original set
setA_copy = setA.copy()
setA_copy.update(setB)
print(f"Using update() method: {setA_copy}")

# ============================================================================
# Question 4: Write a program to find the maximum and minimum value in a set.
print("\n" + "=" * 60)
print("QUESTION 4: Find maximum and minimum value in a set")
print("=" * 60)

# Numeric set
num_set = {45, 12, 78, 23, 56, 89, 34, 67}
print(f"Numeric set: {num_set}")

max_value = max(num_set)
min_value = min(num_set)

print(f"Maximum value in the set: {max_value}")
print(f"Minimum value in the set: {min_value}")

# String set (lexicographic comparison)
string_set = {'apple', 'banana', 'cherry', 'date'}
print(f"\nString set: {string_set}")

max_string = max(string_set)
min_string = min(string_set)

print(f"Maximum string (lexicographically): {max_string}")
print(f"Minimum string (lexicographically): {min_string}")

# Mixed numeric set with negative numbers
mixed_set = {-10, 0, 15, -5, 20, -25}
print(f"\nMixed numeric set: {mixed_set}")

max_mixed = max(mixed_set)
min_mixed = min(mixed_set)

print(f"Maximum value: {max_mixed}")
print(f"Minimum value: {min_mixed}")

# Handling empty set
empty_set = set()
print(f"\nEmpty set: {empty_set}")

try:
    max_empty = max(empty_set)
    min_empty = min(empty_set)
    print(f"Max: {max_empty}, Min: {min_empty}")
except ValueError as e:
    print(f"Error with empty set: {e}")

# ============================================================================
print("\n" + "=" * 60)
print("PROGRAM COMPLETED SUCCESSFULLY!")
print("=" * 60)
