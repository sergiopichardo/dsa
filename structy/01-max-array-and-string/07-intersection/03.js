/*
    n = length of array a, m = length of array b
    Time: O(n+m)
    Space: O(n)
*/

const intersection = (a, b) => {
    const result = [];
    const setA = new Set(a);
    for (let item of b) {
      if (setA.has(item)) {
        result.push(item);
      }
    }
    return result;
};

