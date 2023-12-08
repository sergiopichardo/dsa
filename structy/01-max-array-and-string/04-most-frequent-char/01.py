"""
most frequent char
Write a function, mostFrequentChar, that takes in a string as an argument. The function should return the most frequent character of the string. If there are ties, return the character that appears earlier in the string.

You can assume that the input string is non-empty.
"""

"""
n = length of string
Time: O(n)
Space: O(n)
"""

def most_frequent_char(word: str) -> str:
    char_dict = {char: word.count(char) for char in set(word)}

    most_freq_letter: str = word[0]
    most_freq_value: int = char_dict[most_freq_letter]

    sliced_word = word[1:]
    
    for letter in sliced_word:
        if char_dict[letter] > most_freq_value:
            most_freq_value = char_dict[letter]
            most_freq_letter = letter

    return most_freq_letter

print(most_frequent_char('bookeep')) # 'o'
print(most_frequent_char('bookeeper')) # 'e'
print(most_frequent_char('david')) # 'd'
print(most_frequent_char('abby')) # 'b'
print(most_frequent_char('mississippi')) # 'i'
print(most_frequent_char('potato')) # 'o'
print(most_frequent_char('eleventennine')) # 'e'
print(most_frequent_char("riverbed")) # 'r'

