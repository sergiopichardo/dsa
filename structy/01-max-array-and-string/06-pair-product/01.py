"""
pair product
Write a function, pair_product, that takes in a list of integers and a target product as arguments. The function should return a tuple containing a pair of indices whose elements multiply to the given target. The indices returned must be unique.

Be sure to return the indices, not the elements themselves.

There is guaranteed to be one such pair whose product is the target.
"""

"""
INPUT: list of integers 
OUTPUT: target product

RULES 
- it should return a "tuple" containing a pair of "indices" whose elements multiply to the given target product 
- the indices returned should be unique 
- the inputs are guaranteed to contain a pair whose product equal the target

EXPLORATION 
input: [3, 2, 5, 4, 1], 8

{ number: index }

{
    3: 0,
    4: 1,
    1.6: 2,
    2: 3,
    8: 4
}

complement = target sum / number
8 - 3 = 5

DATA STRUCTURE 
- dictionary: to store seen numbers


ALGORITHM 
DEFINE pair_product(numbers: List[int], target_product: integer): 
    SET seen_numbers = {}
    FOR each index starting at 0 to len(numbers) - 1
        complement = target_product / numbers[index]
        IF complement is in seen_numbers 
            return (seen_numbers[complement], index)    
        ELSE 
            SET seen_numbers[number] = index

COMPLEXITY
N = length of the array
TIME: O(N)
SPACE: O(N)
"""

def pair_product(numbers, target_product):
    seen_numbers = {}
    for index, number in enumerate(numbers):
        complement = target_product / number
        if complement in seen_numbers:
            return (seen_numbers[complement], index)
        else:
            seen_numbers[number] = index

print(pair_product([3, 2, 5, 4, 1], 8))     # (1, 3)
print(pair_product([3, 2, 5, 4, 1], 10))    # (1, 2)
print(pair_product([4, 7, 9, 2, 5, 1], 5))  # (4, 5)
print(pair_product([4, 7, 9, 2, 5, 1], 35)) # (1, 4)
print(pair_product([3, 2, 5, 4, 1], 10))    # (1, 2)
print(pair_product([4, 6, 8, 2], 16))       # (2, 3)