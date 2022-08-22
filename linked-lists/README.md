* Linked lists are an ordered collection of objects
* Each element of a linked list is called a node
* Node
    * Every node has two different fields
    * Data contains the value to be stored in the node
    * Next contains a reference to th next node on the list

* A linked list is a collection of nodes
* The first node is called the head and it's used as the starting point for any iteration through the list
* The last node must have its next reference pointing to None to determine the end of the list

# Queues and Stacks
* Queue --- for a queue you use First-In/First-Out (FIFO) approach. This means that the first element inserted in the list is the first one to be retrieved
* Stack --- for a stack you use Last-In/First-Out (LIFO). The last element inserted int he list is the first to be retrieved.

* Because of the way you insert and retrieve elements from the edges of queues and stacks, linked lists are one of the most convenient ways to implement these data structures. 

# Graphs
* Graphs can be sued to show relationshisp between objects or to represent different types of networks.
* One of the most common ways to implement a graph is to use an adjacency list. A list of linked lists where each vertwex of the graph is stored alongside a collection of connected vertices

# Performance Comparison: Lists vs Linked Lists
* In python, lists are dynamic arrays. That means that the memory usage of both lists and linked lists is similar. This is different from other programming languages.

# Insertion and Delettion of Elements
* Linked lists are straightforward when it comes to insertion and deletion of elements at the beginning or end of a list. Time complexity is always constant O(1)
* Linked lists have a performacne advantage over normal lists when implementing a queue(FIFO) in which elements are continuously inserted and removed at the beginning of a list.
* However, LL and normal lists perform similarly when implementing stacks (LFIO).

# Retrieval of Elements
* When it comes to element lookup, lists perform much better than linked lists. When you know which element you want to access, lists can perform this operation in O(1) time. Linked lists take O(n) because you need to traverse the whole list to find the element
* When searching for a specific element, both lists and LL perform similarly with a time complexity of O(n). Both cases you need to iterate through the entire list to find the element you're looking for

