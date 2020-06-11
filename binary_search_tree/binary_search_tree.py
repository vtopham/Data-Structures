"""
Binary search trees are a data structure that enforce an ordering over 
the data they store. That ordering in turn makes it a lot more efficient 
at searching for a particular piece of data in the tree. 

This part of the project comprises two days:
1. Implement the methods `insert`, `contains`, `get_max`, and `for_each`
   on the BSTNode class.
2. Implement the `in_order_print`, `bft_print`, and `dft_print` methods
   on the BSTNode class.
"""
class BSTNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):
        if value < self.value:
            #Try to put it on the left
            if self.left == None:
                self.left = BSTNode(value)
            else:
            #If there's already a node there, start over evaluating that node
                self.left.insert(value)
        else:
            #Try to put it on the right
            if self.right == None:
                self.right = BSTNode(value)
            else:
            #If there's already a node there, start over evaluating that node
                self.right.insert(value)

      
        
    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        if target == self.value:
            return True
        elif target < self.value:
            if self.left == None:
                return False
            else: 
                return self.left.contains(target)
        else:
            if self.right == None:
                return False
            else:
                return self.right.contains(target)
            
        

    # Return the maximum value found in the tree
    def get_max(self):
        if self.right == None:
            return self.value
        else:
            return self.right.get_max()
        


    # Call the function `fn` on the value of each node
    def for_each(self, fn):
        fn(self.value)
        if self.left != None:
            self.left.for_each(fn)
        if self.right != None:
            self.right.for_each(fn)

    # Part 2 -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self, node):
        
        if node.left:
            #go to the left as far as you can
            node.in_order_print(node.left)
        #before you go right, print the value
        print(node.value)
        if node.right:
            #before you go to the right print yourself, since you're smaller
            node.in_order_print(node.right)
            
        


    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    def bft_print(self, node):
        queue = [node]

        while len(queue) > 0:
            #print the value
            print(queue[0].value)
            #add its children to the end of the queue
            if queue[0].left:
                queue.append(queue[0].left)
            if queue[0].right:
                queue.append(queue[0].right)
            #remove it from the queue
            queue.pop(0)

    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self, node):
        stack = [node]
        while len(stack) > 0:
            #save the node
            eval_node = stack[0]
            #print and remove
            print(eval_node.value)
            stack.pop(0)
            #add the children to the stack
            if eval_node.right:
                stack.insert(0,eval_node.right)
            if eval_node.left:
                stack.insert(0,eval_node.left)
            
            
            


    # Stretch Goals -------------------------
    # Note: Research may be required

    # Print Pre-order recursive DFT
    def pre_order_dft(self, node):
        stack = [node]

        while len(stack) > 0:
            #because we'll be adding to the top of the stack i figured i'd grab this value this way
            eval_node = stack[0]
            #print that baby
            print(eval_node.value)
            #get it off the stack
            stack.pop(0)
            #add the children to the stack
            if eval_node.right:
                stack.insert(0,eval_node.right)
            if eval_node.left:
                stack.insert(0,eval_node.left)

    # Print Post-order recursive DFT
    def post_order_dft(self, node):
        pass
