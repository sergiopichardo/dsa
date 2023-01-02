// Solution 3
/*
- Iterate over the array of numbers
- calculate the "complement" of the current number in the array
  -> complement = target - current number
- if the complement is a key in the `cache` object, 
  it means that the `complement` + the "cached number" will add up to the `target` 
  - in that case we can return the cached number index and the current complement index in an array
- add the current number as a key to the cache object and the index as the value
*/

// Time: O(N), Space: O(N)
const twoSum = (nums, target) => {
  const cache = {};
  
  for (let index = 0; index < nums.length; index++) {
    const complement = target - nums[index]; 
    if (complement in cache) {
      return [cache[complement], index]
    }
    cache[nums[index]] = index; 
  }
}; 

console.log(twoSum([2, 7, 11, 15], 9)); // [0, 1]
console.log(twoSum([3, 2, 4], 6));      // [1, 2] 
console.log(twoSum([3, 3], 6));         // [0, 1]
