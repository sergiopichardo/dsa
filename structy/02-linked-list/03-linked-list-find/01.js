/*
linked list find
Write a function, linkedListFind, that takes in the head of a linked list and a target value. The function should return a boolean indicating whether or not the linked list contains the target.
*/

/*
INPUT: Node, string 
OUTPUT: boolean 

RULES 
- write a function called `linkedListFind` with the following params: 
    - head: Node (head of the linked list)
    - target: the string value we need to find 
- it should return TRUE if the value is found and FALSE otherwise
- the values we expect are alphabetic, lowercase strings

DATA STRUCTURE 
- boolean

ALGORITHM
- while the current node is not NULL 
    - if the `current node`'s value is the `target` value
        - return true 
    - set the `current node` to what the current node's `next` property is pointing to
- return false

COMPLEXITY 
Iterative Solution 
- N: the number of nodes in the list 
- time: O(N)
- space: O(1)

Recursive Solution 
- N: the number of nodes in the list 
- time: O(N)
- space: O(N) --> stack frames take memory
*/

import Node from '../node.js';

const linkedListFind = (head, target) => {
    let currentNode = head; 
    while (currentNode !== null) {
        if (currentNode.val === target) {
            return true
        }
        currentNode = currentNode.next;
    }
    return false;
}; 

// const linkedListFind = (head, target) => {
//     if (head === null) {
//         return false;
//     }

//     if (head.val === target) {
//         return true;
//     }

//     return linkedListFind(head.next, target);
// }




const a = new Node("a");
const b = new Node("b");
const c = new Node("c");
const d = new Node("d");

a.next = b;
b.next = c;
c.next = d;

// a -> b -> c -> d
console.log(linkedListFind(a, "c")); // true


// const a = new Node("a");
// const b = new Node("b");
// const c = new Node("c");
// const d = new Node("d");

// a.next = b;
// b.next = c;
// c.next = d;

// // a -> b -> c -> d

// console.log(linkedListFind(a, "d")); // true


// const a = new Node("a");
// const b = new Node("b");
// const c = new Node("c");
// const d = new Node("d");

// a.next = b;
// b.next = c;
// c.next = d;

// // a -> b -> c -> d

// console.log(linkedListFind(a, "q")); // false


// const node1 = new Node("jason");
// const node2 = new Node("leneli");

// node1.next = node2;

// // jason -> leneli

// console.log(linkedListFind(node1, "jason")); // true


// const node1 = new Node(42);

// 42

// console.log(linkedListFind(node1, 42)); // true
// const node1 = new Node(42);

// 42

// console.log(linkedListFind(node1, 100)); // false