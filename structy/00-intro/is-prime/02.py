from math import sqrt, floor

"""
Complexity
- N: 
- Time: 
- Space: 

"""

def is_prime(n):
    if n == 1: 
        return False 

    for i in range(2, floor(sqrt(n)) + 1):
        if n % i == 0: 
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

