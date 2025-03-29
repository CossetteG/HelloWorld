
'''your bst here'''
class BST:
    
    class Node:
        def __init__(self, value):
            self.value = value
            self.left = None
            self.right = None
            self.depth = 0

        def leaf(self):
            if(self.left == None):
                if (self.right == None):
                    return True
            return False

        def __str__(self):
            return self.value

    def __init__(self):
        self._root = None 
        self._size = 0
        self._height = -1

    def size(self):
        return self._size

    def is_empty(self):
        if (self._size == 0):
            return True
        return False

    def height(self):
        return self._height

    def add(self, item):
        curr = self.Node(item)

        if (self.is_empty()):
            self._root = curr 
        else: 
            compare = self._root

            while (True):
                curr.depth += 1
                if (curr.value <= compare.value):
                    if (compare.left == None):
                        compare.left = curr
                        break
                    else:
                        compare = compare.left
                elif (curr.value > compare.value):
                    if (compare.right == None):
                        compare.right = curr
                        break
                    else:
                        compare = compare.right 


        if (curr.depth > self._height):
            self._height = curr.depth
        self._size +=1

    def recalculate_height(self):
        start = self._root
        self._height = -1

        def inorder_dep(node):
            if(node.left != None):
                inorder_dep(node.left)
            
            if (node.depth > self._height):
                self._height = node.depth

            if(node.right != None):
                inorder_dep(node.right)

        inorder_dep(start)


    def remove(self, item):
        curr = self._root
        parent = self._root
        which_child = ""

        while (curr.value != item):
            if (curr.leaf() ):
                break
            elif(curr == None):
                return
            else: 
                if (item < curr.value):
                    parent = curr
                    curr = curr.left
                    which_child = "left"
                elif (item > curr.value):
                    parent = curr
                    curr = curr.right 
                    which_child = "right"

        if (curr.leaf()):
            if (which_child=="left"):
                parent.left = None
            elif (which_child=="right"):
                parent.right = None 
            elif (curr == self._root):
                self._root = None
            
            self._size -= 1
            self.recalculate_height() 
        else:
            sub = curr
            if (curr.right != None):
                sub = curr.right
                while(sub.left != None):
                    sub = sub.left
            elif (curr.left != None): 
                sub = curr.left 
                while(sub.right != None):
                    sub = sub.right
            else: raise "Logic Error in Remove"
            temp = sub.value
            self.remove(sub.value)
            curr.value = temp

        return self

    def find(self, item):
        curr = self._root
        if (self.is_empty()):
            raise ValueError

        while (curr.value != item):
            # if (curr.leaf()):
            #     raise ValueError
            # else: 
                if (item < curr.value):
                    curr = curr.left
                    if (curr == None):
                        raise ValueError
                elif (item > curr.value):
                    curr = curr.right 
                    if (curr == None):
                        raise ValueError

        return curr.value

    def inorder(self):
        result = []
        start = self._root

        def inorder_rec(node):
            if(node.left != None):
                inorder_rec(node.left)
            
            result.append(node.value)

            if(node.right != None):
                inorder_rec(node.right)

        inorder_rec(start)
        return result

    def preorder(self):
        result = []
        start = self._root

        def inorder_rec(node):
            result.append(node.value)

            if(node.left != None):
                inorder_rec(node.left)

            if(node.right != None):
                inorder_rec(node.right)

        inorder_rec(start)
        return result

    def postorder(self):
        result = []
        start = self._root

        def inorder_rec(node):
            if(node.left != None):
                inorder_rec(node.left)

            if(node.right != None):
                inorder_rec(node.right)

            result.append(node.value)

        inorder_rec(start)
        return result

    def print_tree(self):
        print(self.inorder())
    

#main.py
'''
Project 6: Binary Search Tree
Author: Cossette Gomez
Course: CS 2420
Date: 3/24/25

Description: class BST is to create a binary tree, then an implemation of it using Pair

Lessons Learned: binary trees

'''
from pathlib import Path
from string import whitespace, punctuation
#from bst import BST


class Pair:
    ''' Encapsulate letter,count pair as a single entity.
    
    Realtional methods make this object comparable
    using built-in operators. 
    '''
    def __init__(self, letter, count = 1):
        self.letter = letter
        self.count = count
    
    def __eq__(self, other):
        return self.letter == other
    
    def __hash__(self):
        return hash(self.letter)

    def __ne__(self, other):
        return self.letter != other

    def __lt__(self, other):
        return self.letter < other

    def __le__(self, other):
        return self.letter <= other

    def __gt__(self, other):
        return self.letter > other

    def __ge__(self, other):
        return self.letter >= other

    def __repr__(self):
        return f'({self.letter}, {self.count})'
    
    def __str__(self):
        return f'({self.letter}, {self.count})'

def make_tree():
    ''' A helper function to build the tree.
    
    The test code depends on this function being available from main.
    :param: None
    :returns: A binary search tree
    '''
    atw_tree = BST()
    with open("around-the-world-in-80-days-3.txt", 'r') as txt_file:
        content = txt_file.read()
        for char in content:
            if (char.isspace()): 
                pass
            else:
                char = char.lower()
                try: 
                    atw_tree.find(char).count += 1
                except ValueError:
                    new = Pair(char)
                    atw_tree.add(new)

    return atw_tree


def main():
    ''' Program kicks off here.

    '''
    my_tree = make_tree()
    print(my_tree.size())
    print(my_tree.height())
    print(my_tree.inorder())
    print(my_tree.preorder())
    print(my_tree.postorder())

    #testing 
    # mytree = BST()
    # print(f"Is the tree empty? {mytree.is_empty()}")

    # mytree.add(6)
    # mytree.add(5)
    # mytree.add(12)
    # mytree.add(14)
    # mytree.add(8)
    # mytree.add(3)
    # mytree.add(10)

    # print(f"Is the tree empty? {mytree.is_empty()}")
    # print(f"tree height? {mytree.height()}")
    # print(f"tree size? {mytree.size()}")

    # mytree.print_tree()
    # print(mytree.preorder())
    # print(mytree.postorder())

    # mytree.remove(6)
    # mytree.print_tree()
    # print(f"tree height? {mytree.height()}")
    # print(f"tree size? {mytree.size()}")
    
if __name__ == "__main__":
    main()
