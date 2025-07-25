# Write a program to accept two numbers from the user and perform division. If any exception occurs, print an error message or else print the result.

try:
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    result = num1 / num2
except ZeroDivisionError:
    print("Error: Division by zero is not allowed.")
except ValueError:
    print("Error: Invalid input. Please enter numeric values.")
else:
    print("Result:", result)


#  Write a program to accept a number from the user and check whether it’s prime or not. If user enters anything other than number, handle the exception and print an error message.
try:
    num = int(input("Enter a number to check if it's prime: "))
    if num < 2:
        print("The number is not prime.")
    else:
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                print("The number is not prime.")
                break
        else:
            print("The number is prime.")
except ValueError:
    print("Error: Please enter a valid integer.")

    	
#  Write a program to accept the file name to be opened from the user, if file exist print the contents of the file in title case or else handle the exception and print an error message.

filename = input("Enter the file name to open: ")
try:
    with open(filename, 'r') as file:
        contents = file.read()
        print(contents.title())
except FileNotFoundError:
    print("Error: File not found.")

#   Declare a list with 10 integers and ask the user to enter an index. Check whether the number in that index is positive or negative number. If any invalid index is entered, handle the exception and print an error message.

numbers = [10, -5, 3, 8, -2, 0, 7, -1, 4, 6]
try:
    index = int(input("Enter an index (0-9): "))
    if numbers[index] > 0:
        print("The number is positive.")
    else:
        print("The number is negative.")
except IndexError:
    print("Error: Invalid index.")
except ValueError:
    print("Error: Please enter a valid integer.")