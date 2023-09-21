/*
    n = length of array a, m = length of array b
    Time: O(n*m)
    Space: O(min(n,m))
*/
const intersection = (a, b) => {
    const result = [];
    for (let item of b) {
        if (a.includes(item)) {
        result.push(item);
        }
    }
    return result;
};