

def most_frequent_char(s):
    count = {}
    for char in s:
        if char not in count:
            count[char] = 0
        count[char] += 1

    best = None

    for char in s: 
        if best is None or count[char] > count[best]:
            best = char 

    return best

print(most_frequent_char('bookeep')) # 'o'
print(most_frequent_char('bookeeper')) # 'e'
print(most_frequent_char('david')) # 'd'
print(most_frequent_char('abby')) # 'b'
print(most_frequent_char('mississippi')) # 'i'
print(most_frequent_char('potato')) # 'o'
print(most_frequent_char('eleventennine')) # 'e'
print(most_frequent_char("riverbed")) # 'r'