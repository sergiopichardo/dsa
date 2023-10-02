import Node from "./node"

export default class LinkedList {
    /**
     * 
     * @param {Array<any>} items 
     */
    constructor(items) {
        this.items = items.map(item => {
            return new Node(item);
        })
    }
}