# ============================================================================
# Project: Python IO Operations - Secret Message Finder
# ============================================================================

# The program finds (1) meeting time from number of lines in a given text file,
# and (2) meeting place from the most frequently occurring word.

import string

file_path = 'secret_message.txt'  # Replace with your text file path

# -------------------------
# Step 1: Read all the lines from the file
with open(file_path, 'r') as f:
    lines = f.readlines()

# Step 2: Meeting time (from number of lines)
n_lines = len(lines)
if n_lines == 0:
    print("File is empty.")
    exit()

# 12-hour format conversion (n_lines may be 1-24)
meeting_time_hour = n_lines
ampm = "AM"
if meeting_time_hour > 12:
    meeting_time_hour -= 12
    ampm = "PM"
elif meeting_time_hour == 12:
    ampm = "PM"
else:
    ampm = "AM"

print(f"Meeting time: {meeting_time_hour} {ampm}")

# Step 3: Find the word with the maximum frequency (meeting place)
# Clean and collect all words from all lines
all_words = []
for line in lines:
    words = line.split()
    for word in words:
        # Remove punctuation from both ends
        word_clean = word.strip(string.punctuation)
        if word_clean:
            all_words.append(word_clean)

# Count frequencies (case-sensitive as per sample)
word_freq = {}
for word in all_words:
    word_freq[word] = word_freq.get(word, 0) + 1

# Find word with maximum frequency
max_count = 0
meeting_place_word = ""
for word, count in word_freq.items():
    if count > max_count:
        max_count = count
        meeting_place_word = word

meeting_place = f"{meeting_place_word} Street"
print(f"Meeting place: {meeting_place}")

# ============================================================================
# End of project
# ============================================================================

