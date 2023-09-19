/*
most frequent char
Write a function, mostFrequentChar, that takes in a string as an argument. The function should return the most frequent character of the string. If there are ties, return the character that appears earlier in the string.

You can assume that the input string is non-empty.
*/

/*
INPUT
- word: string

OUTPUT: string
- mostFrequentLetter: string (char)

RULES 
- find the most frequent char in the string 
- if there are ties, repeat the character that appers earlier in the string
- assumptions: 
    - only lowercase characters will be given 
    - a string of a length of 1 or greater will always be provided

EXPLORATION 
T1 
input: "bookeep"
output: "o"

- track quantity
- track the current most frequent char

DATA STRUCTURE 
- string: to track current char 
- number: to track frequency of char

ALGORITHM 
- set `letterCounter` to { [letter]: frequency of the letter }
- set `mostFrequentLetter` to the first letter in the `word` string 
- iterate over each `letter` of `word` string 
    - if the letter key has a value in `letterCounter` > than the value associated with the `mostFrequentLetter`
        - set the `mostFrquentLetter` to the current letter
- return `mostFrequentLetter`


COMPLEXITY
N: length of the input string

- time: O(N)
- space: O(1)

*/

const mostFrequentChar = (word) => {
    const letterCounter = [...word].reduce((acc, curr) => {
        acc[curr] = acc[curr] ? ++acc[curr] : 1
        return acc;
    }, {}); 
    
    let mostFrequentLetter = word[0]; 

    word.slice(1).split('').forEach(letter => {
        if (letterCounter[letter] > letterCounter[mostFrequentLetter]) {
            mostFrequentLetter = letter
        }
    });

    return mostFrequentLetter;
};

console.log(mostFrequentChar('bookeeper')); // -> 'e'
console.log(mostFrequentChar('david')); // -> 'd'
console.log(mostFrequentChar('abby')); // -> 'b'
console.log(mostFrequentChar('mississippi')); // -> 'i'
console.log(mostFrequentChar('potato')); // -> 'o'
console.log(mostFrequentChar('eleventennine')); // -> 'e'
console.log(mostFrequentChar("riverbed")); // -> 'r'