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


BIG O
- time: O(N*M)
- space: O(N*M)

*/

const uncompress = (s) => {
    let numbers = '0123456789'
    let result = ''; 
    let i = 0; 
    let j = 0; 

    while (j < s.length) {
        if (numbers.includes(s[j])) {
            j += 1;
        } else {
            const num = Number(s.slice(i, j));
            for (let count = 0; count < num; count += 1) {
                result += s[j];
            }
            j += 1;
            i = j; 
        }
    }

    return result;

}; 


console.log(uncompress("12c3a")); // -> 'ccccccccccccaaa'
console.log(uncompress("2c3a1t")); // -> 'ccaaat'
console.log(uncompress("4s2b")); // -> 'ssssbb'
console.log(uncompress("2p1o5p")); // -> 'ppoppppp'
console.log(uncompress("3n12e2z")); // -> 'nnneeeeeeeeeeeezz'
console.log(uncompress("127y")); // ->'yyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyy'
