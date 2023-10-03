/*
Complexity
n: number of nodes
- Time: O(N)
- Space: O(N) --> Stack frame takes amount of memory
*/


const sumList = (head) => {
    if (head === null) {
        return 0;
    }

    return head.val + sumList(head.next);
};