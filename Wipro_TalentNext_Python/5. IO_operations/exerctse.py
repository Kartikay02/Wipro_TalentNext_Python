# ============================================================================
# FILE OPERATIONS PROGRAM
# ============================================================================
# Path to the text file - you can modify this to the path of your .txt file
file_path = 'sample.txt'
# Question 1: Read the entire content from a txt file and display it
print("=" * 60)
print("QUESTION 1: Read entire content of a text file")
print("=" * 60)

try:
    with open(file_path, 'r') as file:
        content = file.read()
        print("File Content:\n")
        print(content)
except FileNotFoundError:
    print(f"Error: File '{file_path}' not found.")

# ----------------------------------------------------------------------------
# Question 2: Read first n lines from a txt file. Get n as user input.
print("\n" + "=" * 60)
print("QUESTION 2: Read first n lines from a text file")
print("=" * 60)

try:
    n = int(input("Enter the number of lines to read: "))
    with open(file_path, 'r') as file:
        for i in range(n):
            line = file.readline()
            if line == '':  # End of file
                break
            print(line.rstrip())
except ValueError:
    print("Please enter a valid integer for number of lines.")
except FileNotFoundError:
    print(f"Error: File '{file_path}' not found.")

# ----------------------------------------------------------------------------
# Question 3: Accept input from user and append it to a txt file
print("\n" + "=" * 60)
print("QUESTION 3: Append user input to a text file")
print("=" * 60)

try:
    user_text = input("Enter the text you want to append to the file:\n")
    with open(file_path, 'a') as file:
        file.write(user_text + '\n')
    print("Text appended successfully.")
except Exception as e:
    print("An error occurred:", e)

# ----------------------------------------------------------------------------
# Question 4: Read contents from a txt file line by line and store each line into a list
print("\n" + "=" * 60)
print("QUESTION 4: Read file lines into a list")
print("=" * 60)

try:
    lines_list = []
    with open(file_path, 'r') as file:
        for line in file:
            lines_list.append(line.rstrip('\n'))
    print("Lines read into list:")
    print(lines_list)
except FileNotFoundError:
    print(f"Error: File '{file_path}' not found.")

# ----------------------------------------------------------------------------
# Question 5: Find the longest word from the txt file contents
# Assuming file has only one longest word (no ties)
print("\n" + "=" * 60)
print("QUESTION 5: Find the longest word in the text file")
print("=" * 60)

import string

try:
    with open(file_path, 'r') as file:
        text = file.read()
        # Remove punctuation for accurate word comparison
        translator = str.maketrans('', '', string.punctuation)
        clean_text = text.translate(translator)
        words = clean_text.split()

        if not words:
            print("The file is empty or contains no words.")
        else:
            longest_word = max(words, key=len)
            print(f"The longest word in the file is: '{longest_word}'")
except FileNotFoundError:
    print(f"Error: File '{file_path}' not found.")

# ----------------------------------------------------------------------------
# Question 6: Count the frequency of a user-entered word in a txt file
print("\n" + "=" * 60)
print("QUESTION 6: Count the frequency of a given word in the file")
print("=" * 60)

try:
    search_word = input("Enter the word to search its frequency: ").strip()

    with open(file_path, 'r') as file:
        file_text = file.read()
        # Normalize text and word for case-insensitive match, remove punctuation
        translator = str.maketrans('', '', string.punctuation)
        clean_text = file_text.translate(translator).lower()
        clean_search_word = search_word.lower()

        # Count occurrences
        words_list = clean_text.split()
        frequency = words_list.count(clean_search_word)

    print(f"The word '{search_word}' appears {frequency} time(s) in the file.")
except FileNotFoundError:
    print(f"Error: File '{file_path}' not found.")
