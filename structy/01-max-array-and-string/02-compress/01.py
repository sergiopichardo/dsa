"""
compress
Write a function, compress, that takes in a string as an argument. The function should return a compressed version of the string where consecutive occurrences of the same characters are compressed into the number of occurrences followed by the character. Single character occurrences should not be changed.

'aaa' compresses to '3a'
'cc' compresses to '2c'
't' should remain as 't'
You can assume that the input only contains alphabetic characters.
"""

"""
Complexity 
- N = the length of the string 
- Time: O(N)
- Space: O(N)
"""

# String -> String
def compress(s): 
    s += '$'
    result = []
    slowPointer = 0
    fastPointer = 0

    while fastPointer < len(s):
        if s[fastPointer] == s[slowPointer]:
            fastPointer += 1
        else: 
            count = fastPointer - slowPointer
            if count == 1: 
                result.append(s[slowPointer])
            else: 
                result.append(str(count))
                result.append(s[slowPointer])
            slowPointer = fastPointer
            
    return ''.join(result)

print(compress('x'))  # 'x'
print(compress('a')) # 'a'
print(compress('s')) # 's'
print(compress('ccaaatsss')) # '2c3at3s'
print(compress('ssssbbz')) # '4s2bz'
print(compress('ppoppppp')) # '2po5p'
print(compress('nnneeeeeeeeeeeezz')) # '3n12e2z'
print(compress('yyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyy')); 
# '127y'