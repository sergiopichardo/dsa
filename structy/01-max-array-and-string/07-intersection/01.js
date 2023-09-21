/**
Intersection
Write a function, intersection, that takes in two arrays, a,b, as arguments. The function should return a new array containing elements that are in both of the two arrays.

You may assume that each input array does not contain duplicate elements.
*/

/*
INPUT: number[], number[]
OUTPUT: number[]

RULES 
- it should take 2 array of numbers and return a new array containing elements
    that are included in both the two arrays
- Assume that each input array does not have duplicate numbers

DATA STRUCTURE 
- object: to store the number as key and true as a value
{ 
    4: true,
    2: true,
    1: true,
    6: true
}
array: [2, 6]

ALGORITHM 
- set `numberLookup` --> {}
- set `numbersInCommon` --> []

- select the smallest array 
- select the larget array 

- for each `number` in `arrayA`
    - create a property where key: number and value: true 

- iterate over each `number` of `arrayB` 
    - if `number` is in `numberLookup`
        - append `number` to `numbersICommon`

- return `numbersInCommon`

COMPLEXITY
N: length of array A
M: length of array B
- time: O(N+M)
- space: O(n)
*/

const intersection = (a, b) => {
    const numbersLookup = {}; 
    const numbersInCommon = [];

    const [shortest, longest] = [a, b].sort((a, b) => a.length > b.length)

    for (const number of longest) {
        numbersLookup[number] = true;
    }

    for (const number of shortest) {
        if (numbersLookup[number]) {
            numbersInCommon.push(number);
        }
    }

    return numbersInCommon;
}




console.log(intersection([4,2,1,6], [3,6,9,2,10])) // -> [2,6]
console.log(intersection([2,4,6], [4,2])) // -> [2,4]
console.log(intersection([4,2,1], [1,2,4,6])) // -> [1,2,4]
console.log(intersection([0,1,2], [10,11])) // -> []

const a = [];
const b = [];
for (let i = 0; i < 50000; i += 1) {
  a.push(i);
  b.push(i);
}
console.log(intersection(a, b)) // -> [0,1,2,3,..., 49999]