/*
Two Sum (Easy)

INPUT 1: array of integers 
INPUT 2: integer  
OUTPUT: array of integers
- indices

RULES 
- Given an array of integers and a target integer, 
  return an array of two indices of two numbers that add up to the target
- There will ALWAYS be exactly one solution
- You may not use the same element twice
- You can return the answer in any order

Implicit Rules
- We'll always have an array of at least 2 numbers 
  - No need to check for invalid arrays or array items
- the array numbers and the target will be in the range of -109 and 109

EXAMPLES 
Example 1
Input: [2,7,11,15], 9
Output: [0,1]
- Because nums[0] + nums[1] == 9, we return [0, 1].
- Because 2 + 7 = 9

Example 2
Input: nums = [3,2,4], target = 6
Output: [1,2]

Example 3
Input: nums = [3,3], target = 6
Output: [0,1]

SCRATCH PAD
Input: [2,7,11,15], 9
Output: [0,1]

DATA STRUCTURE 
- array: to return indices 

ALGORITHM 
- for each item at index i 
  - for each item at index i + 1
    - if the items at `nums[i] + nums[j] = target`
      - return an array of the current indices; [i, j]

Complexity 
- Time: O(N^2)
- Space: O(1)
*/


/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number[]}
 */
const twoSum = (nums, target) => {
  for (let i = 0; i < nums.length; i++) {
    for (let j = i + 1; j < nums.length; j++) {
      if (nums[i] + nums[j] === target) {
        return [i, j]; 
      }
    }
  }
}; 
