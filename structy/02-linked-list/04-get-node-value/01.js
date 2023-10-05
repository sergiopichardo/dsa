/*
get node value
Write a function, getNodeValue, that takes in the head of a linked list and an index. The function should return the value of the linked list at the specified index.

If there is no node at the given index, then return null.
*/

/*
INPUT: Node 
OUTPUT: string | null

RULES 
- it should return the value of the linked list at the specified index 
- if there's no node at the given index, then return null

ALGORITHM 
- Given the function `getNodeValue(head: Node, index: number)`

- if `index` is less than 0 
    - return NULL

- set `currentIndex` to 0
- set `currentNode` to `head`
- while `currentNode` is not NULL 
    - if `currentIndex` === `index`
        - return `currentNode`'s `val` property value 
    - increment `currentIndex` by 1 
    - set `currentNode` to currentNode.next
- return NULL 

COMPLEXITY 
- N: the number of nodes in the linked list 
- Time: O(N)
- Space: O(1)
*/
import Node from '../node.js';

const getNodeValue = (head, index) => {
    if (index < 0) return null;

    let currentIndex = 0; 
    let currentNode = head; 
    while (currentNode !== null) {
        if (currentIndex === index) {
            return currentNode.val
        }
        currentIndex += 1;
        currentNode = currentNode.next;
    }

    return null; 
}


// const a = new Node("a");
// const b = new Node("b");
// const c = new Node("c");
// const d = new Node("d");

// a.next = b;
// b.next = c;
// c.next = d;

// // a -> b -> c -> d
// console.log(getNodeValue(a, 2)); // 'c'



// const a = new Node("a");
// const b = new Node("b");
// const c = new Node("c");
// const d = new Node("d");

// a.next = b;
// b.next = c;
// c.next = d;

// // a -> b -> c -> d

// getNodeValue(a, 3); // 'd'


const a = new Node("a");
const b = new Node("b");
const c = new Node("c");
const d = new Node("d");

a.next = b;
b.next = c;
c.next = d;

// a -> b -> c -> d

console.log(getNodeValue(a, 7)); // null



// const node1 = new Node("banana");
// const node2 = new Node("mango");

// node1.next = node2;

// // banana -> mango

// getNodeValue(node1, 0); // 'banana'
// const node1 = new Node("banana");
// const node2 = new Node("mango");

// node1.next = node2;

// // banana -> mango

// getNodeValue(node1, 1); // 'mango'