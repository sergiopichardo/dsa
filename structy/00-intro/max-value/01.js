/*
max value
Write a function, maxValue, that takes in array of numbers as an argument. 
The function should return the largest number in the array.

Solve this without using any built-in array methods.

You can assume that the array is non-empty.
*/

/*
INPUT: array of numbers
OUTPUT: largest number in the array

RULES 
- solve without built-in methods
- assume the array is non-empty 
- assume an array with the right data type will be provided

DATA STRUCTURE 
- number 

ALGORITHM 
- define `max` and set to -Infinity 
- iterate over the array of numbers 
    - if the current number is greater than the max number 
        - set `max` equal to `current`
- return `max`

COMPLEXITY 
- time: O(N)
- space: O(1)
*/


const maxValue = (nums) => {
    let max = -Infinity;
    
    for (let index = 0; index < nums.length; index += 1) {
        if (nums[index] > max) {
            max = nums[index]
        }
    }
    return max;
}; 


console.log(maxValue([4, 7, 2, 8, 10, 9])); // -> 10
console.log(maxValue([10, 5, 40, 40.3])); // -> 40.3
console.log(maxValue([-5, -2, -1, -11])); // -> -1
console.log(maxValue([42])); // -> 42
console.log(maxValue([1000, 8])); // -> 1000
console.log(maxValue([1000, 8, 9000])); // -> 9000
console.log(maxValue([2, 5, 1, 1, 4])); // -> 5
