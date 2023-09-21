/*
pair product
Write a function, pairProduct, that takes in an array and a target product as arguments. The function should return an array containing a pair of indices whose elements multiply to the given target. The indices returned must be unique.

Be sure to return the indices, not the elements themselves.

There is guaranteed to be one such pair whose product is the target.
*/

/*
INPUT: 
--> numbers: number[]
--> targetProduct: number

OUTPUT: 
--> [number, number]

RULES 
- it should return an array of a pair of indices whose elements multiply to the given target
- the indices returned must be unique 
- there will always be a valid pair of indices 

DATA STRUCTURE 
- object: to store values we've seen 
- great lookup times O(1)

ALGORITHM 
- set lookup --> {}
- iterate over each `number` in `numbers` array 
    - set `number` --> the number at the current index 
    - set `complement` --> (`targetProduct` / `number`)
    - if `complement` is a key in `lookup`
        - return [lookup[complement], index]
    - otherwise 
        - set `lookup[number]` --> index

COMPLEXITY 
N: the length of the array
- time: O(N)
- space: O(1)
*/


const pairProduct = (numbers, targetProduct) => {
    const lookup = {}; 

    for (let index = 0; index < numbers.length; index += 1) {
        const currentNumber = numbers[index]; 
        const complement = targetProduct / currentNumber; 
        if (complement in lookup) {
            return [lookup[complement], index];
        } else {
            lookup[currentNumber] = index; 
        }
    }
};

console.log(pairProduct([3, 2, 5, 4, 1], 8)); // -> [1, 3]
console.log(pairProduct([3, 2, 5, 4, 1], 10)); // -> [1, 2]
console.log(pairProduct([4, 7, 9, 2, 5, 1], 5)); // -> [4, 5]
console.log(pairProduct([4, 7, 9, 2, 5, 1], 35)); // -> [1, 4]
console.log(pairProduct([3, 2, 5, 4, 1], 10)); // -> [1, 2]
console.log(pairProduct([4, 6, 8, 2], 16)); // -> [2, 3]