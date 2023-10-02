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
- Array 

EXPLORATION 
1. multiple pointers 

     L
[12, 5, 1, 5, 12, 7]
                  R

Cases: 
- if number at `L` !== 5, then increment `L`
- otherwise if number at `R` === 5, then decrement `R`
- otherwise if number at `L` === 5 (is 5), then swap number at `L` with number at `R`

ALGORITHM (in-place)
- set L at index 0 
- set R at index numbers.length-1
- for each num in numbers
    - if number at L === 5 && number at R is not 5
        - swap number at L with number at R
    - if number at L !== 5
        - increment L by 1 
    - else if number at R === 5
        - decrement R by 1

COMPLEXITY 
N: items in the array 
- time: O(N)
- space: O(1)
*/

// method 1
const fiveSort = (numbers) => {
    let leftPointer = 0; 
    let rightPointer = numbers.length - 1; 

    while (leftPointer < rightPointer) {
        if (numbers[leftPointer] === 5 && numbers[rightPointer] !== 5) {
            [numbers[leftPointer], numbers[rightPointer]] = [numbers[rightPointer], numbers[leftPointer]];
        } 
        
        // set number for next iteration
        if (numbers[leftPointer] !== 5) {
            leftPointer += 1;
        }

        if (numbers[rightPointer] === 5) {
            rightPointer -= 1;
        }
    }

    return numbers;
};

console.log(fiveSort([12, 5, 1, 5, 12, 7])); // -> [12, 7, 1, 12, 5, 5] 
console.log(fiveSort([5, 2, 5, 6, 5, 1, 10, 2, 5, 5])); // -> [2, 2, 10, 6, 1, 5, 5, 5, 5, 5] 
console.log(fiveSort([5, 5, 5, 1, 1, 1, 4])); // -> [4, 1, 1, 1, 5, 5, 5] 
console.log(fiveSort([5, 5, 6, 5, 5, 5, 5])); // -> [6, 5, 5, 5, 5, 5, 5] 
console.log(fiveSort([5, 1, 2, 5, 5, 3, 2, 5, 1, 5, 5, 5, 4, 5])); // -> [4, 1, 2, 1, 2, 3, 5, 5, 5, 5, 5, 5, 5, 5] 

const fives = new Array(20000).fill(5);
const fours = new Array(20000).fill(4);
const nums = [...fives, ...fours];
console.log(fiveSort(nums));
// twenty-thousand 4s followed by twenty-thousand 5s
// -> [4, 4, 4, 4, ..., 5, 5, 5, 5]//