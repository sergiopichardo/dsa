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

const getNodeValue = (head, targetIndex, currentIndex=0) => {
    if (head === null) {
        return null
    }

    if (targetIndex === currentIndex) {
        return head.val;
    }

    return getNodeValue(head.next, targetIndex, currentIndex + 1);
}


const a = new Node("a");
const b = new Node("b");
const c = new Node("c");
const d = new Node("d");

a.next = b;
b.next = c;
c.next = d;

// a -> b -> c -> d
console.log(getNodeValue(a, 0)); // null

