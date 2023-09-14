/*
uncompress
Write a function, uncompress, that takes in a string as an argument. The input string will be formatted into multiple groups according to the following pattern:

<number><char>

for example, '2c' or '3a'.
The function should return an uncompressed version of the string where each 'char' of a group is repeated 'number' times consecutively. You may assume that the input string is well-formed according to the previously mentioned pattern.
*/

/*
INPUT: 
- word: string

OUTPUT: 
- uncompressedResult: string 

RULES
- the input string will be formatted into multiple groups following
  the format: 
    <NUMBER><CHAR>

- The function should return an uncompressed version of the string where 
  each 'char' of a group is repeated 'number' times consecutively.

- You may assume that the input string will always follow the number-char pattern 

- Assumptions
  - The number range will be from 1-9, zero is never included in the input string 

EXAMPLES 
T1
input: "2c"
output: "cc"

T2
input: "3a"
output: "aaa"

DATA STRUCTURE 
- string


ALGORITHM 
- set `uncompressedResult` to an empty string 
- for each `char` in the `word` array
    - set `repeatCountString` to empty string 
    - if `char` is a digit 
        - concat the current digit to `repeatCountString`
    - otherwise 
        - set `repeatCount` to conversion of `repeatCountString` to a number
        - iterate `repeatCount` many times 
            - concat the current `char` to `uncompressedResult`
        - set `repeatCountString` to an empty string again
- return uncompressedResult 

BIG O
N: # of groups
M: max number for any group


- time: O(N*M)
- space: O(N*M)
*/

const uncompress = (word) => {
    let uncompressedResult = ''; 
    let repeatCountString = ''; 

    for (let char of word) {
        if (char in [...'123456789']) {
            repeatCountString += char;
        } else {
            let repeatCount = Number(repeatCountString);
            repeatCountString = ''; 
            
            for (let index = 0; index < repeatCount; index += 1) {
                uncompressedResult += char;
            }
        }
    }
    return uncompressedResult;
}



console.log(uncompress("12c3a")); // -> 'ccccccccccccaaa'
console.log(uncompress("2c3a1t")); // -> 'ccaaat'
console.log(uncompress("4s2b")); // -> 'ssssbb'
console.log(uncompress("2p1o5p")); // -> 'ppoppppp'
console.log(uncompress("3n12e2z")); // -> 'nnneeeeeeeeeeeezz'
console.log(uncompress("127y")); // ->'yyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyy'
