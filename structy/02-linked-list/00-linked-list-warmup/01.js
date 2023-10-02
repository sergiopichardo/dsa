import Node from "../node.js";
import printLinkedList from "../printLinkedList.js";

const a = new Node('A');
const b = new Node('B');
const c = new Node('C');
const d = new Node('D');

a.next = b;
b.next = c;
c.next = d;

// A -> B -> C -> D -> NULL

printLinkedList(a);