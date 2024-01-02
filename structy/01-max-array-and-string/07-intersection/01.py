"""
Intersection
Write a function, intersection, that takes in two arrays, a,b, as arguments. The function should return a new array containing elements that are in both of the two arrays.

You may assume that each input array does not contain duplicate elements.
"""

"""
Complexity
- Time: O(N+M)
- Space: O(1)
"""

def intersection(l1, l2):
    l1 = set(l1)
    l2 = set(l2)

    seen = {}
    common = []

    for num in l1:
        seen[num] = True

    for num in l2:
        if num in seen:
            common.append(num)

    return common


print(intersection([4,2,1,6], [3,6,9,2,10])) # -> [2,6]
print(intersection([2,4,6], [4,2]))          # -> [2,4]
print(intersection([4,2,1], [1,2,4,6]))      # -> [1,2,4]
print(intersection([0,1,2], [10,11]))        # -> []

a = []
b = []

for i in range(0, 50_000):
    a.append(i)
    b.append(i)

print(intersection(a, b))       # -> [0,1,2,3,..., 49999]