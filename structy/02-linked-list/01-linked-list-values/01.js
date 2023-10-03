/*
linked list values
Write a function, linkedListValues, that takes in the head of a linked list as an argument. 
The function should return an array containing all values of the nodes in the linked list.
*/

/*
INPUT: LinkedList Node
OUTPUT: string[]

RULES 
- it should return an array containing all values of the nodes in the linked list

DATA STRUCTURE 
- array: to store each node value

ALGORITHM
- set `collectedValues` to Array<Empty>
- while the current node is NOT NULL 
    - push the current node's value into `collectedValues` array 
    - set current node to the value of the current node's next property
- return `collectedValues`

COMPLEXITY 
- N: the number of nodes in the linked list
- Time: O(N)
- Space: O(N)
*/

import Node from '../node.js';

// class Node {
//   constructor(val) {
//     this.val = val;
//     this.next = null;
//   }
// }

// // Iterative Solution
// const linkedListValues = (head) => {
//     const collectedValues = []; 
//     let currentNode = head; 
//     while (currentNode !== null) {
//         collectedValues.push(currentNode.val);
//         currentNode = currentNode.next;
//     }
//     return collectedValues;
// };

// Recursive Solution 
const linkedListValues = (head, values=[]) => {
    // base case 
    if (head === null) {
        return values;
    }

    values.push(head.val);

    return linkedListValues(head.next, values)
};

const a = new Node("a");
const b = new Node("b");
const c = new Node("c");
const d = new Node("d");

a.next = b;
b.next = c;
c.next = d;

// a -> b -> c -> d

console.log(linkedListValues(a)); // -> [ 'a', 'b', 'c', 'd' ]
const x = new Node("x");
const y = new Node("y");

x.next = y;

// x -> y

console.log(linkedListValues(x)); // -> [ 'x', 'y' ]
const q = new Node("q");

// q

console.log(linkedListValues(q)); // -> [ 'q' ]
console.log(linkedListValues(null)); // -> [ ]