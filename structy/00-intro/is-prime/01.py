"""
is prime
Write a function, isPrime, that takes in a number as an argument. The function should return a boolean indicating whether or not the given number is prime.

A prime number is a number that is only divisible by two distinct numbers: 1 and itself.

For example, 7 is a prime because it is only divisible by 1 and 7. For example, 6 is not a prime because it is divisible by 1, 2, 3, and 6.

You can assume that the input number is a positive integer.
"""

"""
INPUT: int
OUTPUT: bool

RULES: 
- write a function that takes a number as an argument that 
    returns True if the number is prime and False otherwise
- definition: a number is prime if it's only divisible by itself and 1
- only positive integers will be provided as arguments


TESTS
T1 
input: 7
output: True 
why: b/c 7 is only divisible by itself and 1

T2
input: 6
output: False 
why: b/c 6 is divisible by: 6, 1, 2, and 3


MENTAL MODEL 
We could iterate from 1 to the input (inclusive). For example, if the number is 6
We start iterating through 1, 2, 3, 4, 5, 6. If one of the numbers is divisible 
by anything other than 1 and itself, return false immediately. Otherwise, return true 

DATA STRUCTURES
- boolean

ALGORITHM
- if the number is 1, return false 
- for each `number` starting from 2 up to and not including the argument: 
    - if the argument is divisible by the input
        - return false 
- return true 

COMPLEXITY 
- N: the number of iterations
- Time: O(N)
- Space: O(1)

"""

def is_prime(n):
    if n == 1: 
        return False
    
    for number in range(2, n): 
        if n % number == 0:
            return False
    return True

print(is_prime(2))   # -> True
print(is_prime(3))   # -> True
print(is_prime(4))   # -> False
print(is_prime(5))   # -> True
print(is_prime(6))   # -> False
print(is_prime(7))   # -> True
print(is_prime(8))   # -> False
print(is_prime(25))  # -> False
print(is_prime(31))  # -> True
print(is_prime(2017)) # -> True
print(is_prime(2048)) # -> False
print(is_prime(1))   # -> False
print(is_prime(713)) # -> False