import Node from '../node.js';

/*
COMPLEXITY
> N: # of nodes 
- Time: O(N)
- Space: O(N)
*/


const reverseList = (current, prev=null) => {
    // base case 
    if (current === null) return prev;

    const next = current.next; // store rest of linked list
    current.next = prev; // reverse node reference

    // advance linked list
    prev = current;
    current = next;
    
    // recursive case
    return reverseList(current, prev)
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
