import sys

#  Write a program to accept two numbers as command line arguments and display their sum.

if len(sys.argv) != 3:
    print("Usage: python exercise.py <num1> <num2>")
else:
    try:
        num1 = float(sys.argv[1])
        num2 = float(sys.argv[2])
        print("Sum:", num1 + num2)
    except ValueError:
        print("Please provide valid numbers.")


# Write a program to accept a welcome message through command line arguments and display the file name along with the welcome message.

if len(sys.argv) != 2:
    print(f"Usage: python {sys.argv[0]} <welcome_message>")
else:
    message = sys.argv[1]
    print("File Name:", sys.argv[0])
    print("Welcome Message:", message)


# Write a program to accept 10 numbers through command line arguments and calculate the sum of prime numbers among them.

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True

if len(sys.argv) != 11:
    print(f"Usage: python {sys.argv[0]} <num1> <num2> ... <num10>")
else:
    try:
        numbers = [int(arg) for arg in sys.argv[1:]]
        prime_sum = sum(num for num in numbers if is_prime(num))
        print("Sum of prime numbers:", prime_sum)
    except ValueError:
        print("Please provide 10 valid integers.")
