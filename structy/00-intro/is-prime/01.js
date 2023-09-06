/*
is prime
Write a function, isPrime, that takes in a number as an argument. The function should return a boolean indicating whether or not the given number is prime.

A prime number is a number that is only divisible by two distinct numbers: 1 and itself.

For example, 7 is a prime because it is only divisible by 1 and 7. For example, 6 is not a prime because it is divisible by 1, 2, 3, and 6.

You can assume that the input number is a positive integer.
*/

/*
INPUT: number 
OUTPUT: boolean 
- true: the number is prime 
- false: the number is NOT prime 

RULES 
- definition for prime number
    - a number that is only divisible by 1 and itself 

EXAMPLES
T1
- input: 6
- output: false 
- because 6 is divisible by 1, 2, 3, and 6

T2
- input: 7
- output: true 
- because 7 is only divisible by 1 or 7

DATA STRUCTURE 
- number 

ALGORITHM
- if n === 1 return false  
- iterate from 2 up to but not including `input`
    - if the value is divisible by the current number
        - return false 
- return true 

COMPLEXITY
- time: O(N)
- space: O(1)
*/

const isPrime = (n) => {
    if (n === 1) {
        return false;
    }

    for (let value = 2; value < n; value += 1) {
        if ((n % value) === 0) {
            return false;
        }
    }

    return true;
};

console.log(isPrime(2)); // -> true
console.log(isPrime(3)); // -> true
console.log(isPrime(4)); // -> false
console.log(isPrime(5)); // -> true
console.log(isPrime(6)); // -> false
console.log(isPrime(7)); // -> true
console.log(isPrime(8)); // -> false
console.log(isPrime(25)); // -> false
console.log(isPrime(31)); // -> true
console.log(isPrime(2017)); // -> true
console.log(isPrime(2048)); // -> false
console.log(isPrime(1)); // -> false
console.log(isPrime(713)); // -> false
