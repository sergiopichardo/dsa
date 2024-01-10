"""
five sort

Write a function, `five_sort`, that takes in an list of numbers as an argument. 
The function should rearrange elements of the list such that all 5s appear at the end. 
Your function should perform this operation in-place by mutating the original array. 
The function should return the array.

Elements that are not 5 can appear in any order in the output, as long as all 5s are at the end of the array.
"""

"""
INPUT: List[int]
OUTPUT: List[int]

RULES 
- it should rearrage elements of the list such that all 5s appear at the end of the list
- it should perform this operation in-place by mutating the original list 
- it should return the mutated list
- elements that are not 5 can appear in any order in the output

DS
- list: the original list

MENTAL MODEL
- we need to move all 5s to the end of the list 
- we can use the "multiple pointers" pattern 
    - set a pointer at each end of the list 
    - increment the left pointer if the number is NOT a 5
    - decrement the right pointer if the number is a 5
- if the pointers are at the same index break out of the loop
- return the mutated list


ALGO

DEFINE five_sort(numbers: List[int])
    SET left to 0 
    SET right to 0 

    WHILE left != right 
        IF the number at `left` is not 5
            increment `left` by 1
        IF the number at `right` is 5
            decrement `right` by 1
        ELSE 
            swap the number at `left` with the number at `right`
    RETURN `numbers`
    

COMPLEXITY
- N: length of the list
- Time: O(N) 
- Space: O(1)

"""

from typing import List

def five_sort(numbers: List[int]):
    left = 0
    right = len(numbers) - 1

    while left != right:
        if numbers[left] == 5 and numbers[right] != 5:
            temp = numbers[left]
            numbers[left] = numbers[right]
            numbers[right] = temp
        elif numbers[left] != 5:
            left = left + 1
        else:
            right = right - 1

    return numbers


print(five_sort([12, 5, 1, 5, 12, 7]))                        # [12, 7, 1, 12, 5, 5] 
print(five_sort([5, 2, 5, 6, 5, 1, 10, 2, 5, 5]))             # [2, 2, 10, 6, 1, 5, 5, 5, 5, 5] 
print(five_sort([5, 5, 5, 1, 1, 1, 4]))                       # [4, 1, 1, 1, 5, 5, 5] 
print(five_sort([5, 5, 6, 5, 5, 5, 5]))                       # [6, 5, 5, 5, 5, 5, 5] 
print(five_sort([5, 1, 2, 5, 5, 3, 2, 5, 1, 5, 5, 5, 4, 5]))  # [4, 1, 2, 1, 2, 3, 5, 5, 5, 5, 5, 5, 5, 5] 

# fives = [4] * 20_000
# fours = [5] * 20_000
# nums = fours + fives
# print(five_sort(nums))
# twenty-thousand 4s followed by twenty-thousand 5s
# [4, 4, 4, 4, ..., 5, 5, 5, 5]//