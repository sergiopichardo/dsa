/*
zipper lists
Write a function, zipperLists, that takes in the head of two linked lists as arguments. The function should zipper the two lists together into single linked list by alternating nodes. If one of the linked lists is longer than the other, the resulting list should terminate with the remaining nodes. The function should return the head of the zippered linked list.

Do this in-place, by mutating the original Nodes.

You may assume that both input lists are non-empty.
*/

/*
INPUT: Node, Node
OUTPUT: Node

RULES 
- it should "zipper" the two linked lists together into single linked lists by alternating nodes 
- if one of the lists is longer than the other one, the resulting list should terminate with the remaining nodes of the longer list 
- it should return the head of the zipper linked list 
- the alternating of the lists should be done "in-place"
- assume that bothe input lists are non-empty 

TESTS 
T1
input: 
--> LL1: a -> b -> c
--> LL2: x -> y -> z

output: 
--> a -> x -> b -> y -> c -> z 

T2: 
input: 
--> LL1: a -> b -> c -> d -> e
--> LL2: y -> z

output: 
--> a -> y -> b -> z -> c -> d -> e 

DATA STRUCTURES/VARIABLES  
- `current1`
- `current2`
- `tail`
- `count` 

CASES 
- the value of `count` is even 
- the value of `count` is odd 
- either `current1` or `current2` are null

ALGORITHM 
- set `current1` to `head1`
- set `current2` to `head2`
- set `count` to 0
- set `tail` to `current1`

- while current1 is NOT NULL OR current1 is not NULL
    - if `count` is even 
        - tail.next = `current1`
        - `current1` = `current1.next`
    - otherwise
        - tail.next = `current2`
        - `current2` = `current2.next`
    - increment `count` by 1 
    - move up tail 

- if `current1` is NULL
    - attach `current2`
- if `current2` is NULL 
    - attach `current1

- return `head1`

COMPLEXITY
n: length of list 1 
m: length of list 2 

Time: O(min(n, m))
Space: O(1) - we're simply re-organizing the nodes
*/


import Node from '../node.js';

const zipperLists = (head1, head2) => {
    let tail = head1;
    let current1 = head1.next; 
    let current2 = head2; 
    let count = 0; 

    while (current1 !== null && current2 !== null) {
        if (count % 2 === 0) {
            // we attach current2 b/c tail is already starting with current1
            tail.next = current2; 
            current2 = current2.next;
        } else {
            tail.next = current1; 
            current1 = current1.next;
        }
        tail = tail.next;
        count += 1;
    }

    if (current1 === null) {
        tail.next = current2;
    }

    if (current2 === null) {
        tail.next = current1;
    }

    console.log(JSON.stringify(head1))
    return head1;
};

const a = new Node("a");
const b = new Node("b");
const c = new Node("c");
a.next = b;
b.next = c;
// a -> b -> c

const x = new Node("x");
const y = new Node("y");
const z = new Node("z");
x.next = y;
y.next = z;

// x -> y -> z

console.log(zipperLists(a, x)); // a -> x -> b -> y -> c -> z

// const a = new Node("a");
// const b = new Node("b");
// const c = new Node("c");
// const d = new Node("d");
// const e = new Node("e");
// const f = new Node("f");
// a.next = b;
// b.next = c;
// c.next = d;
// d.next = e;
// e.next = f;
// // a -> b -> c -> d -> e -> f

// const x = new Node("x");
// const y = new Node("y");
// const z = new Node("z");
// x.next = y;
// y.next = z;
// // x -> y -> z



// console.log(zipperLists(a, x));
// // a -> x -> b -> y -> c -> z -> d -> e -> f
// const s = new Node("s");
// const t = new Node("t");
// s.next = t;
// // s -> t

// const one = new Node(1);
// const two = new Node(2);
// const three = new Node(3);
// const four = new Node(4);
// one.next = two;
// two.next = three;
// three.next = four;
// // 1 -> 2 -> 3 -> 4



// console.log(zipperLists(s, one));
// // s -> 1 -> t -> 2 -> 3 -> 4
// const w = new Node("w");

// // w

// const one = new Node(1);
// const two = new Node(2);
// const three = new Node(3);
// one.next = two;
// two.next = three;
// // 1 -> 2 -> 3 



// console.log(zipperLists(w, one));
// // w -> 1 -> 2 -> 3
// const one = new Node(1);
// const two = new Node(2);
// const three = new Node(3);
// one.next = two;
// two.next = three;
// // 1 -> 2 -> 3 

// const w = new Node("w");
// // w


// console.log(zipperLists(one, w));
// // 1 -> w -> 2 -> 3