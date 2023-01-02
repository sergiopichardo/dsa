/*
Complexity 
- Time: O(N)
- Space: O(N)
*/

// solution 1
const twoSum = (nums, target) => {
  const complements = {};   
  // iterate over each number in the `nums` array
  for (let index = 0; index < nums.length; index++) {
    
    // if the current number is a key in the `complements` object
    // it means that we have already found a number that added with the 
    // current number adds up to the `target` number. 
    if (nums[index] in complements) { 
      // return the complement index, and the current index
      return [complements[nums[index]], index]
    }
    
    // calculate the complement, set it as a key 
    // and set the value as the current index
    const complement = target - nums[index]; 
    complements[complement] = index;
  }
}; 

// solution 2
// const twoSum = (nums, target) => {
//   const complements = {};   
//   for (let index = 0; index < nums.length; index++) {
//     const complementIndex = complements[nums[index]]

//     if (complementIndex !== undefined) {
//       return [complements[nums[index]], index]
//     }
    
//     const complement = target - nums[index]; 
//     complements[complement] = index;
//   }
// }; 



console.log(twoSum([2, 7, 11, 15], 9)); // [0, 1]
console.log(twoSum([3, 2, 4], 6));      // [1, 2] 
console.log(twoSum([3, 3], 6));         // [0, 1]


/*
Key => Value 
complement => index 

- Why is this important? 
  - if we know that a number 

- SET complements = []
- FOR each number in `nums` 
  - IF the current number already exists as a key in the complements object 
    - return array with two items: 
      - 0: complement index
      - 1: current number index
  - ELSE 
    - A. Calculate the complement of the current number 
        -> complement = target - current number 
    - B. Set a new property in complements object where: 
      - key: complement 
      - value: current index 
*/

