# ============================================================================
# STRING OPERATIONS PROGRAM
# ============================================================================

# Question 1: Write a program to count the number of upper and lower case letters in a String.
print("=" * 60)
print("QUESTION 1: Count uppercase and lowercase letters in a string")
print("=" * 60)

def count_upper_lower(s):
    upper_count = 0
    lower_count = 0
    for ch in s:
        if ch.isupper():
            upper_count += 1
        elif ch.islower():
            lower_count += 1
    return upper_count, lower_count

input_str1 = "Wipro Technologies"
upper, lower = count_upper_lower(input_str1)
print(f"Input string: \"{input_str1}\"")
print(f"Uppercase letters: {upper}")
print(f"Lowercase letters: {lower}")

# ============================================================================
# Question 2: Write a program that will check whether a given String is Palindrome or not.
print("\n" + "=" * 60)
print("QUESTION 2: Check whether a string is palindrome")
print("=" * 60)

def is_palindrome(s):
    # Normalize string for palindrome checking (ignore case and spaces)
    s_normalized = ''.join(ch.lower() for ch in s if ch.isalnum())
    return s_normalized == s_normalized[::-1]

input_str2 = "Madam"
result = is_palindrome(input_str2)
print(f"Input string: \"{input_str2}\"")
print(f"Is palindrome? {result}")

input_str2b = "Hello"
result2b = is_palindrome(input_str2b)
print(f"Input string: \"{input_str2b}\"")
print(f"Is palindrome? {result2b}")

# ============================================================================
# Question 3: Given a string, return a new string made of n copies of the first 2 chars of the original string,
# where n is the length of the string. The string length will be >= 2.
# Example: "Wipro" -> "WiWiWiWiWi"
print("\n" + "=" * 60)
print("QUESTION 3: Return n copies of first 2 chars of string, where n=length of string")
print("=" * 60)

def n_copies_first_two_chars(s):
    n = len(s)
    first_two = s[:2]
    return first_two * n

input_str3 = "Wipro"
output3 = n_copies_first_two_chars(input_str3)
print(f"Input string: \"{input_str3}\"")
print(f"Output: \"{output3}\"")

# ============================================================================
# Question 4: Given a string, if the first or last character is 'x' return the string without those characters,
# else return the string unchanged.
# Example: "xHix" -> "Hi"
print("\n" + "=" * 60)
print("QUESTION 4: Remove 'x' from start and end of string if present")
print("=" * 60)

def remove_x_edges(s):
    if s.startswith('x'):
        s = s[1:]
    if s.endswith('x'):
        s = s[:-1]
    return s

input_str4a = "xHix"
input_str4b = "Hello"
output4a = remove_x_edges(input_str4a)
output4b = remove_x_edges(input_str4b)

print(f"Input: \"{input_str4a}\" -> Output: \"{output4a}\"")
print(f"Input: \"{input_str4b}\" -> Output: \"{output4b}\"")

# ============================================================================
# Question 5: Given a string and an integer n, return a string made of n repetitions of the last n characters of the string.
# You may assume that n is between 1 and the length of the string inclusive.
# Example: "Wipro", 3 -> "propropro"
print("\n" + "=" * 60)
print("QUESTION 5: Return n repetitions of last n chars of the string")
print("=" * 60)

def n_repetitions_last_n_chars(s, n):
    last_n = s[-n:]
    return last_n * n

input_str5 = "Wipro"
n_val = 3
output5 = n_repetitions_last_n_chars(input_str5, n_val)
print(f"Input string: \"{input_str5}\", n = {n_val}")
print(f"Output: \"{output5}\"")

# ============================================================================
print("\n" + "=" * 60)
print("PROGRAM COMPLETED SUCCESSFULLY!")
print("=" * 60)
