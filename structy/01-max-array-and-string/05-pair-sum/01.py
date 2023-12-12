from typing import List


"""
pair sum
Write a function, pair_sum, that takes in an array and a target sum as arguments. The function should return a tuple containing a pair of indices whose elements sum to the given target. The indices returned must be unique.

Be sure to return the indices, not the elements themselves.

There is guaranteed to be one such pair that sums to the target.
"""


"""
INPUT: 
    numbers: List of integers
    target: integer
OUTPUT: 
    pair: List of 2 integers that add up to the target


RULES
- It should return an array containing indices whose elements sum to the given target 
- The indices returned must be unique 
- The input list is guaranteed to have a pair of two indices whose items add up to the target input

EXAMPLES
T1
input: [3, 2, 5, 4, 1], 8
output: [0, 2]
why: b/c 3 + 5 = 8

T1
input: [4, 7, 9, 2, 5, 1], 5
output: [0, 5]
why: b/c 4 + 1 = 5 

T1
input: [4, 7, 9, 2, 5, 1], 3
output: [3, 5]
why: because list[3] + list[5] = 2 + 1 = 5

DATA STRUCTURE 
- list: return the indices 


ALGORITHM
Technique: Nested loops


Function pair_sum(numbers, target):
    For each outer_index from 0 to length of numbers - 1:
        For each inner_index from outer_index + 1 to length of numbers - 1:
            If numbers[outer_index] + numbers[inner_index] equals target:
                Return [outer_index, inner_index]
    Return None
End Function

COMPLEXITY: 
- N: length of the list 
- Time: O(N^2) 
- Space: O(1)

Technique: Complements

Function pair_sum(numbers, target):    
    seen_numbers = {}
    For each index from 0 to length of numbers - 1:
        complement = target - numbers[index]
        If complement is in seen_numbers:
            Return [seen_numbers[complement], index]
        seen_numbers[numbers[index]] = index
    Return None
End Function

COMPLEXITY
- N: length of the array 
- Time: O(N)
- Space: O(1)

"""

# Solution 1 
# def pair_sum(numbers: List[int], target_sum: int) -> (int, int): 
#     for i in range (0, len(numbers)):
#         for j in range (i + 1, len(numbers)):
#             if numbers[i] + numbers[j] == target_sum:
#                 return (i, j)

# Solution 2 
def pair_sum(numbers: List[int], target_sum: int) -> (int, int): 
    seen_nums = {}

    for index, num in enumerate(numbers): 
        complement = target_sum - num

        if complement in seen_nums:
            return (seen_nums[complement], index)
        else: 
            seen_nums[num] = index




print(pair_sum([3, 2, 5, 4, 1], 8))    #  (0, 2)
print(pair_sum([4, 7, 9, 2, 5, 1], 5)) #  (0, 5)
print(pair_sum([4, 7, 9, 2, 5, 1], 3)) #  (3, 5)
print(pair_sum([1, 6, 7, 2], 13))      #  (1, 2)
print(pair_sum([9, 9], 18))            #  (0, 1)
print(pair_sum([6, 4, 2, 8 ], 12))     #  (1, 3)