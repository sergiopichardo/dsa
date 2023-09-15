const compress = (word) => {
    let result = []; 
    let slowPointer = 0; 
    let fastPointer = 0; 

    while (fastPointer <= word.length) {
        if (word[slowPointer] === word[fastPointer]) {
            fastPointer += 1;
        } else {
            const count = fastPointer - slowPointer; 
            if (count === 1) {
                result.push(word[slowPointer]);
            } else {
                result.push(count, word[slowPointer]);
            }
            slowPointer = fastPointer;
        }
    }

    return result.join('');
}


console.log(compress('x')); // -> 'x'
console.log(compress('a')); // -> 'a'
console.log(compress('s')); // -> 's'
console.log(compress('ccaaatsss')); // -> '2c3at3s'
console.log(compress('ssssbbz')); // -> '4s2bz'
console.log(compress('ppoppppp')); // -> '2po5p'
console.log(compress('nnneeeeeeeeeeeezz')); // -> '3n12e2z'
console.log(compress('yyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyy')); 
// -> '127y'