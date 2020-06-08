"""
A queue is a data structure whose primary purpose is to store and
return elements in First In First Out order. 

1. Implement the Queue class using an array as the underlying storage structure.
   Make sure the Queue tests pass.
2. Re-implement the Queue class, this time using the linked list implementation
   as the underlying storage structure.
   Make sure the Queue tests pass.
3. What is the difference between using an array vs. a linked list when 
   implementing a Queue?
   
Stretch: What if you could only use instances of your Stack class to implement the Queue?
         What would that look like? How many Stacks would you need? Try it!
"""
#Array implentation
# class Queue:
#     def __init__(self):
#         self.size = 0
#         self.storage = []
    
#     def __len__(self):
#         return self.size

#     def enqueue(self, value):
#         self.storage.append(value)
#         self.size = len(self.storage)

#     def dequeue(self):
#         if self.size > 0:
#             self.size = len(self.storage) - 1
#             return self.storage.pop(0)

#Linked list implementation
class Node:
    def __init__(self, value, next_node):
        self.value = value
        self.next = next_node

class LinkedList:
    def __init__(self, head = None, tail = None):
        self.head = head
        self.tail = tail

class Queue:
    def __init__(self):
        self.size = 0
        self.storage = LinkedList()
    
    def __len__(self):
        return self.size

    def enqueue(self, value):
        new_node = Node(value, None)
        if self.size == 0:
            self.storage.head = new_node
            self.storage.tail = new_node
        else:
            self.storage.tail.next = new_node
            self.storage.tail = new_node
        self.size += 1

    def dequeue(self):
        if self.size > 0:
            popped_node = self.storage.head
            self.storage.head = self.storage.head.next
            self.size -= 1
            return popped_node.value
