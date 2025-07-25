# Name: KUMAR KARTIKAY
# Enrollment: 0176AL221074
# College: LNCTE
# Branch: CSE-AIML
# Semester: 7tH

#---------------------------------------------------- EXERCISES---------------------------------------

# Q1. Check if a given number is Positive, Negative, or Zero
num = float(input("Enter a number: "))
if num > 0:
    print("Positive")
elif num < 0:
    print("Negative")
else:
    print("Zero")

# Q2. Check if a given number is odd or even
num = int(input("Enter a number: "))
if num % 2 == 0:
    print("Even")
else:
    print("Odd")

# Q3. Check if two numbers have the same last digit
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
if num1 % 10 == num2 % 10:
    print("True")
else:
    print("False")

# Q4. Print numbers from 1 to 10 in a single row with one tab space
for i in range(1, 11):
    print(i, end='\t')
print()  # move to next line

# Q5. Print even numbers between 23 and 57 (each in separate row)
for num in range(24, 58, 2):
    print(num)

# Q6. Check if a given number is prime or not
num = int(input("Enter a number: "))
if num > 1:
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            print("Not prime")
            break
    else:
        print("Prime")
else:
    print("Not prime")

# Q7. Print prime numbers between 10 and 99
for num in range(10, 100):
    if num > 1:
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                break
        else:
            print(num)

# Q8. Print the sum of all digits of a given number
num = input("Enter a number: ")
digit_sum = sum(int(digit) for digit in num)
print("Sum of digits:", digit_sum)

# Q9. Reverse a given number and print
num = input("Enter a number: ")
reversed_num = num[::-1]
print("Reversed number:", reversed_num)

# Q10. Check if the given number is a palindrome
num = input("Enter a number: ")
if num == num[::-1]:
    print("Palindrome")
else:
    print("Not a palindrome")


