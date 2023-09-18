/*
anagrams
Write a function, anagrams, that takes in two strings as arguments. The function should return a boolean indicating whether or not the strings are anagrams. Anagrams are strings that contain the same characters, but in any order.
*/

/*
INPUT: string, string
OUTPUT: boolean 

RULES
- it should return boolean if the two strings are anagrams 
- (DEF) Anagram: strings that contain the same characters, but in any order 
- it should contain the same characters and the same character count 
- 2 empty strings are considered anagrams of each other
- Guard Clauses
    - if the 2 input strings do not have the same lengths, return FALSE 
    - if the 2 input string are empty, return true
- Assumptions
    - assume that all input strings will only contain, lowercase alphabetic characters

EXPLORATION 
T1
input: "restful", "fluster"
output: true
reason: 
- both strings have the same length
- both strings have the same quantity of the same characters 

T2
input: "tax", "taxi"
output: false
reason: 
- strings DO NOT have the same length
- strings do not have the same characters

T3
input: "taxx", "taxi"
output: false
reason: 
- strings have the same lenght but
- strings do not have the same characters count of each character


DATA STRUCTURE
- Object: count all character in `sourceWord`

ALGORITHM 
- if `sourceWord` and `targetWord` don't have the same length
    - return false 
- if `sourceWord` and `targetWord` are empty strings 
    - return true 

- set `sourceCounter` = { count all the characters in `sourceString` and store in an object }
- iterate over each character of the `targetWord`
    - if the current character is in `sourceCounter`
        - subtract 1 from that property
    - otherwise
        - return false  
- set totalCharacterCount = reduce `sourceCounter` 
- if totalCharacterCount is 0 
    - return true 
- otherwise
    - return false 

COMPLEXITY
N: length of source word
M: length of target word

- time: O(N+M)
- space: O(1) --> max is 26 properties in the object
*/

const anagrams = (sourceWord, targetWord) => {
    if (sourceWord.length !== targetWord.length) {
        return false; 
    }

    if (sourceWord === '' && targetWord === '') {
        return true;
    }

    const sourceCounter = [...sourceWord].reduce((acc, curr) => {
        acc[curr] = acc[curr] ? ++acc[curr] : 1
        return acc;
    }, {});

    for (const letter of targetWord) {
        if (!sourceCounter[letter]) {
            return false;
        } else {
            sourceCounter[letter] -= 1;
        }
    }

    const totalCharacterCount = Object
        .values(sourceCounter)
        .reduce((acc, value) => acc + value, 0);

    // const allZeros = Object
        // .values(sourceCounter)
        // .every(value => value === 0);

    return totalCharacterCount === 0;
}; 

console.log(anagrams('', '')); // -> true
console.log(anagrams('restful', 'fluster')); // -> true
console.log(anagrams('monkeyswrite', 'newyorktimes')); // -> true
console.log(anagrams('elbow', 'below')); // -> true
console.log(anagrams('night', 'thing')); // -> true


console.log(anagrams('fluster', '')); // -> false
console.log(anagrams('', 'fluster')); // -> false
console.log(anagrams('cats', 'tocs')); // -> false
console.log(anagrams('paper', 'reapa')); // -> false
console.log(anagrams('tax', 'taxi')); // -> false
console.log(anagrams('taxi', 'tax')); // -> false
console.log(anagrams('abbc', 'aabc')); // -> false
console.log(anagrams('po', 'popp')); // -> false
console.log(anagrams('pp', 'oo')) // -> false