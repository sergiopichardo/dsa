export default function printLinkedList(head) {
    if (head === null) return;
    console.log(head.val);
    printLinkedList(head.next)
}

// export default function printLinkedList(head) {
//     let currentNode = head;
//     while (currentNode.next !== null) {
//         console.log(currentNode.val);
//         currentNode = currentNode.next;
//     }
// }