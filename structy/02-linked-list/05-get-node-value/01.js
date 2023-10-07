/*
reverse list
Write a function, reverseList, that takes in the head of a linked list as an argument. The function should reverse the order of the nodes in the linked list in-place and return the new head of the reversed linked list.
*/

/*
INPUT: Node (head)
OUTPUT: Node (reversed linked list head)

RULES 
- it should reverse the order of the nodes in the linked list 
- it should reverse the linked list "in-place"
- it should return the head of the reverse linked list 

Assumptions 
- A valid linked list with at least one Node will always be provided
    - we'll never get NULL as a value 

Exploration 
T1
tail = null
rest
tail <- a <- b <- c -> d -> e -> f -> NULL

tail = null  

while current !== null 
    current.next = tail
    rest = current.next
    current = current.next 

b -> c -> d -> e -> f -> NULL

a <- b <- c <- d <- e <- f <- NULL

DATA STRUCTURE 
- original linked list (mutated)

ALGORITHM 
--> given a `head` parameter representing a linked list node

- set `prev` to NULL 
- set `curr` to `head` 
- set `next` to `head.next` 

- while `curr` is NOT NULL 
    - set `curr.next` to `prev`
    - set `next` to `curr.next`
    - set `curr` to `next`
    - set `prev` to `curr`
- return `prev`

COMPLEXITY (Iterative solution)
- N = # of nodes
- Time: O(N)
- Space: O(1)
*/

import Node from '../node.js';

/*
const reverseList = (head) => {
    let prev = null; 
    let curr = head; 
    let next = curr.next;

    while (curr !== null) {
        curr.next = prev;
        next = curr.next;
        curr = next; 
        prev = curr;
    }

    return prev;
};
*/

const reverseLinkedList = (head) => {
    let current = head; 
    let prev = null; 
    
    while (current !== null) {
        const next = current.next;
        current.next = prev; 
        prev = current;
        current = next;
    }

    return prev;
}; 


const a = new Node("a");
const b = new Node("b");
const c = new Node("c");
const d = new Node("d");
const e = new Node("e");
const f = new Node("f");

a.next = b;
b.next = c;
c.next = d;
d.next = e;
e.next = f;

// a -> b -> c -> d -> e -> f

console.log(reverseList(a)); // f -> e -> d -> c -> b -> a


const x = new Node("x");
const y = new Node("y");

x.next = y;

// x -> y

console.log(reverseList(x)); // y -> 


const p = new Node("p");

// p

console.log(reverseList(p)); // p
