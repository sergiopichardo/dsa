from collections import Counter

"""
anagrams
Write a function, anagrams, that takes in two strings as arguments. The function should return a boolean indicating whether or not the strings are anagrams. Anagrams are strings that contain the same characters, but in any order.
"""

"""
INPUT: string, string
OUTPUT: boolean 

RULES
- it returns true if the strings are anagrams, and false otherwise 
- assume inputs will contain only lowercase, alphabetic characters
- Definitions
    - Anagram: a string that contain the same characters, but in different order

Algorithm 
- create a dictionary of string1 with its letter count
- for each letter in string2
    - if the current letter is in string1 dictionary
        - subtract 1
- iterate over string1 dictionary once again 
    - if there's a value greater not equal to 0
        - return false
- return true 


Complexity: 
- n = string1 length
- m = string2 length
- Time: O(n + m)
- Space: ~O(n+m)
"""


def count_letters(string):
    count = {}

    for char in string:
        if char not in count:
            count[char] = 0
        count[char] += 1

    return count

# def count_letters(string):
#     return {char: string.count(char) for char in set(string)}

# def anagrams(str1, str2):
#     return Counter(str1) == Counter(str2)

def anagrams(str1, str2):
    str1Dict = count_letters(str1)
    str2Dict = count_letters(str2)
    return str1Dict == str2Dict


    

print(anagrams('restful', 'fluster')) # -> True
print(anagrams('cats', 'tocs')) # -> False
print(anagrams('monkeyswrite', 'newyorktimes')) # -> True
print(anagrams('paper', 'reapa')) # -> False
print(anagrams('elbow', 'below')) # -> True
print(anagrams('tax', 'taxi')) # -> False
print(anagrams('taxi', 'tax')) # -> False
print(anagrams('night', 'thing')) # -> True
print(anagrams('abbc', 'aabc')) # -> False
print(anagrams('po', 'popp')) # -> false
print(anagrams('pp', 'oo')) # -> false