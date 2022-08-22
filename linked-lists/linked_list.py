class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def __repr__(self):
        return self.data
        
class LinkedList:
    def __init__(self, nodes=None):
        self.head = None
        if nodes is not None:
            node = Node(data=nodes.pop(0))
            self.head = node
            for elem in nodes:
                node.next = Node(data=elem)
                node = node.next


    def __repr__(self):
        node = self.head
        nodes = []
        while node is not None:
            nodes.append(node.data)
            node = node.next
        nodes.append('None')
        return " -> ".join(nodes)

    def __iter__(self):
        node = self.head
        while node is not None:
            yield node
            node = node.next
            
    def add_first(self, node):
        node.next = self.head
        self.head = node
    
    def add_last(self, node):
        if self.head is None:
            self.head = node
            return
        for current_node in self:
            pass
        current_node.next = node

    def add_after(self, target_node_data, new_node):
        if self.head is None:
            raise Exception("List is empty")

        for node in self:
            if node.data == target_node_data:
                new_node.next = node.next
                node.next = new_node
                return
        
        raise Exception("Node with data '%s' not found" % target_node_data)

    
if __name__ == '__main__':
    pass
    # add_after demo ***************
    # llist = LinkedList()
    # llist.add_after('a', Node('b'))
    # print(llist)

    # llist = LinkedList(['a', 'b', 'c', 'd'])
    # print(llist)

    # llist.add_after('c', Node('cc'))
    # print(llist)

    # llist.add_after('f', Node('g'))
    # print(llist)
    # add_after demo *******************

    # llist = LinkedList(['a', 'b', 'c', 'd'])
    # llist.add_last(Node('e'))
    # print(llist)
    # llist.add_last(Node('f'))
    # print(llist)



    # llist = LinkedList()
    # llist.add_first(Node('b'))
    # llist.add_first(Node('a'))
    # print(llist)



    # llist = LinkedList(['a', 'b', 'c', 'd', 'e'])
    # print(llist)

    # for node in llist:
    #     print(node)


    # llist = LinkedList()
    # first_node = Node('a')
    # llist.head = first_node
    
    # second_node = Node('b')
    # third_node = Node('c')
    # first_node.next = second_node
    # second_node.next = third_node
    # print(llist)
