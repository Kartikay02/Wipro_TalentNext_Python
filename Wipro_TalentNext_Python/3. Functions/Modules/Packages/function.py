#  Write a function to return the sum of all numbers in a list.  
# Sample List : (8, 2, 3, 0, 7)
# Expected Output : 20

def sum_list(numbers):
    return sum(numbers)

print(sum_list([8, 2, 3, 0, 7]))  


# Write a function to return the reverse of a string.  
# Sample String : "1234abcd"
# Expected Output : "dcba4321"

def reverse_string(s):
    return s[::-1]
print(reverse_string("1234abcd"))  


#  Write a function to calculate and return the factorial of a number (a non-negative integer).
def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

print(factorial(5))


#  Write a function that accepts a string and prints the number of upper case letters and lower case letters in it.
def count_case(s):
    upper_count = 0
    lower_count = 0
    for char in s:
        if char.isupper():
            upper_count += 1
        elif char.islower():
            lower_count += 1
    print("Upper case letters:", upper_count)
    print("Lower case letters:", lower_count)

count_case("Hello World!")


#  Write a function to print the even numbers from a given list. List is passed to the function as an argument. 
#  Sample List : [1, 2, 3, 4, 5, 6, 7, 8, 9]
# Expected Result : [2, 4, 6, 8]
def print_even(numbers):
    even_numbers = [num for num in numbers if num % 2 == 0]
    print(even_numbers)

print_even([1, 2, 3, 4, 5, 6, 7, 8, 9])

#  Write a function that takes a number as a parameter and checks whether the number is prime or not.
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

print(is_prime(7))
print(is_prime(10))
