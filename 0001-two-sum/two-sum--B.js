/*
We can use a hashmap to map the current `value` to the current `index`. 

Visit and Move 1 and add value to hash map

*/

/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number[]}
 */
const twoSum = (nums, target) => {
  const complements = {}
  for (let index = 0; index < nums.length; index++) {
    if (complements[target - nums[index]]) {
      return []
    } 
    complements[index] = nums[index]
  }; 

  

  console.log(complements)
}; 


console.log(twoSum([2, 7, 11, 15], 9)); // [0, 1]
// console.log(twoSum([3, 2, 4], 6));      // [1, 2] 
// console.log(twoSum([3, 3], 6));         // [0, 1]