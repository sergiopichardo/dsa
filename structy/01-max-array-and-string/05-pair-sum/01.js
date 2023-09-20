/*
pair sum
Write a function, pairSum, that takes in an array and a target sum as arguments. The function should return an array containing a pair of indices whose elements sum to the given target. The indices returned must be unique.

Be sure to return the indices, not the elements themselves.

There is guaranteed to be one such pair that sums to the target.
*/

/*
INPUT: 
--> `numbers`: number[]
--> `targetSum`: number

OUTPUT
--> `sumResult`: [number, number]


RULES 
- it should return an array containing a pair of "indices" of the two elements that add up to the given `targetSum`
- the two indices must be unique 
- there will ALWAYS be a pair of indices that add up to the `targetSum`

TESTS 
T1
input: [3, 2, 5, 4, 1], 8
output: [0, 2]

{
    3: 0,
    2: 1,
    5: 2,
    4: 3,
    1: 4 
}

DATA STRUCTURE 
- object: lookup table 
- very efficient lookup times O(1)

MENTAL MODEL 
- create an object to store the "number" we've seen and their "index"
- complement = targetSum - currentNumber
- if the complement is in the lookup table, then we have a valid pair
- we always need to set the new numbe rin the lookup table 

ALGORITHM 
- set `lookup` to an empty object 
- iterate for each `currentNumber` in the `numbers` array 
    - set `complement` to `targetSum` - `currentNumber`
    - if the `complement` is a key in the `lookup` object
        - return [complementIndex, currentIndex]
    - otherwise 
        - set prop in lookup where key: currentNumber, and value: currentNumber's index
*/

const pairSum = (numbers, targetSum) => {
    const lookup = {};

    for (let index = 0; index < numbers.length; index += 1) {
        const currentNumber = numbers[index]; 
        const complement = targetSum - currentNumber;
        if (complement in lookup) {
            return [lookup[complement], index]
        } else {
            lookup[currentNumber] = index;
        }
    }
}; 

console.log(pairSum([3, 2, 5, 4, 1], 8)); // -> [0, 2]
console.log(pairSum([4, 7, 9, 2, 5, 1], 5)); // -> [0, 5]
console.log(pairSum([4, 7, 9, 2, 5, 1], 3)); // -> [3, 5]
console.log(pairSum([1, 6, 7, 2], 13)); // -> [1, 2]
console.log(pairSum([9, 9], 18)); // -> [0, 1]
console.log(pairSum([6, 4, 2, 8 ], 12)); // -> [1, 3]