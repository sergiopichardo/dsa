/*
compress
Write a function, compress, that takes in a string as an argument. The function should return a compressed version of the string where consecutive occurrences of the same characters are compressed into the number of occurrences followed by the character. Single character occurrences should not be changed.

'aaa' compresses to '3a'
'cc' compresses to '2c'
't' should remain as 't'
You can assume that the input only contains alphabetic characters.
*/

/*
INPUT
- word: string 

OUTPUT: string 
--> The compressed string

RULES
- Write a function called `compress` that takes a string as argument, `word`
- It should return a compressed version of the string 
    - "compressed" means that consecutive occurrences of the same character are compressed 
      into the number followed by the character 
- Single character occurrences should not be changed 
- characters in the input string will only contain lower-case alphabetic characters (a-z)
- digits in the output string will only contain the numbers 1-9
- Assumptions
    - assume that we'll get a string of at least size 1

DATA STRUCTURE 
- string 

EXPLORATION 
"ccaaatsss"

ALGORITHM 
- guard clause: if the input string is of size 1 
    - return the same string 

- set `slowPointer` to 0
- set `fastPointer` to 0
- set `result` to ''
- iterate over each letter in the `word` input 
    | start: 0
    | stop: `fastPointer` <=  `word`.length
    | step: increment by 1

    - if the letter at slowPointer is not equal to the letter at fastPointer
        - slice `word` from `slowPointer` up to but not including `fastPointer`, get the length, and store in `count` variable
        - if count is EQUAL TO 1
            - append the current `letter` to `result`
        - otherwise 
            - append the current `count` and the `letter` to `result`
        
        - set `slowPointer` to `fastPointer` 
- return result

COMPLEXITY (BIG O)
N: the input string length

- Time: O(N)
- Space: O(N) 
*/

const compress = (word) => {
    let result = ''; 
    let slowPointer = 0; 

    for (let fastPointer = 0; fastPointer <= word.length; fastPointer += 1) {
        if (word[slowPointer] !== word[fastPointer]) {
            const count = word.slice(slowPointer, fastPointer).length;
            if (count === 1) {
                result += word[slowPointer];
            } else {
                result += count + word[slowPointer];
            }
            slowPointer = fastPointer;
        }    
    }

    return result; 
}; 


console.log(compress('x')); // -> 'x'
console.log(compress('a')); // -> 'a'
console.log(compress('s')); // -> 's'
console.log(compress('ccaaatsss')); // -> '2c3at3s'
console.log(compress('ssssbbz')); // -> '4s2bz'
console.log(compress('ppoppppp')); // -> '2po5p'
console.log(compress('nnneeeeeeeeeeeezz')); // -> '3n12e2z'
console.log(compress('yyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyy')); 
// -> '127y'