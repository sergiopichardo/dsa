/*
five sort

Write a function, fiveSort, that takes in an array of numbers as an argument. 
The function should rearrange elements of the array such that all 5s appear at the end. 
Your function should perform this operation in-place by mutating the original array. 
The function should return the array.

Elements that are not 5 can appear in any order in the output, as long as all 5s are at the end of the array.
*/

/*
INPUT: 
- numbers: number[]

OUTPUT: 
- sortedFives: number[]

RULES 
- in-place sorting 
    - it should rearrange elements of the array such that all 5s appear at the end 
    - it should mutate original array in place and return the sorted array
- Assumptions
    - We'll always get a valid array with at least one number 

DATA STRUCTURE 
- 

ALGORITHM 
- count all the fives in the array 
- iterate over the original array and remove all the fives
- add all the fives counted at the end of the array
- return the original array 

COMPLEXITY 
N: items in the array 
- time: O(N)
- space: O(N)

*/

// method 1
const fiveSort = (numbers) => {
    const fivesCount = numbers.reduce((acc, number) => {
        if (number === 5) {
            acc += 1;
        }
        return acc;
    }, 0)

    const numbersCopy = numbers.slice(0);
    numbersCopy.forEach((number, index) => {
        if (number === 5) {
            numbers.splice(index, 1);
        }
    });

    for (let index = 0; index < fivesCount; index += 1) {
        numbers.push(5)
    }

    return numbers;
};

console.log(fiveSort([12, 5, 1, 5, 12, 7])); // -> [12, 7, 1, 12, 5, 5] 
// console.log(fiveSort([5, 2, 5, 6, 5, 1, 10, 2, 5, 5])); // -> [2, 2, 10, 6, 1, 5, 5, 5, 5, 5] 
// console.log(fiveSort([5, 5, 5, 1, 1, 1, 4])); // -> [4, 1, 1, 1, 5, 5, 5] 
// console.log(fiveSort([5, 5, 6, 5, 5, 5, 5])); // -> [6, 5, 5, 5, 5, 5, 5] 
// console.log(fiveSort([5, 1, 2, 5, 5, 3, 2, 5, 1, 5, 5, 5, 4, 5])); // -> [4, 1, 2, 1, 2, 3, 5, 5, 5, 5, 5, 5, 5, 5] 

// const fives = new Array(20000).fill(5);
// const fours = new Array(20000).fill(4);
// const nums = [...fives, ...fours];
// console.log(fiveSort(nums));
// twenty-thousand 4s followed by twenty-thousand 5s
// -> [4, 4, 4, 4, ..., 5, 5, 5, 5]