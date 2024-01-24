def print_list(head):
    result = []
    current_node = head
    while current_node is not None:
        result.append(str(current_node.val) + ' -> ')
        current_node = current_node.next

    joined_result = ''.join(result) + 'None'
    print(joined_result)