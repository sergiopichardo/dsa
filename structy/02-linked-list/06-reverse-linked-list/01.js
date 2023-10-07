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

Mental Model 
The objective is to reverse the order of a singly linked list. To achieve this, we'll manipulate the `next` property of each node to reference the preceding one instead of the succeeding one.

Here's a step-by-step breakdown:
1. Initialize a Variable: Start by initializing a variable, prev, to NULL. This will represent the "previous" node as we traverse the list.
2. Traverse the List: As we move through each node in the linked list:
    - Temporarily store the current node's next reference (so we don't lose access to the remaining part of the list).
    - Update the current node's next property to point to prev (effectively reversing its direction).
    - Move forward in the list by updating the prev to be the current node and the current node to the temporarily stored next node.
3. Reach the End: Continue this process until we've traversed the entire list and the current node points to NULL.
4. Final Step: At this point, prev will be pointing to what used to be the last node, but it's now the first node in our reversed list. Return prev as the new head of the reversed linked list.


DATA STRUCTURE 
- set `prev` to NULL 

while `node` IS NOT NULL keep traversing
    - set `next` to the the current node's next property 
    - set the current node's next property to point to the `prev` node 
    - set `prev` to the current node 
    - set the current node to `next`
- return `prev`

COMPLEXITY 
> N: # of nodes in the linked list 
- Time: O(N)
- Space: O(1)
*/

import Node from '../node.js';

const reverseList = (node) => {
    let prev = null; 

    while (node !== null) {
        // Here, we save the reference to the rest of the linked list
        // otherwise, we'd lose it when we set the `next` property of the current node to the previous node
        const next = node.next;
        
        // Here, we actually execute the reversal. We set the `next` property of the current node to point to `prev` 
        // Like I previously mentioned, if we set this before next = current.next, we'd lose the rest of the linked list reference
        node.next = prev;

        // TRAVERSING THROUGH THE LINKED LIST 
        // We set `prev` to `current` to move the `prev` pointer forward, so now `prev` becomes the current node 
        prev = node;

        // Same as above, we move the current node to the reference stored in `next`, which holds the rest of the linked list
        node = next;
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

console.log(JSON.stringify(reverseList(a))); // f -> e -> d -> c -> b -> a


const x = new Node("x");
const y = new Node("y");

x.next = y;

// x -> y

console.log(reverseList(x)); // y -> 


const p = new Node("p");

// p

console.log(reverseList(p)); // p
