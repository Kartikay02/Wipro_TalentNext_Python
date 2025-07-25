
# Project 1 (Functions/Modules/Packages):
# Write a function that accepts a hyphen-separated sequence of colors, sorts them alphabetically, and returns them in a hyphen-separated sequence.

def sort_colors(color_sequence):
    colors = color_sequence.split('-')
    colors.sort()
    return '-'.join(colors)

# Sample usage:
input1 = "green-red-yellow-black-white"
print(sort_colors(input1))

input2 = "PINK-BLUE-TAN-PURPLE"
print(sort_colors(input2))



# Functions/Modules/Packages Project 2:

def ispalindrome(name):
    if name == name[::-1]:
        print("Yes, it is a palindrome.")
    else:
        print("No, it is not a palindrome.")

def count_vowels(name):
    vowels = 'aeiouAEIOU'
    count = sum(1 for c in name if c in vowels)
    print("No of vowels:", count)

def frequency_of_letters(name):
    freq = {}
    for c in name:
        freq[c] = freq.get(c, 0) + 1
    freq_list = [f"{char}-{count}" for char, count in freq.items()]
    print("Frequency of letters:", ', '.join(freq_list))


name = input("Enter the name: ")
ispalindrome(name)
count_vowels(name)
frequency_of_letters(name)
