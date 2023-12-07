"""
uncompress
Write a function, uncompress, that takes in a string as an argument. The input string will be formatted into multiple groups according to the following pattern:

<number><char>

for example, '2c' or '3a'.
The function should return an uncompressed version of the string where each 'char' of a group is repeated 'number' times consecutively. You may assume that the input string is well-formed according to the previously mentioned pattern.
"""

"""
Complexity
n = number of groups
m = max num found in any group
Time: O(n*m)
Space: O(n*m)
"""

def uncompress(s): 
    result = []
    i = 0
    j = 0

    while j < len(s):
        if s[j].isdigit():
            j += 1
        else: 
            num = int(s[i:j])
            result.append(s[j] * num)
            j += 1
            i = j
    
    return ''.join(result)

    
    
print(uncompress("12c3a"))   # 'ccccccccccccaaa'
print(uncompress("2c3a1t"))  # 'ccaaat'
print(uncompress("4s2b"))    # 'ssssbb'
print(uncompress("2p1o5p"))  # 'ppoppppp'
print(uncompress("3n12e2z")) # 'nnneeeeeeeeeeeezz'
print(uncompress("127y"))    # ->'yyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyy'
