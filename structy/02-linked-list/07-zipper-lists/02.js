/*
Complexity
- Time: O(min(m, n))
- Space: O(n)

*/

import Node from '../node.js';

const zipperLists = (head1, head2) => {
    if (head1 === null && head2 === null) return null; 
    if (head1 === null) return head2;
    if (head2 === null) return head1;

    const next1 = head1.next;
    const next2 = head2.next;
    head1.next = head2;
    head2.next = zipperLists(next1, next2);
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