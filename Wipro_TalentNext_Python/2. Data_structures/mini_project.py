# 1. People and facts-- Dictionary
# =================================================================================
# Project: People Facts Dictionary (Python Data Structure Module)
# =================================================================================

# 1. Create a dictionary with people and an interesting fact about each.
people_facts = {
    "Jeff": "Is afraid of Dogs.",
    "David": "Plays the piano.",
    "Jason": "Can fly an airplane."
}

def display_people_facts(title, facts_dict):
    print("\n" + title)
    for person, fact in facts_dict.items():
        print(f"{person}: {fact}")

# Display the initial list
display_people_facts("Initial people and interesting facts:", people_facts)

# 2. Change a fact about one person (e.g. Jeff)
people_facts["Jeff"] = "Is afraid of heights."

# 3. Add an additional person and corresponding fact
people_facts["Jill"] = "Can hula dance."

# Display the updated list
display_people_facts("Updated people and interesting facts:", people_facts)

# 4. Run multiple times to observe order (for demonstration, run 3 times)
import random

print("\nRepeated random order display demonstration:")

for i in range(3):
    print(f"\nRun #{i+1}:")
    # For true random order in display, shuffle items
    items = list(people_facts.items())
    random.shuffle(items)
    for person, fact in items:
        print(f"{person}: {fact}")

# =================================================================================
# End of project
# =================================================================================


# 2.Find the Runner-Up Score -- List
# ============================================================================
# Project: Find the Runner-Up Score (Python Data Structure)
# ============================================================================

# Step 1: Store scores in a list (you can modify this list for different test cases)
scores = [2, 3, 6, 6, 5]

# Step 2: Remove duplicates to ensure only unique scores are considered
unique_scores = list(set(scores))

# Step 3: Sort the unique scores in descending order
unique_scores.sort(reverse=True)

# Step 4: Check there are at least two unique scores
if len(unique_scores) < 2:
    print("No runner-up score exists (not enough unique values).")
else:
    # Step 5: The runner-up score is the second element in the sorted list
    runner_up = unique_scores[1]
    print(f"The runner-up score is: {runner_up}")

# ============================================================================
# End of Project
# ============================================================================




# 3 Find the Percentage --Dictionary and List
# ============================================================================
# Project: Student Average Percentage Marks (Python Dictionary)
# ============================================================================

# Step 1: Create the student records dictionary
students = {
    "Krishna": [67, 68, 69],
    "Arjun": [70, 98, 63],
    "Malika": [52, 56, 60]
}

# Step 2: Prompt user to enter a student's name
student_name = input("Enter a name: ")

# Step 3: Check if the student exists and calculate average
if student_name in students:
    marks = students[student_name]
    average = sum(marks) / len(marks)
    # Optional: output as integer if you want, otherwise keep floating point
    print(f"Average percentage mark: {int(average) if average == int(average) else average}")
else:
    print("Student not found in the record.")

# ============================================================================

# 4 Find the name-- String

# Project: Count occurrences of "Alex" in a string

# Accept input from user
input_str = input()

# Use the count() method to find occurrences of 'Alex'
count = input_str.count("Alex")

print(count)


