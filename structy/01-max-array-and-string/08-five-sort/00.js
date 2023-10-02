
// const fiveSort = (numbers) => {
//     let leftPointer = 0; 
//     let rightPointer = numbers.length - 1;
  
//     while (leftPointer <= rightPointer) {
//       if (numbers[rightPointer] === 5) {
//         rightPointer -= 1;
//       } else if (numbers[leftPointer] === 5) {
//         [numbers[leftPointer], numbers[rightPointer]] = [numbers[rightPointer], numbers[leftPointer]]
//         leftPointer += 1;
//       } else {
//         leftPointer += 1;
//       }
//     }
  
//     return numbers;
//   }