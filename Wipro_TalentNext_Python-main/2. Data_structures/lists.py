# ============================================================================
# LIST OPERATIONS PROGRAM
# ============================================================================

# Question 1: Write a program to create a list of 5 integers and display the list items.
# Access individual elements through index.
print("=" * 50)
print("QUESTION 1: Create list and access elements")
print("=" * 50)

# Creating a list of 5 integers
numbers = [10, 25, 30, 45, 50]
print(f"Original list: {numbers}")

# Displaying list items
print("List items:")
for i, item in enumerate(numbers):
    print(f"Index {i}: {item}")

# Accessing individual elements through index
print(f"\nAccessing individual elements:")
print(f"Element at index 0: {numbers[0]}")
print(f"Element at index 2: {numbers[2]}")
print(f"Element at index 4: {numbers[4]}")

# ============================================================================
# Question 2: Write a program to append a new item to the end of the list.
print("\n" + "=" * 50)
print("QUESTION 2: Append new item to end of list")
print("=" * 50)

# Using the same list from question 1
print(f"Original list: {numbers}")
new_item = 60
numbers.append(new_item)
print(f"After appending {new_item}: {numbers}")

# ============================================================================
# Question 3: Write a program to reverse the order of the items in the list.
print("\n" + "=" * 50)
print("QUESTION 3: Reverse the order of items")
print("=" * 50)

print(f"Original list: {numbers}")
numbers.reverse()
print(f"After reversing: {numbers}")

# ============================================================================
# Question 4: Write a program to print the number of occurrences of a specified element in a list.
print("\n" + "=" * 50)
print("QUESTION 4: Count occurrences of specified element")
print("=" * 50)

# Creating a list with duplicate elements for demonstration
sample_list = [1, 2, 3, 2, 4, 2, 5, 2, 6]
print(f"Sample list: {sample_list}")
element_to_count = 2
count = sample_list.count(element_to_count)
print(f"Number of occurrences of {element_to_count}: {count}")

# ============================================================================
# Question 5: Write a program to append the items of list1 to list2 in the front.
print("\n" + "=" * 50)
print("QUESTION 5: Append items of list1 to front of list2")
print("=" * 50)

list1 = [1, 2, 3]
list2 = [4, 5, 6]
print(f"List1: {list1}")
print(f"List2 (before): {list2}")

# Method 1: Using list concatenation
list2 = list1 + list2
print(f"List2 (after appending list1 to front): {list2}")

# Alternative method using extend and reverse
# list2_copy = [4, 5, 6]  # Reset for demonstration
# list2_copy[:0] = list1  # Insert at beginning
# print(f"Alternative method result: {list2_copy}")

# ============================================================================
# Question 6: Write a program to insert a new item before the second element in an existing list.
print("\n" + "=" * 50)
print("QUESTION 6: Insert new item before second element")
print("=" * 50)

demo_list = [10, 20, 30, 40, 50]
print(f"Original list: {demo_list}")
new_element = 15
demo_list.insert(1, new_element)  # Insert at index 1 (before second element)
print(f"After inserting {new_element} before second element: {demo_list}")

# ============================================================================
# Question 7: Write a program to remove the item from a specified index in a list.
print("\n" + "=" * 50)
print("QUESTION 7: Remove item from specified index")
print("=" * 50)

removal_list = [100, 200, 300, 400, 500]
print(f"Original list: {removal_list}")
index_to_remove = 2
removed_item = removal_list.pop(index_to_remove)
print(f"Removed item at index {index_to_remove}: {removed_item}")
print(f"List after removal: {removal_list}")

# ============================================================================
# Question 8: Write a program to remove the first occurrence of a specified element from a list.
print("\n" + "=" * 50)
print("QUESTION 8: Remove first occurrence of specified element")
print("=" * 50)

elements_list = [5, 10, 15, 10, 20, 10, 25]
print(f"Original list: {elements_list}")
element_to_remove = 10
if element_to_remove in elements_list:
    elements_list.remove(element_to_remove)
    print(f"After removing first occurrence of {element_to_remove}: {elements_list}")
else:
    print(f"Element {element_to_remove} not found in the list")

# ============================================================================
print("\n" + "=" * 50)
print("PROGRAM COMPLETED SUCCESSFULLY!")
print("=" * 50)
