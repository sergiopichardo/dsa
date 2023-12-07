"""
max value
Write a function, maxValue, that takes in array of numbers as an argument. 
The function should return the largest number in the array.

Solve this without using any built-in array methods.

You can assume that the array is non-empty.
"""

"""
INPUT: integers list 
OUTPUT: largest integer

RULES
- it should return the largest numbe rin the array 
- solve this without any built-in array method 
- assume that the array is non-empty 

Algorithm 
- set `current_max_value` to negative infinity
- for each `current_number` in `numbers_list`
    - if `current_number` is greater than `current_max_value`
        - set `current_max_value` to `current_number`
- return `current_max_value`

Complexity
n = length of list
Time: O(n)
Space: O(1)
"""

def max_value(numbers_list):
    current_max_value = float("-inf")
    for current_number in numbers_list:
        if current_number > current_max_value: 
            current_max_value = current_number
    return current_max_value


print(max_value([4, 7, 2, 8, 10, 9])) # 10
print(max_value([10, 5, 40, 40.3])); # 40.3
print(max_value([-5, -2, -1, -11])); # -1
print(max_value([42])) # 42
print(max_value([1000, 8])) # 1000
print(max_value([1000, 8, 9000])) # 9000
print(max_value([2, 5, 1, 1, 4])) # 5
