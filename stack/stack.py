"""
A stack is a data structure whose primary purpose is to store and
return elements in Last In First Out order. 

1. Implement the Stack class using an array as the underlying storage structure.
   Make sure the Stack tests pass.
2. Re-implement the Stack class, this time using the linked list implementation
   as the underlying storage structure.
   Make sure the Stack tests pass.
3. What is the difference between using an array vs. a linked list when 
   implementing a Stack?
"""

#Array implementation
# class Stack:
#     def __init__(self):
#         self.size = 0
#         self.storage = []

#     def __len__(self):
#         return self.size

#     def push(self, value):
#         self.storage.insert(0,value)
#         self.size = len(self.storage)

#     def pop(self):
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

class Stack:
    def __init__(self):
        self.size = 0
        self.storage = LinkedList()

    def __len__(self):
        return self.size

    def push(self, value):
        new_node = Node(value, self.storage.head)
        self.storage.head = new_node
        self.size += 1

    def pop(self):
        if self.size > 0:
            popped = self.storage.head
            self.storage.head = self.storage.head.next
            self.size -= 1
            return popped.value
        
